FROM python:3.11.8-alpine
WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFRED 1

RUN apk update && \
    apk add postgresql-dev gcc python3-dev musl-dev zlib-dev jpeg-dev && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . /usr/src/app/

# manage.py 파일이 있는 디렉터리로 이동
WORKDIR /usr/src/app/  # 이동할 디렉터리를 재지정합니다.

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
