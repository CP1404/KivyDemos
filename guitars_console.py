"""CP1404 Guitars console program"""
import json
from guitar import Guitar


def main():
    """Simple program to load and display guitars."""
    filename = "guitars.json"
    guitars = load_guitars()
    print(f"{len(guitars)} guitars loaded from {filename}")
    for guitar in guitars:
        print(guitar)


def load_guitars(filename="guitars.json"):
    """Load guitars from filename"""
    guitars = []
    with open(filename) as in_file:
        records = json.load(in_file)
    for record in records:
        guitars.append(Guitar(**record))
    return guitars


if __name__ == '__main__':
    main()
