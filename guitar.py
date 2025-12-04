"""
CP1404/CP5632 - Guitar class from practicals
"""
from datetime import datetime

VINTAGE_AGE = 50


class Guitar:
    """Guitar class for storing details of a guitar."""

    def __init__(self, name="", year=0, cost=0.0):
        """Initialise a Guitar."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self, ):
        """Return a string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __repr__(self):
        """Return a developer-friendly string representation of a Guitar."""
        return f"{vars(self)}"

    def get_age(self):
        """Get the age of a guitar based on its year and the current year."""
        current_year = datetime.now().year
        return current_year - self.year

    def is_vintage(self):
        """Determine if a Guitar is considered vintage or not based on age."""
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        """Determine if Guitar is considered less than the other object based on year (older is less than younger)."""
        return self.year < other.year
