# Demo image for unipay-uz: the library installed from source plus a small
# FastAPI app (examples/demo_app.py) that runs without real merchant credentials.
FROM python:3.12-slim

LABEL org.opencontainers.image.source="https://github.com/javlondevv/unipay-uz" \
      org.opencontainers.image.description="unipay-uz demo: offline checkout links for Payme, Click, Uzum and Paynet, plus the FastAPI webhook handlers" \
      org.opencontainers.image.licenses="MIT"

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

# Install the library from this checkout, then drop the sources so the app
# imports the installed package.
COPY pyproject.toml setup.cfg MANIFEST.in README.md LICENSE /tmp/src/
COPY unipay_uz /tmp/src/unipay_uz
RUN pip install "/tmp/src[fastapi]" "uvicorn>=0.30,<1" \
    && rm -rf /tmp/src

COPY examples ./examples

RUN useradd --create-home --uid 10001 --shell /usr/sbin/nologin unipay
USER unipay

EXPOSE 8000

CMD ["uvicorn", "examples.demo_app:app", "--host", "0.0.0.0", "--port", "8000"]
