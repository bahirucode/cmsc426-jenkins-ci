"""Small Python app used to demonstrate a Jenkins CI pipeline (CMSC 426)."""


def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b


def main():
    print("Application started")
    result = add_numbers(2, 3)
    print(f"2 + 3 = {result}")


if __name__ == "__main__":
    main()
