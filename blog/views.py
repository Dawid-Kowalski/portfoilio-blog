from django.shortcuts import render, redirect
from .models import Documments, Skill, FAQ, Portal
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm

def main_page(request):
    return render(request,'blog/main-page.html')

def cv_page(request):
    documents_objects = Documments.objects.all()
    return render(request,'blog/cv-page.html',{'documents':documents_objects})

def skills_page(request):
    skills_description_objects = Skill.objects.all().order_by('name_en')
    return render(request,'blog/skills-page.html',{'skills':skills_description_objects})

def FAQ_page(request):
    FAQ_objects = FAQ.objects.all()
    return render(request,'blog/FAQ-page.html',{'FAQS':FAQ_objects})

def find_me_on_page(request):
    Portal_objects = Portal.objects.all()
    return render(request,'blog/find-me-on-page.html',{'portals':Portal_objects})

def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('blog:success')
    return render(request, "blog/contact-page.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')
