from django.db import models


class TimeStampedModel(models.Model):
    """ Time Stamped Model """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # 데이터베이스 등록 방지
    class Meta:
        abstract = True
