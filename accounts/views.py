from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages, auth
from django.template.context_processors import csrf
from accounts.forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(email=request.POST.get('email'),
                                     password=request.POST.get('password'))

            if user is not None:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")
                return redirect(reverse('profile'))
            else:
                form.add_error(None, "Your email or password was not recognised")

    else:
        form = UserLoginForm()

    args = {'form': form}
    args.update(csrf(request))
    return render(request, 'login.html', args)



@login_required(login_url='/login/')
def profile(request):
    return render(request, 'profile.html')



def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    # return render(request, 'index.html')
    return redirect('/')