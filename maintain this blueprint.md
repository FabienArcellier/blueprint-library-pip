# Maintain this blueprint

This blueprint is a python project template. It may need to be rebuilt regularly, especially to update the stack dependencies.

### 1. rebase the blueprint from parent

This blueprint is based on [blueprint-python3](https://github.com/FabienArcellier/blueprint-python3). You have to update it by doing a git rebase of the `master` branch.

```bash
git pull --rebase base master
```

The git remote endpoint `base` is declared on [blueprint-python3](https://github.com/FabienArcellier/blueprint-python3)

### 2. update the dependencies

```bash
poetry add --dev toml@latest
poetry add --dev sphinx@latest
poetry add --dev sphinx-rtd-theme@latest
```

## Rebuild the blueprint from scratch

### 2. add the dependencies

```bash
poetry add --dev toml@latest
poetry add --dev sphinx@latest
poetry add --dev sphinx-rtd-theme@latest
```

### 3. generate documentation skeleton with sphinx

1. generate the skeleton

```bash
cd ./docs
sphinx-quickstart .

> Separate source and build directories (y/n) [n]: n
> ...
```

2. remove the file `./docs/make.bat`

3. configure the theme sphinx-rtd-theme in `./docs/conf.py`

```python
html_theme = 'sphinx_rtd_theme'
```

4. configure `./docs/index.rst`

```rst
Blueprint-library-pip documentation
===================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   api
```

### 4. reconfigure gitpod for this repository in README.md : Run in gitpod

```markdown
[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/FabienArcellier/blueprint-library-pip)
```
