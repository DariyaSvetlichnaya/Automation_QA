celsius = float(input('Please enter temperature in Celsius: '))

# Converting to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Converting to Kelvin
kelvin = celsius + 273.15

# Printing the results in Fahrenheit and Kelvin
print('%0.1f Celsius = %0.1f Fahrenheit.' % (celsius, fahrenheit))
print('%0.1f Celsius = %0.1f Kelvin.' % (celsius, kelvin))
