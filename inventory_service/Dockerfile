FROM python:3.12
LABEL maintainer="arman ashraf"
WORKDIR /code
RUN apt-get update && apt-get install -y \
    build-essential \
    protobuf-compiler \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*
RUN pip install poetry
# RUN poetry config virtualenvs.create false \
#     && poetry install --no-interaction --no-root
COPY . /code/
RUN poetry config virtualenvs.create false
RUN poetry install 
EXPOSE 8000
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000","--reload"]

 