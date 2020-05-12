from django.db import models
from django.conf import settings

class Author_Description(models.Model):
    title = models.CharField(max_length=100)
    description_de = models.TextField(max_length=500)
    description_en = models.TextField(max_length=500)
    image = models.ImageField(upload_to ='media/')
    objects = models.Manager()

    def __str__(self):
        return self.title

class Documments(models.Model):
    name_de = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    date = models.DateField()
    image = models.ImageField(upload_to='media/')
    description_de = models.TextField(max_length=500)
    description_en = models.TextField(max_length=500)
    objects = models.Manager()

    def __str__(self):
        return self.name_en

class Skill_description(models.Model):
    description_de = models.TextField(max_length=300)
    description_en = models.TextField(max_length=300)

    def __str__(self):
        return self.description_en

class Skill(models.Model):
    name_de = models.TextField(max_length=100)
    name_en = models.TextField(max_length=100)
    rating = models.TextField(max_length=10)
    skill_description = models.ManyToManyField(Skill_description,related_name='skill_description')

    def __str__(self):
        return self.name_en

class FAQ(models.Model):
    FAQ_name = models.TextField(max_length=50)
    FAQ_de_text = models.TextField(max_length=300)
    FAQ_en_text = models.TextField(max_length=300)
    FAQ_de_answer = models.TextField(max_length=300)
    FAQ_en_answer = models.TextField(max_length=300)

    def __str__(self):
        return self.FAQ_name

class Portal(models.Model):
    portal_name = models.TextField(max_length=50)
    image = models.ImageField(upload_to='media/')
    profile_url = models.TextField(max_length=50)
    description_de = models.TextField(max_length=500)
    description_en = models.TextField(max_length=500)

    def __str__(self):
        return self.portal_name