def sum():
    while number== int(number) and number== float(number):
        total_sum= counter + number




def main():
    counter= 0
    number= input("introduce un número para realizar la suma porfavor")
    try:
        sum()
         print("la suma total es: ", total_sum)

    except TypeError:
        print("nuumbers must be integers or float")

    except KeyboardInterrupt:
        print("programm aborted by the user ")


