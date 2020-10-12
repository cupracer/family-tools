FROM python:3-slim

EXPOSE 8000

RUN mkdir -p /opt/family-tools
COPY . /opt/family-tools

CMD ["/opt/family-tools/manage.py", "runserver", "0.0.0.0:8000"]
