ARG IRONBANK_REGISTRY=registry1.dso.mil
ARG IRONBANK_PYTHON_IMAGE=ironbank/opensource/python/python39
ARG IRONBANK_PYTHON_TAG=v3.9.7

FROM $IRONBANK_REGISTRY/$IRONBANK_PYTHON_IMAGE:$IRONBANK_PYTHON_TAG as python_base

# For layer stability, and build cache optimization, do the Python libraries independent of the app itself
ENV PATH="/home/python/.local/bin:$PATH"
COPY --chown=python:python requirements.txt /home/python/requirements.txt

RUN pip3 install --no-cache-dir -r /home/python/requirements.txt

# Copy app
COPY --chown=python:python src /home/python/app
WORKDIR /home/python/app


FROM python_base as python_test_libs

COPY --chown=python:python requirements-testing.txt /home/python/
RUN pip3 install --no-cache-dir -r /home/python/requirements-testing.txt

# SSSC has requested this step to run at container build time to support the pipeline
FROM python_test_libs as python_tests

RUN python3 -m pytest -s --cov-report=term --junitxml=/tmp/junit.xml --cov-report=xml:/tmp/coverage.xml --cov -vv && \
    sed -i -e "s,/home/python/app,src,g" /tmp/coverage.xml && sed -i -e "s,\"tests,\"src.tests,g" /tmp/junit.xml


FROM python_base as python_runtime
ENV GUNICORN_CMD_ARGS="--bind=0.0.0.0 --access-logfile='-'"
EXPOSE 8000
CMD ["gunicorn", "tctap:app"]
