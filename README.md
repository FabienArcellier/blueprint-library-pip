## Motivation

blueprint to implement a library in python. This library may be deployed on pip.

* code to share between several applications
* domain specific library
* ...

## Getting started

1. clone this repository

2. remove .git directory

3. use your library identifier as module name

    replace `mylib`, `mylib_tests` by your own identifier
    change `Makefile` and `setup.py`

## The latest version

You can find the latest version to ...

```bash
git clone ...
```

## Usage

You can run the application with the following command

```python
import mylib

mylib.hello_world()
```

## Developper guideline

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
make update_requirements
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

A short snippet describing the license (MIT, Apache, etc.)
