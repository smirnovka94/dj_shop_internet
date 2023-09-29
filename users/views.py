from django.conf import settings
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView
from users.forms import UserForm, VerificationForm
from users.models import User
import random
import string
import copy


random_key = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
_key = copy.copy(random_key)


class LoginView(BaseLoginView):
    template_name = 'users/login.html'

class LogoutView(BaseLogoutView):
    pass

class RegisterView(CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:verification')
    template_name = 'users/register.html'

    def form_valid(self, form):
        self.object = form.save()
        verification_link = "http://127.0.0.1:8000/users/register/users/verification/"

        send_mail(
            subject='Поздравляем с регистрацией',
            message= f'Для завершения регистрации перейдите по ссылке: {verification_link} \n'
                     f'Для прохождения верификации скопируйте ключ: {_key}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.object.email]
        )
        return super().form_valid(form)


class UserVerificationView(FormView):
    form_class = VerificationForm
    success_url = reverse_lazy('main:home')
    template_name = 'users/user_verification.html'

    def post(self, request, *args, **kwargs):
        key_post = request.POST.get('key_post')
        if _key == key_post:
            return redirect ('users:login')
        else:
            return render(request, 'users/user_verification.html', {'error_message': 'Ключи не совпадают'})

def delete_user(email):
    User.objects.get(email=User.email).delete()
    return redirect('home')

def delete(request):

    if request.method == "POST":
        email = request.POST.get('email')
        print(email)
        # КАКТО УДАЛИТЬ ЭКЗЕМПЛЯР КЛАССА ПРОБУЮ ЧЕРЕЗ delete_user() НО НЕ ПОЛУЧАЕТСЯ
        # delete_user(email)
        # ПРИ УСПЕШНОМ УЛАДЕННИИ ПЕРЕЙТИ НА "users:verification"
    return render(request, 'users/user_detail.html')

