FROM python:3.6

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt -i https://pypi.douban.com/simple/

COPY . /app

CMD ["python", "bot.py"]
