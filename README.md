# MBTA Matrix Portal 
> Train scheduler board that displays Subway/Metro/Trains/Bus, next arrival schedules on real time based. -Enrique Gamboa @egamboafuentes . 

> [!IMPORTANT]
> You will want a settings.toml file to go along with the code.py. TL;DR: it's the better version of secrets.py. It will need to contain the following:

```
CIRCUITPY_WIFI_SSID = "YOUR SSID HERE"
CIRCUITPY_WIFI_PASSWORD = "YOUR WIFI PASSWORD HERE"

ADAFRUIT_AIO_USERNAME = "YOUR USERNAME"
ADAFRUIT_AIO_KEY = "YOUR PASS"
TIMEZONE = "America/New_York", # http://worldtimeapi.org/timezones
```

## WIP Status

- [x] Current project connected to public MBTA API V3 (Boston).
- [x] Update MatrixPortal M4 to current stable CircuitPython releases
    - [x] [Install CircuitPython](https://learn.adafruit.com/adafruit-matrixportal-m4/install-circuitpython)
        - [CircuitPython Download 9.2.8](https://circuitpython.org/board/matrixportal_m4/)
    - [x] [Wifi-BLE coprocessor update, nina](https://learn.adafruit.com/upgrading-esp32-firmware/upgrade-all-in-one-esp32-airlift-firmware)
        - [NINA_ADAFRUIT-esp32-3.1.0.bin](https://github.com/adafruit/nina-fw/releases/tag/3.1.0)
- [x] Update Libraries in /lib directory.
    - [x] [adafruit-circuitpython-bundle-9.x-mpy-20250810.zip](https://circuitpython.org/libraries)
- [ ] Get code.py on updated board.
- [ ] Debug.

 ## Links of interest
- [Adafruit Matrix Portal M4](https://www.adafruit.com/product/4745)
- [Original Medium writeup by Enrique I found.](https://jegamboafuentes.medium.com/i-created-my-own-subway-arrival-board-with-real-time-data-to-dont-miss-my-train-anymore-28bfded312c0?source=friends_link&sk=a229cfebc19bc9f1874ba3a0441f0620)
-  [Starting Point for this forked project.](https://github.com/jegamboafuentes/Train_schedule_board/tree/main/display_code/8-23-23/new)
