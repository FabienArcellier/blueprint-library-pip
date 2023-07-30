# Building the blueprint

This blueprint is a python project template. It may need to be rebuilt regularly, especially to update the stack.

### 1. update the dependencies

```bash
poetry add --dev toml@latest
poetry add --dev sphinx@latest
poetry add --dev sphinx-rtd-theme@latest
```

### 2. generate documentation skeleton with sphinx

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
