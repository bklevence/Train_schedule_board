# MBTA Matrix Portal 
> Train scheduler board that displays Subway/Metro/Trains/Bus, next arrival schedules on real time based. -Enrique Gamboa @egamboafuentes . 

## Overview

I was compelled to start using my MatrixPortal again. I previously used it as a [countdown to holidays](https://learn.adafruit.com/halloween-countdown-display-matrix) throughout the year in my classroom, however now as an at home caretaker for my kiddo I wanted to have it as something useful for my partner who takes the MBTA daily. I found Enrique's work, but it wasn't working correctly with my setup. So I updated everything and tinkered until I got something working again that matched my [MBTA stops webpage](https://www.mbta.com/stops/place-portr). See below for more working notes in [WIP Status](#WIP-Status). For a better writeup on how to successfully tune this to your MBTA line, stop, and travel direction check out [Enrique's Medium post](https://jegamboafuentes.medium.com/i-created-my-own-subway-arrival-board-with-real-time-data-to-dont-miss-my-train-anymore-28bfded312c0?source=friends_link&sk=a229cfebc19bc9f1874ba3a0441f0620). I may come back in the future to add that content here, but for now I'm just looking to get things working! :sunglasses:

> [!IMPORTANT]
> You will want to create a settings.toml file to go along with the code.py. TL;DR: [settings.toml is the better version of secrets.py](https://youtu.be/Ph8SHE1s89c?si=fGxQndlHP3gXufug). 
> 
> It will need to contain the following:

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
- [x] Get [code.py](code.py) on updated board.
- [ ] Debug.
    - [x] Fixed json memory allocation overload on second update.
    - [ ] Possible memory allocation issue over time(hrs) or json access overload.
        - [ ] Include reboot after x hours if this is a trend.
- [ ] Instructions on how to setup

 ## Links of interest
- [Adafruit Matrix Portal M4](https://www.adafruit.com/product/4745)
- [Adafruit 64x32 RGB LED Matrix - 4mm pitch](https://www.adafruit.com/product/2278)
- [MatrixPortal Documentation Guide](https://learn.adafruit.com/adafruit-matrixportal-m4)
- [Original Medium Post](https://jegamboafuentes.medium.com/i-created-my-own-subway-arrival-board-with-real-time-data-to-dont-miss-my-train-anymore-28bfded312c0?source=friends_link&sk=a229cfebc19bc9f1874ba3a0441f0620)
- [Upstream repository (ae2938fc52b9993b929b04ba700fe58fa47946cb) for my work here](https://github.com/jegamboafuentes/Train_schedule_board/tree/main/display_code/8-23-23/new)
- [MBTA Stops Webpage](https://www.mbta.com/stops/subway)
- [MBTA V3 API](https://www.mbta.com/developers/v3-api)