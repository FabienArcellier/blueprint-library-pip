import alfred

@alfred.command("run", help="execute the application")
def run():
    """
    execute the application

    >>> $ alfred run
    """
    python = alfred.sh("python", "python should be present")
    alfred.run(python, ['src/app/main.py'])
