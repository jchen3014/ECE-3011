# Imports go at the top
from find_i2c import *
from lcd_lib import *
import bme280
import music

LCD_I2C_ADDR = 39
BME280_I2CADDR = 0x76

# Make sure all I2C addresses are detected
# print(scan_i2c())

# Initialize devices
lcd = LCD1620()
bme = bme280.BME280(i2c)

# Intro
lcd.puts("Welcome to your")
lcd.puts("Hydroponic Garden!", y = 1)
music.play(music.RINGTONE)
sleep(1000)
lcd.clear()

# Continuously read temp and humidity from sensor
while True:
    temp, pres, humi = bme.values()
    lcd.puts("Temperature: {:.2f}F".format(temp))
    lcd.puts("Humidity: {:.2f}%".format(humi), y = 1)
    sleep(3000)
    






    
# x = pin1.read_digital()
# print(x)

# print("Temperature: {:.2f}F".format(temp))
# print("Pressure: {:.2f}inHg".format(pres))
# print("Humidity: {:.2f}%".format(humi))



