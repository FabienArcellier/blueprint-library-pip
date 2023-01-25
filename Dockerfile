FROM python:3.10

RUN pip install poetry
RUN mkdir -p /app/src

COPY . /app

WORKDIR /app

RUN poetry config virtualenvs.create false \
  && poetry install --without dev

CMD ["python", "src/app/main.py"]
