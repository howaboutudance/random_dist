FROM python:3.9-rc as builder

WORKDIR /build
COPY Pipfile ./
RUN python -m venv /opt/venv
ENV PATH="/opt/venv:$PATH"


COPY ./random_dist/. ./random_dist/
COPY ./setup.py ./
COPY ./requirements.txt ./

RUN pip install --install-option="--prefix=/opt/venv" -r requirements.txt
RUN pip install --install-option="--prefix=/opt/venv" .


FROM python:3.9-rc-alpine3.12 as deploy

WORKDIR /app
COPY --from=builder /build/requirements.txt ./
COPY --from=builder /opt/venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"
ENV VIRTUAL_ENV="/opt/venv"
RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "-m" , "random_dist"]
