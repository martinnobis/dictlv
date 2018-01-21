"""Utility functions for retrieving objects and translations from the database
"""
from translations.models import English, Latvian, Enlv
from django.core.exceptions import ObjectDoesNotExist

def retrieve(fn):
    def modified_fn(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except(AssertionError, ObjectDoesNotExist) as e:
            return None
    return modified_fn

@retrieve
def get_object_from_text(model, text):
    return model.objects.get(txt=text)

@retrieve
def get_objects_from_ids(model, ids):
    return model.objects.filter(pk__in=ids)

@retrieve
def get_intersects_from_id(model, id):
    if model is English:
        return Enlv.objects.filter(en_id=id)
    return Enlv.objects.filter(lv_id=id)

def latvian_trans_from_english(text):
    en_id = get_object_from_text(English, text).id
    lv_ids = [inter.lv_id for inter in get_intersects_from_id(English, en_id)]
    lv_objs = get_objects_from_ids(Latvian, lv_ids)
    return [lv.txt for lv in lv_objs]

def english_trans_from_latvian(text):
    lv_id = get_object_from_text(Latvian, text).id
    en_ids = [inter.en_id for inter in get_intersects_from_id(Latvian, lv_id)]
    en_objs = get_objects_from_ids(English, en_ids)
    return [en.txt for en in en_objs]
