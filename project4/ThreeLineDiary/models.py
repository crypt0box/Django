from django.db import models
from django.utils import timezone


class Post(models.Model):
    """日記"""

    line_one = models.TextField('1つ目', max_length=50)
    line_two = models.TextField('2つ目', max_length=50)
    line_three = models.TextField('3つ目', max_length=50)
    created_at = models.DateTimeField('作成日', default=timezone.now)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.line_one[:10]
