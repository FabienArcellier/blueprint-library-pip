# Prepare the blueprint to use it as your project base

A library project that implements this template must be hosted on github. The publication of a new version of the library is triggered on github action when a tag is created.

1. change the project metadata into `./pyproject.toml`

```toml
name = "blueprint-library-pip"
description = "blueprint to implement a library in python to deploy on pypi"
authors = ["Fabien Arcellier <fabien.arcellier@gmail.com>"]
license = "MIT"
```

2. change the package name

* change package name from `src/lib` to desired name `src/my_custom_lib`

3. remove the markdown files relative to the blueprint

```bash
rm "prepare the blueprint.md" 
rm "maintain this blueprint.md"
```

4. modify the CI badget for github action in the readme

The github action badge must point to your repo instead of the blueprint for the badge to match your project.

```markdown
[![ci](https://github.com/{...}/actions/workflows/main.yml/badge.svg)](https://github.com/{...}/actions/workflows/main.yml)
```

5. modify section Run in gitpod in README.md

The ![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg) command should point to your repository instead of the blueprint one

```markdown
[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/...)
```


5. change the package declaration into `pyproject.toml`

```toml
packages = [{include = "my_custom_lib", from = "src"}]
```

5. configure the credential of pypi on github repository for github action

In this step, I should register the token of the pypi account. The token will be used by github action to publish the library. The configuration is done in github settings. The variable `TWINE_PASSWORD` should be created in Secrets and variables > Actions section.
```bash
TWINE_PASSWORD : pypi-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

6. import the project to readthedocs.org


7. publish the library on pypi

```bas
alfred publish
```
