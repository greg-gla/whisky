from django.shortcuts import render
from django.views.generic import View


# Create your views here.
class IndexView(View):
    def get(self, request, **kwargs):
        return render(request, 'pages/index.html')


def register(request):
    # registered = False
    # if request.method == 'POST':
    #     user_form = UserForm(request.POST)
    #     profile_form = UserProfileForm(request.POST)
	#
    #     if user_form.is_valid() and profile_form.is_valid():
    #         user = user_form.save(commit=False)
	#
    #         user.set_password(user.password)
    #         user.save()
	#
    #         profile = profile_form.save(commit=False)
    #         profile.user = user
	#
    #         if 'picture' in request.FILES:
    #             profile.picture = request.FILES['picture']
	#
    #         profile.save()
    #         registered = True
    #     else:
    #         print(user_form.errors, profile_form.errors)
    # else:
    #     user_form = UserForm()
    #     profile_form = UserProfileForm()

    return render(request,'pages/registration.html')
                  # context={'user_form': user_form,
                  #          'profile_form': profile_form,
                  #          'registered': registered})


def user_login(request):
    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     user = authenticate(username=username, password=password)
	#
    #     if user:
    #         if user.is_active:
    #             login(request, user)
    #             return redirect(reverse('rango:index'))
    #         else:
    #             return HttpResponse("Your Rango account is disabled.")
    #     else:
    #         print(f"Invalid login details: {username}, {password}")
    #         return HttpResponse("Invalid login details supplied.")
    # else:
        return render(request, 'pages/login.html')


# @login_required
# def user_logout(request):
#     logout(request)
#     return redirect(reverse('rango:index'))
