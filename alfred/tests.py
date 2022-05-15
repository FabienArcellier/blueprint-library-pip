import os

import alfred
import click

ROOT_DIR = os.path.realpath(os.path.join(__file__, "..", ".."))


@alfred.command("tests", help="workflow to execute all automatic tests")
def tests():
    """
    workflow to execute all automatic tests

    >>> $ alfred tests
    """
    alfred.invoke_command('tests:units')


@alfred.command("tests:units", help="execute unit tests")
def tests__units():
    """
    execute unit tests with unittests

    >>> $ alfred tests:units
    """
    python = alfred.sh("python")
    os.chdir(ROOT_DIR)
    alfred.run(python, ['-m', 'unittest', 'discover', 'tests/units'])

