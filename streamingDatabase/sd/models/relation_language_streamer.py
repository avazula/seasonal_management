from .person import Person
from .language import Language
from django.db import models


class RelationLanguageStreamer(models.Model):
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
