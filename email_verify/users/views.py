from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import tokens, get_user_model
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string

from .forms import UserRegistrationForm




def bread(path: str) -> list:
    p = []
    paths = path.split('/')
    paths = [path for path in paths if path != '']

    for i in range(len(paths)):
        p.append('/'.join(paths[:i+1]) + '/')

    return p


def send_activation_email(reciver_emails, username, domain, uid, token):
    str_msg = ''
    subject = 'Confirm you email'
    sender = 'saeidtempmail@gmail.com'
    html_msg = render_to_string('users/verify.html', {
                'username': username,
                'domain': domain,
                'uid': uid,
                'token': token
    })

    send_mail(subject, str_msg, sender, reciver_emails, html_message=html_msg)


def home(request):
    return render(request, 'users/home.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            # deactive user
            user.is_active = False
            form.save()

            # create userid and token
            current_site = get_current_site(request)
            domain = current_site.domain
            user_id = urlsafe_base64_encode(force_bytes(user.pk))
            token = tokens.default_token_generator.make_token(user)
            # Send activation email
            send_activation_email([email], user.username, domain, user_id, token)


            return redirect('users:home')
        else:
            print(f'Error, user didnt created')
    else:
        form = UserRegistrationForm()
        
    paths = bread(get_current_site(request).domain + request.path)
    return render(request, 'users/register.html', {'form': form, 'paths':paths})


def activate(request, uid, token):
    User = get_user_model()
    try:
        user_id = urlsafe_base64_decode(uid)
        user = User.objects.get(pk=user_id)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
        
    if user is not None and tokens.default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'users/confirm.html')
    else:
        return HttpResponse('<h1>Confiramtion Failed!!!</h1>')
    