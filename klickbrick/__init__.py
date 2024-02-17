#!/usr/bin/env python3

"""
Klickbrick
"""


import argparse
import sys


def get_args():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        prog="klickbrick",
        description="An onboarding CLI for Klickbrick",
    )

    subparser = parser.add_subparsers(
        title="subcommands",
        description="valid subcommands",
        help="additional help",
    )

    hello_parser = subparser.add_parser("hello", help="Say hello")
    hello_parser.add_argument(
        "-n",
        "--name",
        metavar="name",
        default="World",
        help="The name to greet",
        type=str,
    )
    hello_parser.set_defaults(func=say_hello)

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    return parser.parse_args()


def say_hello(args) -> None:
    if not len(args.name) > 0:
        args.name = "World"
    print(f"Hello, {args.name.title()}!")


def main():
    args = get_args()
    args.func(args)


if __name__ == "__main__":
    main()
