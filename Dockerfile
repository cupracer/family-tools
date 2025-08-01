FROM python:3.12-slim

ENV SECRET_KEY="dummy"

RUN useradd -u 999 -m -s /bin/bash -g users appuser

RUN mkdir -p /opt/family-tools
COPY . /opt/family-tools
RUN chown -R appuser: /opt/family-tools

USER appuser
WORKDIR /opt/family-tools

RUN pip install -r requirements.txt
RUN ./manage.py collectstatic

EXPOSE 8000

CMD ["/bin/sh", "/opt/family-tools/.docker/run.sh"]
