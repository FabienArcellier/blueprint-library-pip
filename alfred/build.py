import alfred


@alfred.command("build", help="build the package into ./build")
def build():
    python = alfred.sh("python")
    alfred.run(python, ["setup.py", "bdist", "sdist"])
