#!/usr/bin/env python3
# Created by: Adrian student
# Created on: 01st Sept 2026
# This program is a guessing game in which the user
# tries to guess a number between 0 and 9
import constants


def main():
    # get the user number between 0 and 9
    user_number = int(input("enter your number between 0 and 9:"))
    print("")

    # check if number is the number is right
    if user_number == constants.CR:
        print("you are right")
    if user_number != constants.CR:
        print("you are wrong")

    # display correct number if wrong
    if user_number != constants.CR:
        print("The correct number is :{}".format(constants.CR))


if __name__ == "__main__":
    main()
