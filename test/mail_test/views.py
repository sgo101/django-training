from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import tokens, get_user_model
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes
from django.utils.html import strip_tags
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string

from .forms import UserRegistrationForm


# https://medium.com/@shafikshaon/user-registration-with-email-verification-in-django-8aeff5ce498d
def home(request):
    return render(request, 'mail_test/home.html')


def send_activation_email(reciver_emails, username, domain, uid, token):
    # how to send email with attachment # https://blog.mailtrap.io/django-send-email/
    

    subject = 'Confirm your email'
    # content = 'This is the content of the email'
    sender = 'saeidtempmail@gmail.com'
    # send_mail(subject, content, sender, recivers)  # function to send email
    # get a template and render it (basically the html page)
    html_msg =  render_to_string('mail_test/verfiy_msg.html', {
        'username': username, 
        'domain': domain,
        'uid': uid, 
        'token': token
    })  
    # if you are not strip the message it will send as html page and render like html page on browser
    message = strip_tags(html_msg)  # remove any things like tags <>
    send_mail(subject, html_msg, sender, reciver_emails)  # send eamil
    print(html_msg)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            username = form.cleaned_data.get('username')
            email_to = form.cleaned_data.get('email')
            form.save()

            current_site = get_current_site(request)  # get current site name
            domain = current_site.domain
            user_id = urlsafe_base64_encode(force_bytes(user.pk))
            token = tokens.default_token_generator.make_token(user)
            send_activation_email([email_to], username, domain, user_id, token)

            return redirect('mail:user201')

    else:
        form = UserRegistrationForm()

    return render(request, 'mail_test/register.html', {'form': form})


def user201(request):
    return render(request, 'mail_test/user201.html', )


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and tokens.default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'mail_test/confirmed.html')
        import time
        time.sleep(5)
        return redirect('mail:login')
    else:
        return HttpResponse('Activation link is invalid!')

