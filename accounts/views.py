from django.http import request, HttpResponse
from django.contrib.auth.views import LoginView
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views.generic import CreateView, TemplateView
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode


from accounts.tokens import account_activation_token
from .forms import SignupForm
from .models import User


class Login(LoginView):
    template_name = "accounts/login.html"

    def get_success_url(self):
        if self.request.user.is_superuser:
            return reverse_lazy("sales:plans_list")
        else:
            return reverse_lazy("sales:plans_list")


# registration and user activation
class RegisterCreateView(CreateView):
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        return redirect("register-pending")

    form_class = SignupForm
    template_name = "accounts/register_form.html"


class RegisterPendingView(TemplateView):
    template_name = "accounts/register_done.html"


class ForgetPassword(TemplateView):
    template_name = "accounts/forget.html"


class RegisterCompleteView(TemplateView):
    template_name = "accounts/register_complete.html"


def activate(req, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect("register-complete")
    else:
        return HttpResponse("فعالسازی اکانت ناموفق بود.")
