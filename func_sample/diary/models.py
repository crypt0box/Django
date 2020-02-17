from django.db import models
from django.utils import timezone   # djangoではdatetime.nowのかわりに、timazone.nowで日付/時刻を取得する


class Day(models.Model):
    title = models.CharField('タイトル', max_length=200)
    text = models.TextField('本文')
    date = models.DateTimeField('日付', default=timezone.now)
