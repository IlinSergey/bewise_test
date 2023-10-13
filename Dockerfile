FROM python:3.10

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY config.py /app/
COPY database.py /app/
COPY main.py /app/
COPY my_types.py /app/
COPY service.py /app/

ENV DB=${DB}

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]