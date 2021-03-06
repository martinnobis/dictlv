"""My docstring."""

from django.db import models


class English(models.Model):
    """Contains a list of English words."""

    id = models.BigAutoField(primary_key=True)
    txt = models.TextField(unique=True, blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'english'

    def __str__(self):
        return self.txt


class Latvian(models.Model):
    """Contains a list of Latvian words.
    
    The alt column contains the spelling of
    a word without any special characters, used to support the feature of
    searching for a Latvian word when they are with missing or incorrect.
    """

    id = models.BigAutoField(primary_key=True)
    txt = models.TextField(unique=True, blank=False, null=False)
    alt = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'latvian'

    def __str__(self):
        return self.txt


class Enlv(models.Model):
    """Contains the ids for the translations between English and Latvian.

    Each row contains a foreignkey to a Latvian and English model id from their
    respective tables. Many-to-many and one-to-many translations are supported.
    """

    id = models.BigAutoField(primary_key=True)
    en = models.ForeignKey(
        English, models.CASCADE, blank=False, null=False, default=1)
    lv = models.ForeignKey(
        Latvian, models.CASCADE, blank=False, null=False, default=1)

    class Meta:
        managed = False
        db_table = 'enlv'

    def __str__(self):
        return "%s = %s" % (self.en.txt, self.lv.txt)
