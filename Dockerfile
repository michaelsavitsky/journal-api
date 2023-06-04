FROM python:3.8

WORKDIR /code

ENV FASTAPI_APP=main.py
ENV FASTAPI_RUN_HOST=0.0.0.0

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8000

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]