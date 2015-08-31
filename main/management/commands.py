from django.core.management.base import BaseCommand

class NewsCommand(BaseCommand):

    args = 'asdadfdgwdfdsdsakd'
    help = "help me"

    def handle(self,*args,**kwargs):
        print("Help me!")