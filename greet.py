"""Trivial module providing greet and farewell functions for the sandbox Delivery cycle."""


def greet(name: str) -> str:
    return f"Hello, {name}!"


def farewell(name: str) -> str:
    return f"Goodbye, {name}!"


if __name__ == "__main__":
    print(greet("world"))
    print(farewell("world"))
