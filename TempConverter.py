print("TEMPERATURE CONVERTER 1.0 by John Cash")
def converter():
    import time
    unit = input("Are you converting to Celsius or Fahrenheit [C/F]: ")
    if unit.upper() != "F" and unit.upper() != "C":
        print("Incorrect value, please input a correct value")
        converter()
    if unit.upper() == "C":
        temperature = input("What is the temperature in Fahrenheit?: ")
        converted = 5/9 * (float(temperature) - 32); print("That is", round(converted, 1), "degrees Celsius.")
    if unit.upper() == "F":
        temperature = input("What is the temperature in Celsius?: ")
        converted = (float(temperature) * 9/5) + 32; print("That is", round(converted, 1), "degrees Fahrenheit.")
    repeat = input("Would you like to convert another number? [Y/N]:")
    if repeat.upper() == "Y":
        converter()
    else:
        print("Bye!"), time.sleep(1.5)
        exit()
converter()

