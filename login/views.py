"""
A one-step (user signs up and is immediately active and logged in)
workflow.

"""

from django.contrib.auth import authenticate, get_user_model, login

from registration import signals
from registration.backends.simple.views import RegistrationView

from login.models import RegistrationForm

User = get_user_model()


class RegistrationView(RegistrationView):
    """
    Registration via the simplest possible process: a user supplies a
    username, email address and password (the bare minimum for a
    useful account), and is immediately signed up and logged in).

    """

    def register(self, form):
        # new_user = form.save(self.request)
        new_user = self.save(self.request)
        if not new_user:
            return RegistrationForm()
        new_user = authenticate(
            username=getattr(new_user, User.USERNAME_FIELD),
            password=form.cleaned_data['password1']
        )
        login(self.request, new_user)
        signals.user_registered.send(sender=self.__class__,
                                     user=new_user,
                                     request=self.request)
        return new_user

    def get_success_url(self, user):
        return '/'

    def save(self, request):
        form = RegistrationForm(self.request.POST)
        print form.errors
        if form.is_valid():
            print form.cleaned_data
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email'],
            )
            return user
        else:
            return False
