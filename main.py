# Imports
from find_i2c import *
from lcd_lib import *
import bme280
import music

LCD_I2C_ADDR = 39
BME280_I2CADDR = 0x76

# Make sure all I2C addresses are detected
# print(scan_i2c())

# Initialize devices and pins
lcd = LCD1620()
bme = bme280.BME280(i2c)
pin1.set_pull(pin1.PULL_DOWN)

# Intro
lcd.puts("Welcome to your")
lcd.puts("Hydroponic Garden!", y = 1)
music.play(music.ENTERTAINER)
sleep(1750)
lcd.clear()

# Continuously read temp and humidity from sensor
# and trigger water pump if necessary
while True:
    x = pin0.read_digital()
    #print(x)
    if (x == 1):
        pin1.write_digital(1)
        #print("pumping water")
    else: 
        pin1.write_digital(0)
        #print("not")
        
    temp, pres, humi = bme.values()
    lcd.puts("Temperature: {:.2f}F".format(temp))
    lcd.puts("Humidity: {:.2f}%".format(humi), y = 1)
    sleep(3000)

# print("Temperature: {:.2f}F".format(temp))
# print("Pressure: {:.2f}inHg".format(pres))
# print("Humidity: {:.2f}%".format(humi))