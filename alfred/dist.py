import alfred


@alfred.command('dist', help='build distribution packages')
def dist():
    """
    build distribution packages

    >>> $ alfred dist
    """
    alfred.run('poetry build')
