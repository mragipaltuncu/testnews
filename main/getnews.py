import requests
from lxml import html, etree
from lxml.cssselect import CSSSelector


def get_news():
    content = requests.get("http://www.radikal.com.tr/d/rss/RssYazar_438.xml")
    dom_tree = etree.fromstring(content.content)
    item_selector = CSSSelector('channel > item')

    return item_selector(dom_tree)

def news():
    news = [item.find('title').text for item in get_news()]
    return news

