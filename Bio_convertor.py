# Function for calculating how much to dilute a solution of known concentration.
def concetration(concentration_start,substance_volum,concentration_ultimate):

    if concentration_start > concentration_ultimate:
        water_volum = (concentration_start * substance_volum/concentration_ultimate) - substance_volum

    elif concentration_start == concentration_ultimate:
        water_volum = "Message"

    else:
        water_volum = "None"

    return water_volum

# Volume converter. The input is a number and 2 dimensions - initial and final.
def volume_converter(value,dimension_to_convert,finish_dimension):

    if dimension_to_convert == "ml":

        if finish_dimension == "l":
            convertation = value/1000

        elif finish_dimension == "mcl":
            convertation = value*1000

    elif dimension_to_convert == "mcl":

        if finish_dimension == "l":
            convertation = value/1000000

        elif finish_dimension == "ml":
            convertation = value/1000

    elif dimension_to_convert == "l":

        if finish_dimension == "ml":
            convertation = value*1000

        elif finish_dimension == "mcl":
            convertation = value*1000000

    return convertation
# Function for calculating the speed or acceleration of the centrifuge depending on the user's choice
def rotor(radius,operation,parametr):

    if operation == "RPM":
        from math import sqrt
        value = sqrt((parametr*10**5)/(1.118*radius))

    else:
        value = 1.118*radius*parametr**2/10**5

    return value
# Function body
for i in range(1000):
    print("\n Good day! Welcome to the set of converters used in molecular biology"
          "\n To calculate how much to dilute the solution, type \"сoncentration\""
          "\n To convert volumetric values, type \"volum\
          \n To calculate the speed and acceleration of the rotor, type \"rotor\" "
          "\n To exit, type \"exit\" ")

    command = input("Enter yor comand: ")

    if command == "exit":
        print("Bye!")
        break

    elif command == "сoncentration":

        try:
            concetration_start = float(input("Start concentration level: "))
        except:
            print ("Wrong value!")
            continue
        try:
            substance_volume = float(input("How much of the substance of the"
                                 " initial concentration do you want to take? "))
        except:
            print("Wrong value!")
            continue
        try:
            concentration_ultimate = int(input("What concentration of the "
                                       "substance do you want to get in the end?"))
        except:
            print("Wrong value!")
            continue

        if concetration(concetration_start,substance_volume,concentration_ultimate) != "None":
            print("You need to take {0} μl of substance and {1} μl of water to "
              "get a solution of concentration {2}".format(substance_volume,
                                                           concetration(concetration_start,
                                                                        substance_volume,
                                                                        concentration_ultimate),
                                                           concentration_ultimate))
        else:
            print("Wrong value!")
            continue

    elif command == "volum":
        print ("I can work only with liters(use l), milliliters(use ml) or mikrolitry(use mcl)")

        try:
            value = float(input("Enter you volum: "))
        except:
            print("Wrong value")
            continue

        dimension_to_convert = input("Enter the starting dimension: ")
        finish_dimension = input("Enter the final dimension: ")

        if (dimension_to_convert in ["mcl","ml","l"]) and (finish_dimension in ["mcl","ml","l"]):
            print("I covert {0}{1} to {2}{3}".format(value,
                                                     dimension_to_convert,
                                                     volume_converter(value,
                                                                     dimension_to_convert,
                                                                     finish_dimension),
                                                     finish_dimension))
        else:
            print("I cannot convert it sorry!")
            continue

    elif command == "rotor":
        try:
            radius = float(input("Enter the centrifuge radius: "))
        except:
            print("Wrong value")
            continue

        operation = input("What do you want to calculate - "
                          "speed or acceleration (RPM) "
                              "or acceleration (RCF)?")
        if radius <= 0:
            print("You Joker!")
            continue


        if operation == "RPM":

            try:
                parametr = float(input("Enter RCF: "))
            except:
                print("Wrong value")
                continue

            print("Your speed is {0} rpm".format(rotor(radius,operation,parametr)))

        elif operation == "RCF":
            try:
                parametr = float(input("Enter RPM: "))
            except:
                print("Wrong value")
                continue

            print("Your speed is {0} rcf".format(rotor(radius,operation,parametr)))

        else:
            print("Sorry, I cannot do that!")
            continue
    else:
        print("Wrong operation!")
        continue
