# MBTA Adafruit Matrix Portal M4 Display
# Updated for CircuitPython 9.x.x
# Based on original work Train_schedule_board by Jorge Enrique Gamboa Fuentes
# Vibe coded into working after upgrade of circuitpython and wifi/ble drivers by bk @bklevence on github
# Data from: Boston - MBTA
# 
# Note 
# I've kept this running for about 6 hours and noticed a memory allocation issue maybe once 
# Have not had time to recreate with a serial connection to PC to log errors
# I may come back to include a restart every few hours, but this is better than my first iteration 

import time
import microcontroller
import gc
import json
import board
import displayio
import adafruit_display_text.label
import os
from adafruit_datetime import datetime
from adafruit_bitmap_font import bitmap_font
from adafruit_matrixportal.matrix import Matrix
from adafruit_matrixportal.network import Network


# --- CONFIGURABLE PARAMETERS ---
# I may do an overview of these, but for now see below
# https://jegamboafuentes.medium.com/i-created-my-own-subway-arrival-board-with-real-time-data-to-dont-miss-my-train-anymore-28bfded312c0
BOARD_TITLE = 'Porter'
STOP_ID = 'place-portr'
DIRECTION_ID = '0'
ROUTE = 'Red'
BACKGROUND_IMAGE = 'Tred-dashboard.bmp'
PAGE_LIMIT = '3'
DATA_SOURCE = f'https://api-v3.mbta.com/predictions?filter%5Bstop%5D={STOP_ID}&filter%5Bdirection_id%5D={DIRECTION_ID}&page%5Blimit%5D={PAGE_LIMIT}&sort=departure_time'
UPDATE_DELAY = 15
SYNC_TIME_DELAY = 30
ERROR_RESET_THRESHOLD = 3


# Rotation setting - 0, 90, 180, or 270 degrees clockwise
# Useful as I needed to put this on my fridge
DISPLAY_ROTATION = 180
# --- END CONFIGURABLE PARAMETERS ---

def get_arrival_in_minutes_from_now(now, date_str):
    """Calculates minutes from now to a given time."""
    try:
        train_date = datetime.fromisoformat(date_str).replace(tzinfo=None)
        return round((train_date - now).total_seconds() / 60.0)
    except (ValueError, TypeError):
        return -999

def get_arrival_times_optimized():
    """Fetches and parses train arrival times with memory efficiency."""
    now = datetime.now()
    print(f"Current time: {now}")
    print(f"Fetching from: {DATA_SOURCE}")

    predictions = []
    try:
        # Use fetch instead of get for libraries etc
        response = network.fetch(DATA_SOURCE)
        data = response.json()
        response.close()

        for prediction in data.get("data", []):
            departure_time = prediction.get("attributes", {}).get("departure_time")
            if departure_time:
                predictions.append(departure_time)

        del data
        gc.collect()

    except (RuntimeError, ValueError) as e:
        print(f"Network or JSON parsing error: {e}")
        return (-999, -888, -777)

    train_minutes = [get_arrival_in_minutes_from_now(now, p_time) - 1 for p_time in predictions]

    while len(train_minutes) < 3:
        train_minutes.append(-777)

    return tuple(train_minutes[:3])

def format_text(minutes):
    """Formats the time in minutes into a display string."""
    if minutes < 0:
        if minutes in [-999, -888, -777]:
            return "----"
        else:
            return "brding"
    if minutes <= 0:
        return "brding"
    if minutes < 10:
        return f"{minutes}  min"
    return f"{minutes} min"

def update_display_text(t1, t2, t3):
    """Updates the text labels on the display."""
    text_lines[1].text = format_text(t1)
    text_lines[2].text = format_text(t2)
    text_lines[3].text = format_text(t3)
    text_lines[1].color = colors[2] if format_text(t1) == "brding" else colors[1]
    display.root_group = group   # corrected for updated libraries

# --- Main setup, runs once ---
matrix = Matrix(rotation=DISPLAY_ROTATION)
display = matrix.display
network = Network(status_neopixel=board.NEOPIXEL, debug=False)
group = displayio.Group()
colors = [0x444444, 0xDD8000, 0x9966cc]

tile_grid = None
try:
    if BACKGROUND_IMAGE:
        bitmap = displayio.OnDiskBitmap(open(BACKGROUND_IMAGE, "rb"))
        tile_grid = displayio.TileGrid(bitmap, pixel_shader=getattr(bitmap, 'pixel_shader', displayio.ColorConverter()))
except (OSError, ValueError) as e:
    print(f"Could not load background image '{BACKGROUND_IMAGE}': {e}")
    bitmap = displayio.Bitmap(64, 32, 1)
    palette = displayio.Palette(1)
    palette[0] = 0x000000
    tile_grid = displayio.TileGrid(bitmap, pixel_shader=palette)

if tile_grid:
    group.append(tile_grid)

font = bitmap_font.load_font("fonts/6x10.bdf")

text_lines = [
    adafruit_display_text.label.Label(font, color=colors[0], x=20, y=3, text=BOARD_TITLE),
    adafruit_display_text.label.Label(font, color=colors[1], x=26, y=11, text="- min"),
    adafruit_display_text.label.Label(font, color=colors[1], x=26, y=20, text="- min"),
    adafruit_display_text.label.Label(font, color=colors[1], x=26, y=28, text="- min"),
]

for line in text_lines:
    group.append(line)

display.root_group = group   # corrected for updated libraries

error_counter = 0
last_time_sync = None
print("Starting MBTA display...")
gc.collect()
print(f"Free memory: {gc.mem_free()} bytes")

# --- Main loop ---
while True:
    try:
        if last_time_sync is None or time.monotonic() > last_time_sync + SYNC_TIME_DELAY:
            network.get_local_time()
            last_time_sync = time.monotonic()
            gc.collect()

        arrivals = get_arrival_times_optimized()
        update_display_text(*arrivals)
        error_counter = 0

    except Exception as e:
        print(f"An error occurred: {e}. Retrying...")
        error_counter += 1
        gc.collect()

        if error_counter > ERROR_RESET_THRESHOLD:
            print("Too many errors. Resetting microcontroller...")
            microcontroller.reset()

    time.sleep(UPDATE_DELAY)
