import os

import alfred

ROOT_DIR = os.path.realpath(os.path.join(__file__, "..", ".."))


@alfred.command("run", help="execute the application")
def run():
    """
    construit l'image docker pour l'application

    >>> $ alfred docker:build
    """
    python = alfred.sh("python", "python should be present")
    os.chdir(ROOT_DIR)
    alfred.run(python, ['src/app/main.py'])
