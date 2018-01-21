"""Utility functions for retrieving objects and translations from the database.
"""
from translations.models import English, Latvian, Enlv
from django.core.exceptions import ObjectDoesNotExist

def retrieve(fn):
    """Querying the database for non-existant object throws an exception. This
    function serves can be used as a decorator to instead return None for
    when the database is queried for objects which don't exist.
    """
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

# TODO: How to refactor this to remove the if statement? There is probably a 
# way to refactor all of these methods into a concise efficient query.
@retrieve
def get_intersect_ids_from_id(model, id):
    """Searches for the id in the models intersect table and returns a list of
    ids from the other column which correspond to its translations. Can only
    work with English and Latvian models.
    """
    if model is English:
        return Latvian.objects.filter(enlv__en_id=id)
    return English.objects.filter(enlv__lv_id=id)

def get_translation(from_lang, to_lang, text):
    """Returns a list of translation strings.
    """
    from_id = get_object_from_text(from_lang, text).id
    to_ids = get_intersect_ids_from_id(from_lang, from_id)
    to_objs = get_objects_from_ids(to_lang, to_ids)
    return [to_obj.txt for to_obj in to_objs]
