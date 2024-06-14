FROM python:3.12.4

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED 1

WORKDIR /dbmovies

COPY requirements.txt /dbmovies/
RUN pip install -r requirements.txt

COPY . /dbmovies/

EXPOSE 8000

ENTRYPOINT ["bash", "/dbmovies/django.sh"]