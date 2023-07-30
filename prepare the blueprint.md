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
