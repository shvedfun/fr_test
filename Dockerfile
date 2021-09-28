FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN git clone https://github.com/shvedfun/fr_test.git /drf_src


WORKDIR /drf_src

RUN ls .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

VOLUME /drf_src

EXPOSE 8080

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000
# CMD ["%%CMD%%"]