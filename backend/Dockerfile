FROM python

WORKDIR /backend/

COPY requirements.txt requirements.txt

RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
