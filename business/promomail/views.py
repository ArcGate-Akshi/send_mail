from django.contrib import messages
from django.core.mail import send_mass_mail, send_mail
from django.http import HttpResponse
from django.shortcuts import render
from .models import Customer
from .models import Message
from .models import Delivery
from business import settings


# Create your views here.
def mail_list(request):
    try:
        if request.method == "POST":
            if request.POST.get('temp'):
                customer_count = Customer.objects.all().count()
                print(customer_count)
                print('inside try')
                print(request)

                # getting mail template to send
                mail_id = request.POST.get('temp')
                print(mail_id)
                mail_option = Message.objects.filter(m_id=mail_id).first()
                print(mail_option.text)

                # to get list of selected emails
                selected_mails = request.POST.getlist('mail_to_choice')
                print(selected_mails)

                # sending mail
                for i,s in enumerate(selected_mails):
                    to = selected_mails[i]
                    print(to)
                    subject = mail_option.subject
                    message = mail_option.text
                    from_email = settings.EMAIL_HOST_USER
                    print(subject)
                    print(message)
                    print(from_email)
                    print('before msg')
                    send_mail(subject, message, from_email, [to])
                    print('after')

                print('end of send mail')
                return render(request, 'done.html')
        else:
            emails = Customer.objects.values_list('email', flat=True)
            print(emails)
            return render(request, 'mailing_list.html',{'emails': emails})

    except Exception as e:
        print(e)
        return HttpResponse('except block')


def home(request):
    try:
        print("+++++++++++++++++++++++++++==")
        if request.method == 'POST':
            if request.POST.get('mail'):
                customer_count = Customer.objects.all().count()
                print(customer_count)
                print('inside try')
                print(request)
                mail_id = request.POST.get('mail')
                print(mail_id)
                # Message.m_id = mail_id
                mail_option = Message.objects.filter(m_id=mail_id).first()
                print(mail_option.text)

                # sending mails
                subject = mail_option.subject
                message = mail_option.text
                from_email = settings.EMAIL_HOST_USER

                messagess = [(subject, message, from_email, [User.email]) for User in Customer.objects.all()]
                send_mass_mail(messagess)
                print('end of send mail')
                return HttpResponse('sent mass mail')

        return render(request, 'home.html')
    except (TypeError, ValueError):
        print('except')
        return render(request, 'home.html')




