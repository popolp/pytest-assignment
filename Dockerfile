FROM python:3.10.1

COPY . /pytest-assignment
WORKDIR /pytest-assignment

RUN pip install -r requirements.txt
CMD ["python", "-m", "pytest", "-q"] 