#!/usr/bin/env python3

# Created by Cristiano Sellitto
# Created in October 2022
# A program that finds if the user's number between 0 and 9 is equal to the hidden number

import constants


def main():
    # Finds if the chosen number from 0 to 9 is equal to the hidden number

    chosen_number = float(input("Enter a number from 0-9: "))
    if chosen_number == constants.HIDDEN_NUMBER:
        print("\nYou got the number right!")
    if chosen_number != constants.HIDDEN_NUMBER:
        print("\nYou got the number wrong.")

    print("\nDone.")


if __name__ == "__main__":
    main()
