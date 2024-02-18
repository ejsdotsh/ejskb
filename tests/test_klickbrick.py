#!/usr/bin/env python3


import unittest

from subprocess import getoutput


prg = "./ejskb/klickbrick.py"


class Testing(unittest.TestCase):
    def test_usage(self):
        """usage"""
        for flag in ["", "-h", "--help"]:
            out = getoutput(f"{prg} {flag}")
            assert out.lower().startswith("usage")

    def test_say_hello(self):
        self.assertEqual(getoutput(f"{prg} hello"), "Hello, World!")
        self.assertEqual(
            getoutput(f"{prg} hello --name strawberries"), "Hello, Strawberries!"
        )
        self.assertEqual(getoutput(f"{prg} hello --name 13"), "Hello, 13!")


if __name__ == "__main__":
    unittest.main()
