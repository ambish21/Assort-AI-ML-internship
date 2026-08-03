"""
Main File
"""

from data import students
from report import generate_report


def main():
    generate_report(students)


if __name__ == "__main__":
    main()