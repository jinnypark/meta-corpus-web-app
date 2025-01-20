"""
Models for the ***** app.
"""
from django.db import models

class Score(models.Model):
    file = models.TextField()
    title = models.TextField()
    composer = models.TextField()
    format = models.TextField()
    text = models.TextField()
    factsheet = models.JSONField()

# factsheet format
# {
#   'tonic': pitch (A, B, C) | ? (ambiguous),
#   'time_signature': '4/4'
#   'structure': ['A', 'B', 'A', 'C'],
#   'chords': ['V'],
#   'sections': [
#       {
#           'name': 'A, interlude',
#           'progression': 'I-IV-V-I'
#       }
#   ]
# }