#!/usr/bin/env python3
"""TLG Learning | AAlegre
   if, elif, else - A simple program using conditionals to make a decision."""

def main():

    # Requests the user to provide their final grade between 0 - 100 for the semester
    grade = float(input("What was you final score for the semester? "))

    # This if-elif-else section provides the appropriate letter grade.
    # Goes on the A - F system, and the Harry Potter OWL/NEWT Grading Standards
    if grade >= 90:
        print("Your final letter grade for the semester: A")
        print("Outstanding.")
    elif grade >= 80:
        print("Your final letter grade for the semester: B")
        print("Exceeds Expectations")
    elif grade >= 70:
        print("Your final letter grade for the semester: C")
        print("Acceptable")
    elif grade >= 60:
        print("Your final letter grade for the semester: D")
        print("Poor")
    elif grade > 0:
        print("Your final grade for the semester: F")
        print("Dreadful")
    else:
        print("Troll")

# Calls the function
main()