from django.db import models

class MultipleFileUpload(models.Model):
    files = models.FileField(upload_to='uploads/', null=True, blank=True)
    title = models.CharField(max_length=255,null=True, blank=True)
    content = models.TextField(default="",null=True, blank=True)
    position_index = models.JSONField(default=dict,null=True, blank=True)

    def __str__(self):
        return str(self.files)
    
    class Meta:
        app_label = 'home'