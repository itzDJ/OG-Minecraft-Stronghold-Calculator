#!/usr/bin/env python3


def main():
    # importing the tangent trig function and pi value
    from math import tan, pi

    class points():
        x, z, f = 0, 0, 0

    firstPoint = points()
    secondPoint = points()

    try:
        # getting values for the coordinates and angles
        firstPoint.x = float(input("Name your first x value: "))
        firstPoint.z = float(input("Name your first z value: "))
        firstPoint.f = float(input("Name your first f value: "))
        secondPoint.x = float(input("Name your second x value: "))
        secondPoint.z = float(input("Name your second z value: "))
        secondPoint.f = float(input("Name your second f value: "))
    except ValueError:
        # runs if the try block returns an error and ends the program
        # the only error that can occur in the try block:
        #   if the input cannot be converted into a float (ex: if the input is not a number)
        print("That is not a number.")
    else:
        # runs if the try block runs successfully
        # solving for x and z coordinates of the stronghold
        z = ((firstPoint.z * tan(-firstPoint.f * pi / 180)) -
             (secondPoint.z * tan(-secondPoint.f * pi / 180)) - firstPoint.x +
             secondPoint.x) / (tan(-firstPoint.f * pi / 180) -
                               tan(-secondPoint.f * pi / 180))

        x = (z - firstPoint.z) * tan(-firstPoint.f * pi / 180) + firstPoint.x

        # output results
        print(f"\nThe stronghold is at {round(x), round(z)}.")


if __name__ == "__main__":
    main()
