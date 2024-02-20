import subprocess

from behave import *


@given("we have behave installed")
def step_impl(context):
    pass


@when('the user runs "ejskb hello"')
def step_impl(context):
    context.result = subprocess.run(
        ["poetry", "run", "ejskb", "hello"],
        capture_output=True,
        text=True,
    )
    print(context.result)


@then('the CLI prints "Hello, World!"')
def step_impl(context):
    print(context.result.stdout)
    assert context.result.stdout == "Hello, World!\n\n"
