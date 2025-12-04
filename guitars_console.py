"""CP1404/CP5632 - Guitars console program"""
import json
from guitar import Guitar


def main():
    """Simple program to load and display guitars."""
    filename = "guitars.json"
    guitars = load_guitars(filename)
    print(f"{len(guitars)} guitars loaded from {filename}")
    for guitar in guitars:
        print(guitar)


def load_guitars(filename):
    """Load guitars from JSON file."""
    guitars = []
    with open(filename) as in_file:
        records = json.load(in_file)
    # For debugging: Let's see what the data looks like (a list of dictionaries)
    print(repr(records))
    for record in records:
        # Use ** dictionary unpacking to provide key:value pairs to the Guitar constructor
        guitars.append(Guitar(**record))
    return guitars


if __name__ == '__main__':
    main()
