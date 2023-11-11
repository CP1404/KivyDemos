"""CP1404 Guitars console program"""
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
    """Load guitars from filename"""
    guitars = []
    with open(filename) as in_file:
        records = json.load(in_file)
    print(repr(records))  # Let's see what the data looks like
    for record in records:
        guitars.append(Guitar(**record))
    return guitars


if __name__ == '__main__':
    main()
