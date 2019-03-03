## Motivation

blueprint to implement a library in python. This library may be deployed on pip.

* code to share between several applications
* domain specific library
* compliant with different python version
* ...

[![Build Status](https://travis-ci.org/FabienArcellier/blueprint-library-pip.svg?branch=master)](https://travis-ci.org/FabienArcellier/blueprint-library-pip)

## Getting started

1. clone this repository

2. remove .git directory

3. use your library identifier as module name

    * replace `mylib`, `mylib_tests` by your own identifier
    * change `.coveragerc`, `Makefile`, `setup.py`, `tox.ini`

## The latest version

You can find the latest version to ...

```bash
git clone https://github.com/FabienArcellier/blueprint-library-pip.git
```

## Usage

You can run the application with the following command

```python
import mylib

mylib.hello_world()
```

## Developper guideline

```
$ make
coverage                       output the code coverage in htmlcov/index.html
freeze_requirements            update the project dependencies based on setup.py declaration
help                           provides cli help for this makefile (default)
install_requirements_dev       install pip requirements for development
install_requirements           install pip requirements based on requirements.txt
lint                           run pylint
tests                          run automatic tests
tox                            run tests described in tox.ini on multiple python environments
venv                           build a virtual env for python 3 in ./venv
```

### Install development environment

Use make to instanciate a python virtual environment in ./venv and install the
python dependencies.

```bash
make install_requirements_dev
```

### Install production environment

```bash
make install_requirements
```

### Initiate or update the library requirements

If you want to initiate or update all the requirements `install_requires` declared in `setup.py`
and freeze a new requirements.txt, use this command

```bash
make freeze_requirements
```

### Activate the python environment

When you setup the requirements, a `venv` directory on python 3 is created.
To activate the venv, you have to execute :

```bash
make venv
source venv/bin/activate
```

### Run the linter and the unit tests

Before commit or send a pull request, you have to execute `pylint` to check the syntax
of your code and run the unit tests to validate the behavior.

```bash
make lint
make tests
```

## Contributors

* Fabien Arcellier

## License

MIT License

Copyright (c) 2018 Fabien Arcellier

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
