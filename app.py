from flask import Flask
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def get_article():
    url = requests.get("https://en.wikipedia.org/wiki/Special:random")
    soup = BeautifulSoup(url.content)
    topic = soup.find(class_="firstHeading").text
    #new_url = "https://en.wikipedia.org/wiki/" + topic
    return {"Topic": topic}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')