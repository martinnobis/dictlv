from translations.models import English, Latvian, Enlv

def get_latvian_from_text(text):
    return Latvian.objects.get(txt=text)

def get_latvian_from_id(id):
    return Latvian.objects.get(id=id)

def get_english_from_text(text):
    return English.objects.get(txt=text)

def get_english_from_id(id):
    return English.objects.get(id=id)

def get_intersect_from_english_id(id):
    return Enlv.objects.get(en_id=id)

def get_intersect_from_latvian_id(id):
    return Enlv.objects.get(lv_id=id)
