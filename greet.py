"""Trivial module providing greet and farewell functions for the sandbox Delivery cycle."""

VERSION = "1.0"


def greet(name: str) -> str:
    return f"Hello, {name}!"


def farewell(name: str) -> str:
    return f"Goodbye, {name}!"


def birthday(name: str, age: int) -> str:
    return f"Happy birthday, {name}, you are {age}!"


if __name__ == "__main__":
    print(greet("world"))
    print(farewell("world"))
    print(birthday("world", 1))
    print(VERSION)
