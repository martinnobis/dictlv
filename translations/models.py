# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class EnLv(models.Model):
    en = models.ForeignKey('English', models.CASCADE, blank=True, null=True)
    lv = models.ForeignKey('Latvian', models.CASCADE, blank=True, null=True)
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'en_lv'

    def __str__(self):
        return "%s = %s" % (self.en.txt, self.lv.txt)

class English(models.Model):
    id = models.BigAutoField(primary_key=True)
    txt = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'english'

    def __str__(self):
        return self.txt


class Latvian(models.Model):
    id = models.BigAutoField(primary_key=True)
    txt = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'latvian'

    def __str__(self):
        return self.txt
