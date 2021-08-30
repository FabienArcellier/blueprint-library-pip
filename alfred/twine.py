import alfred


@alfred.command("twine", help="publish the package on pypi")
def twine():
    alfred.invoke_command("build")

    twine = alfred.sh("twine")
    alfred.run(twine, ['upload', 'dist/*'])
