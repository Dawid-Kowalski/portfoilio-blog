from .models import Author_Description

def author_description(request):
    description_object = Author_Description.objects.all()[:1].values()
    description = [element for element in description_object]
    return {'description' : description[0]}