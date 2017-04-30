# animation-bot
A simple wechat bot, with a scrapy crawler.

## configuration
```bash
export MONGO_URI="your mongodb uri"
```

## run bot
```bash
python bot.py
```

## crawl data
```bash
scrapy crawl imdb
```
## usage
start the bot, login with QR Code. Send message '/random' to this bot,
and it will reply a random animation character's name to you.