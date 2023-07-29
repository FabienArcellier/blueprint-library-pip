# Building the blueprint

Ce blueprint est un template de projet python. Il peut necessiter d'être reconstruit régulièrement, notamment pour mettre à jour la stack.

### 1. update the dependencies

```bash
poetry add python-dotenv@latest

poetry add --dev alfred-cli@latest
poetry add --dev mypy@latest
poetry add --dev pytest@latest
```

