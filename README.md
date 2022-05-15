## Motivation

blueprint to implement a library in python. This library may be deployed on pip.

* code to share between several applications
* domain specific library
* compliant with different python version
* ...

[![ci](https://github.com/FabienArcellier/blueprint-library-pip/actions/workflows/ci.yml/badge.svg)](https://github.com/FabienArcellier/blueprint-library-pip/actions/workflows/ci.yml)

## Getting started

1. clone this repository

2. remove .git directory

3. use your library identifier as module name

    * replace `src/mylib` by your own identifier
    * change `Pipfile`, `setup.cfg`

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
pipenv shell
```

### Install development environment

Use make to instanciate a python virtual environment in ./venv and install the
python dependencies.

```bash
pipenv install --dev
```

### Install production environment

```bash
pipenv install
```

### Initiate or update the library requirements

If you want to initiate or update all the requirements `install_requires` declared in `setup.py`
and freeze a new `Pipfile.lock`, use this command

```bash
pipenv update
```

### Run the linter and the unit tests

Before commit or send a pull request, you have to execute the continuous integration process.

```bash
alfred ci
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
