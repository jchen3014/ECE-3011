# Find all I2C device addresses on the I2C bus

from microbit import *

def scan_i2c():
    devices = []
    for addr in range(0, 128):
        try:
            i2c.read(addr, 1)
            devices.append(addr)
        except OSError:
            pass
    return devices