"""Functions for retrieving objects and translations from the database."""

from translations.models import English, Latvian
from django.core.exceptions import ObjectDoesNotExist

special_chars = {
    'ē': 'e',
    'ā': 'a',
    'ī': 'i',
    'ū': 'u',
    'č': 'c',
    'ģ': 'g',
    'ķ': 'k',
    'ļ': 'l',
    'ņ': 'n',
    'š': 's',
    'ž': 'z'
}


def retrieve(fn):
    """Return None instead of an exception when an object doesn't exist.
    
    Otherwise an exception is thrown.
    """
    def modified_fn(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except (AssertionError, ObjectDoesNotExist) as e:
            return None

    return modified_fn


@retrieve
def get_object_from_text(model, text):
    return model.objects.get(txt__iexact=text)


@retrieve
def get_objects_from_ids(model, ids):
    return model.objects.filter(pk__in=ids)


# TODO: How to refactor this to remove the if statement? There is probably a
# way to refactor all of these methods into a concise efficient query.
@retrieve
def get_intersect_ids_from_id(model, id):
    """Search for the id in the models intersect table.
    
    Returns a list of ids from the other column which correspond to its
    translations. Can only work with English and Latvian models.
    """
    if model is English:
        return Latvian.objects.filter(enlv__en_id=id)
    return English.objects.filter(enlv__lv_id=id)


@retrieve
def get_alt_candidate(text):
    return Latvian.objects.filter(alt=text)


def get_translations(from_lang, to_lang, text):
    """Return a list of translation strings."""
    from_object = get_object_from_text(from_lang, text)
    if from_object:
        from_id = from_object.id
        to_ids = get_intersect_ids_from_id(from_lang, from_id)
        to_objs = get_objects_from_ids(to_lang, to_ids)
        return [to_obj.txt for to_obj in to_objs]
    return []


def translation_exists(lang, text):
    """Check if a translation exists.

    Retrns a boolean.
    """
    obj = get_object_from_text(lang, text)
    if obj:
        if get_intersect_ids_from_id(lang, obj.id):
            return True
    return False


def get_similar_latvian_words(text):
    """Search the Latvian table for words with incorrect special characters.

    Returns a list of potential candidates with proper spelling.
    """
    modified_text = text.translate(text.maketrans(special_chars))
    candidate_objs = Latvian.objects.filter(alt=modified_text)
    return [candidate.txt for candidate in candidate_objs]
