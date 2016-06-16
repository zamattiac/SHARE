from django.core.management.base import BaseCommand

from share.monitor import ShareMonitor


class Command(BaseCommand):

    def handle(self, *args, **options):
        from project.celery import app
        ShareMonitor(app).listen()
