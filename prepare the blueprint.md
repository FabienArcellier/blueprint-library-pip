# Prepare the blueprint to use it as your project base

1. change the project metadata into `./pyproject.toml`

```toml
name = "blueprint-python3"
description = "blueprint to implement a python application"
authors = ["Fabien Arcellier <fabien.arcellier@gmail.com>"]
license = "MIT"
```

2. configure the .env file

copy the `.env.example` file into `.env` and change the value of the environment variables to adapt the project behavior between development and production.

3. remove the markdown files relative to the blueprint

```bash
rm "prepare the blueprint.md" 
rm "maintain this blueprint.md"
```

4. modify section Run in gitpod in README.md

The ![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg) command should point to your repository instead of the blueprint one

```markdown
[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/...)
```
