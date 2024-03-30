# DeskClock

Raspberry Pi Model 2B + Touch Screen turned into a desktop clock and
lightweight server endpoint for development. Or, run it as a window
on your computer.

## Python Packages

If you're not running this on a dedicated device, you will probably want a
virtualenv.

```shell
python -m venv .venv
source .venv/bin/activate
```
To install the python dependencies:

```shell
pip install -r requirements.txt
```

## Raspberry Pi OS Lite dependencies

```shell
sudo ./rpi-os-lite-installs.sh
```

## "MESA-LOADER: failed to open iris" Error

```shell
export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6
```