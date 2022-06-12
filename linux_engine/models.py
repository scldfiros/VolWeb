from django.db import models
from investigations.models import *

class PsTree(models.Model):
    investigation = models.ForeignKey(
            UploadInvestigation,
            on_delete=models.CASCADE,
            related_name="linux_pstree_investigation"
        )
    graph = models.JSONField(null = True)

class PsList(models.Model):
    investigation = models.ForeignKey(
            UploadInvestigation,
            on_delete=models.CASCADE,
            related_name="linux_pslist_investigation"
        )
    COMM = models.CharField(max_length = 255,null = True)
    PID = models.BigIntegerField(null = True)
    PPID = models.BigIntegerField(null = True)
