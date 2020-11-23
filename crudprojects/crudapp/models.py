from django.db import models

class USR_TIMETBL_INF(models.Model):
        USRID = models.CharField(max_length=200)
        USRNAME = models.CharField(max_length=400)
        GRPID = models.CharField(max_length=200)
        GRPNAME = models.CharField(max_length=200)
        GRPBUNRUI = models.CharField(max_length=200)
        USR_TIMEINF = models.CharField(max_length=1000)
        REGDATE = models.DateTimeField('date published')

        def __str__(self):
                return self.USR_TIMEINF