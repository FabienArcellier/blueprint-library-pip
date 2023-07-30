# Maintain this blueprint

This blueprint is a python project template. It may need to be rebuilt regularly, especially to update the stack dependencies.

### 1. rebase the blueprint

This blueprint is based on [blueprint-python3](https://github.com/FabienArcellier/blueprint-python3). You have to update it by doing a git rebase of the `master` branch.

```bash
git pull --rebase base master
```

The git remote endpoint `base` is declared on [blueprint-python3](https://github.com/FabienArcellier/blueprint-python3)

### 2. update the dependencies

```bash
poetry add --dev toml@latest
```

