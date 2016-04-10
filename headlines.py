from flask import Flask
from flask import render_template
import feedparser

app = Flask(__name__)

RSS_FEED = {"bbc": "http://feeds.bbci.co.uk/news/rss.xml",
			"cnn": "http://rss.cnn.com/rss/edition.rss",
			"fox": "http://feeds.foxnews.com/foxnews/latest",
			"iol": "http://www.iol.co.za/cmlink/1.640"
			}

@app.route('/')
@app.route("/<publication>")
def get_news(publication="bbc"):
	return get_news(publication)

def get_news(publication):
	feed = feedparser.parse(RSS_FEED[publication])
	first_article = feed['entries'][0]
	return render_template('index.html', first_article=first_article)


if __name__ == "__main__":
	app.run(debug=True)