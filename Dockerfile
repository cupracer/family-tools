FROM python:3-slim

EXPOSE 8000

RUN useradd -u 999 -m -s /bin/bash -g users appuser

RUN mkdir -p /opt/family-tools
RUN chown appuser: /opt/family-tools

USER appuser

COPY . /opt/family-tools
WORKDIR /opt/family-tools

RUN pip install -r requirements.txt
RUN ./manage.py collectstatic

CMD ["/bin/sh", "/opt/family-tools/.docker/run.sh"]
