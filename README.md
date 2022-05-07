## blueprint-python3

[![ci](https://github.com/FabienArcellier/blueprint-python3/actions/workflows/main.yml/badge.svg)](https://github.com/FabienArcellier//blueprint-python3/actions/workflows/main.yml)


blueprint to implement a simple spike with python3

* test python code
* use jupyter notebook with python dependencies
* ...

The implementation is compatible with python 3

## Getting started

1. clone this repository

2. remove .git directory

## The latest version

You can find the latest version to ...

```bash
git clone https://github.com/FabienArcellier/blueprint-python3.git
```

## Usage

You can run the application with the following command

```bash
python main.py
```

## Developper guideline

### Add a dependency

Write the dependency in ``setup.py``. As it's the distribution standard for pypi,
I prefer to keep ``setup.py`` as single source of truth.

I encourage avoiding using instruction as ``pipenv install requests`` to register
a new library. You would have to write your dependency in both ``setup.py`` and ``Pipfile``.

### Install development environment

Use make to instanciate a python virtual environment in ./venv and install the
python dependencies.

```bash
pipenv install --dev
```

### Update release dependencies

Use make to instanciate a python virtual environment in ./venv and freeze
dependencies version on requirement.txt.

```bash
pipenv update
```

### Activate the python environment

When you setup the requirements, a `venv` directory on python 3 is created.
To activate the venv, you have to execute :

```bash
pipenv shell
```

### Run the continuous integration process

Before commit or send a pull request, you have to execute `pylint` to check the syntax
of your code and run the unit tests to validate the behavior.

```bash
$ pipenv shell
$ alfred ci
```

## Contributors

* Fabien Arcellier

## License

MIT License

Copyright (c) 2018-2022 Fabien Arcellier

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
