FROM python:3-slim

EXPOSE 8000

RUN useradd -u 999 -m -s /bin/bash -g users appuser

RUN mkdir -p /opt/family-tools
COPY . /opt/family-tools
RUN chown -R appuser: /opt/family-tools

USER appuser
WORKDIR /opt/family-tools

RUN pip install -r requirements.txt
RUN SECRET_KEY="dummy-secret" ./manage.py collectstatic

CMD ["/bin/sh", "/opt/family-tools/.docker/run.sh"]
