
def celsius_to_fahrenheit(temps):

    return[(temp*9/5)+32 for temp in temps]
print(celsius_to_fahrenheit([1,2,3,4,5]))
