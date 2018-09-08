FROM python:3.6-alpine

RUN pip3 install falcon
RUN pip3 install gunicorn

ENV MI_VARIABLE=sorpresa

EXPOSE 5000
COPY . /app

WORKDIR /app
CMD ["gunicorn", "-b", "0.0.0.0:5000", "-w", "4", "api:demo"]

