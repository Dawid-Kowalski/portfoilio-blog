from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('',views.main_page,name='main_page'),
    path('cv',views.cv_page,name='cv_page'),
    path('skills',views.skills_page,name='skills_page'),
    path('FAQ',views.FAQ_page,name='FAQ_page'),
    path('find-me-on',views.find_me_on_page,name='find_me_on_page'),
    path('contact', views.contactView, name='contact'),
    path('success', views.successView, name='success'),
]