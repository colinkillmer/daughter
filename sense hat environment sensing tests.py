from sense_hat import SenseHat
sense = SenseHat()
pressure = sense.get_pressure()
print(pressure)
temperature = sense.get_temperature()
print(temperature)
humidity = sense.get_humidity()
print(humidity)
