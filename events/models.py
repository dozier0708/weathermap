from django.db import models

class EventType(models.Model):
    event_type = models.CharField(max_length=255)
    event_type_slug = models.SlugField()
    def __unicode__(self):
        return self.event_type

class WxEvent(models.Model):
    event_type = models.ForeignKey(EventType)
    event_start_date = models.DateTimeField('date occurred')
    event_description = models.TextField()
    event_headline = models.CharField(max_length=200)
    event_location = models.CharField(max_length=200)
    def __unicode__(self):
        return self.event_type
