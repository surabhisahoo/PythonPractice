# name = input("Enter your name: ")
# print("Hello {}!!" .format(name))

hour = input("Enter hours: ")
rate = input("Enter rate: ")
try:
    hour = int(hour)
    rate = float(rate)
    if hour > 40:
        print("Pay: {}" .format((hour * rate)*1.5))
    else:
        print("Pay: {}".format(hour * rate))
except:
    print("Invalid input")
