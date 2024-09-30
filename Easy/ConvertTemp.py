def convertTemperature(celsius: float) -> list[float]:
    kelvin = celsius + 273.15
    fahrenheit = celsius * 1.80 + 32.00
    return [kelvin, fahrenheit]

print(convertTemperature(36.50))