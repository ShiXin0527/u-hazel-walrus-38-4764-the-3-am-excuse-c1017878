#!/usr/bin/env python3
"""Entry for make.fun bounty: The 3 AM Excuse

A tiny one-liner joke program. Run it and it prints the joke.
"""

JOKE = "Sorry I'm late. I was up at 3AM explaining to my computer that 'turn it off and on again' is not a personality trait."


def tell_joke():
    """Return the one-line joke for this bounty."""
    return JOKE


def main():
    print(tell_joke())


if __name__ == "__main__":
    main()
