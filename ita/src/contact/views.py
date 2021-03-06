from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from .forms import contactForm

# Create your views here.
def contact(request):
    title = 'Contact'
    form = contactForm(request.POST or None)
    confirm_message = None

    if form.is_valid():
        # name = form.cleaned_data['name']
        # comment = form.cleaned_data['comment']
        # subject = 'Message from User '
        # message = '%s %s' %(name, comment)
        # emailFrom = form.cleaned_data['email']
        # emailTo = [settings.EMAIL_HOST_USER]
        # send_mail(subject, message, emailFrom, emailTo, fail_silently=False)
        title = "Thanks!"
        confirm_message = "Thank you. We will get back to you in a jiffy!"
        form = None

    context = {'title': title, 'form': form, 'confirm_message': confirm_message }
    template = 'contact.html'
    return render(request, template, context)
