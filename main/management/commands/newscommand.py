from django.core.management.base import BaseCommand
from main.getnews import news
from main.models import ArticleTitle

class Command(BaseCommand):

    args = 'asdadfdgwdfdsdsakd'
    help = "help me"

    def handle(self,*args,**kwargs):
        list_news = news()
        for item in list_news:
            article = ArticleTitle()
            article.title = item
            article.save()
