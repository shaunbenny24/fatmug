from django.db import models

# Create your models here.
from django.db import models

import re
import re

class Video(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='videos/')
    subtitles = models.TextField(blank=True, null=True)

    def search_subtitles(self, query):
        if not self.subtitles:
            return []

        results = []
        # Updated regex pattern to handle potential subtitle variations
        pattern = re.compile(r"(\d{2}:\d{2}:\d{2},\d{3}) --> .*?\n(.*?)(?=\n\n|\Z)", re.DOTALL)
        for match in pattern.finditer(self.subtitles):
            timestamp = match.group(1)
            subtitle_text = match.group(2).strip()  # Remove leading/trailing whitespace
            if query.lower() in subtitle_text.lower():
                results.append((timestamp, subtitle_text))
        return results


class Subtitle(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    language = models.CharField(max_length=20)
    text = models.TextField()

    def __str__(self):
        return f'{self.video.title} - {self.language}'
