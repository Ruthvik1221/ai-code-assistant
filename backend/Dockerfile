FROM python:3.10

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install openai

COPY . /app

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
