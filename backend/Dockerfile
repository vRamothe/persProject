FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc libpq-dev curl \
    libpango-1.0-0 libpangoft2-1.0-0 libpangocairo-1.0-0 \
    libcairo2 libglib2.0-0 libfontconfig1 libgdk-pixbuf-2.0-0 \
    fonts-liberation fonts-stix \
    texlive-latex-base texlive-latex-recommended texlive-fonts-recommended \
    dvisvgm && \
    rm -rf /var/lib/apt/lists/* && \
    fc-cache -f

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN DJANGO_SETTINGS_MODULE=config.settings.production \
    SECRET_KEY=build-placeholder-not-real \
    DATABASE_URL=sqlite:////tmp/dummy.db \
    python manage.py collectstatic --noinput

RUN addgroup --system django && adduser --system --ingroup django django
RUN chown -R django:django /app
RUN mkdir -p /home/django/.cache/fontconfig && chown -R django:django /home/django

USER django

EXPOSE 8000

CMD ["/bin/sh", "entrypoint.sh"]
