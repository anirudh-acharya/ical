from django.db import models

class Event(models.Model):
    uid = models.IntegerField(default=0)
    summary = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return "%s, %s, %s, %s" % (
                self.summary,
                self.location,
                self.start_date,
                self.end_date
                )
