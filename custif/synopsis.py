#!/usr/bin/env python3
""" TLG Learning | AAlegre
   if, elif, else - A simple program using conditionals to make a decision."""

# Film / book series with provided summaries.
print("Synopsis is available for the following films: ")
print("1 - Harry Potter")
print("2 - Fast and Furious")
print("3 - Injustice: Gods Among Us")
print("4 - Top Gun: Maverick")

# User requests the film they wish to receive a summary about.
selection = float(input("Please select the number of the film you wish to receive a synopsis about: "))

# Synopsises
if selection == 1:
    print("Harry Potter is a series of seven fantasy novels written by British author J. K. Rowling. The novels chronicle the lives of a young wizard, Harry Potter, and his friends Hermione Granger and Ron Weasley, all of whom are students at Hogwarts School of Witchcraft and Wizardry. The main story arc concerns Harry's conflict with Lord Voldemort, a dark wizard who intends to become immortal, overthrow the wizard governing body known as the Ministry of Magic and subjugate all wizards and Muggles (non-magical people).")
elif selection == 2:
    print("Fast & Furious (also known as The Fast and the Furious) is a media franchise centered on a series of action films that are largely concerned with street racing, heists, spies, and family.")
elif selection == 3:
    print("The film is directed by Matt Peters from a story by Ernie Altbacker and stars Justin Hartley and Anson Mount as Superman and Batman, respectively. The film, set in a separate continuity from the main DC Universe, follows Superman’s descent into madness after being tricked by Joker into killing his pregnant wife Lois Lane and detonating a nuclear weapon that destroys Metropolis. As Superman transforms the Earth into a police state to enforce global peace, Batman forms an underground resistance to oppose Superman and his allies.")
elif selection == 4:
    print("In the film, Maverick confronts his past while training a group of younger Top Gun graduates, including the son of his deceased best friend, for a dangerous mission.")
else:
    print("Summary not available, please select from the provided films.")
