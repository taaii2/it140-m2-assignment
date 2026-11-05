"""Ask for a user's name and age and calculate their approximate birth year.

Input:
    Name as a string entered by the user.
    Age as an interger entered by the user.

Process:
    Subtract the user's age from the current year.
    Assume the user has already had their birthday this year.
Output:
    A string displayed on the screen with the user's name and birth year. 

Typical usage example:
    What is nyour name? Thomas
    How old are you? 29
    Hello Thomas! You were born in 1997.
"""

# === Imports ===
from datetime import date

# === Constants ===
CURRENT_YEAR = date.today().year  # Get current year from system as integer


# === Main Function ===
def main() -> None:
    """Run the name-age program."""

    # Get user input.
    name = input("What is your name? ")
    age = int(input("How old are you? "))

    # Calculate user's approximate birth year.
    birth_year = CURRENT_YEAR - age

    # Output personalized message with user's name and birth year.
    print()
    print(f"Hello {name}! You were born in {birth_year}.")


# === Main Guard ===
if __name__ == "__main__":
    main()


