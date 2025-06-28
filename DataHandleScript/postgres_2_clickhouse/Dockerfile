FROM python:3.8-alpine

WORKDIR /app/
COPY ./pyproject.toml /app/
COPY ./*.py /app/


RUN MAIN_VERSION=$(cat /etc/alpine-release | cut -d '.' -f 0-2) \
        && mv /etc/apk/repositories /etc/apk/repositories-bak \
        && { echo "https://mirrors.aliyun.com/alpine/v${MAIN_VERSION}/main"; \
        echo "https://mirrors.aliyun.com/alpine/v${MAIN_VERSION}/community"; } >> /etc/apk/repositories \
        && apk add --update --no-cache tzdata gcc build-base libffi-dev postgresql-dev curl && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
        && mkdir ~/.pip \
        && printf '[global]\nindex-url=https://mirrors.aliyun.com/pypi/simple/' > ~/.pip/pip.conf \
        && python3.8 -m pip install --upgrade pip \
        && curl -o poetry-install.py -SL https://install.python-poetry.org \
        && python3.8 -u poetry-install.py \
        && rm poetry-install.py \
        && export PATH="/root/.local/bin:$PATH" \
        && poetry config virtualenvs.create false --local \
        && poetry install --no-root 

CMD python3 -u main.py