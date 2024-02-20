#!/usr/bin/env python3

import argparse
import sys

# sub-commands
from ejskb.sc.greeter import say_hello

# typing
from typing import List
from argparse import ArgumentParser, Namespace


class Klickbrick(object):
    """Klickbrick, an extensible CLI for onboarding."""

    def __init__(self, arguments: List[str]) -> None:
        self.parser: ArgumentParser = argparse.ArgumentParser(
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            prog="ejskb",
            description="An onboarding CLI for Klickbrick",
        )
        self.subparser = self.parser.add_subparsers(
            title="subcommands",
            description="available subcommands",
            help="description",
        )

        hello_parser: ArgumentParser = self.subparser.add_parser(
            "hello", help="Says hello"
        )
        hello_parser.add_argument(
            "-n",
            "--name",
            metavar="name",
            default="World",
            help="An optional name to greet",
            type=str,
        )

        if not len(arguments) >= 1:
            self.parser.print_help(sys.stderr)
            sys.exit(1)

        options: Namespace = self.parser.parse_args(arguments)

        getattr(self, arguments[0])(options)

    def hello(self, options) -> None:
        print(say_hello(options.name))


def main():
    Klickbrick(sys.argv[1:])


if __name__ == "__main__":
    main()
