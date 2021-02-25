from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from django.urls import reverse


def login_view(request):
    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     # return HttpResponse('{} & {}'.format(username, password))
    #     user = authenticate(request, username=username, password=password)
    #     if user is None:
    #         raise Http404('نام کاربری یا گذرواژه نادرست است')
    #     else:
    #         login(request, user)
    #         return HttpResponse('wellcome user!!!')
    # else:
    #     if request.user.is_authenticated:
    #         return HttpResponse('شما قبلا وارد شدید')
    #     else:
    #          return render(request, 'accounts/login.html', {})
    next_url = request.GET.get('next')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Successful login
            login(request, user)
            redirect_url = next_url if next_url else reverse('index')
            return HttpResponseRedirect(redirect_url)
        else:
            # undefined user or wrong password
            context = {
                'username': username,
                'error': 'کاربری با این مشخصات یافت نشد'
            }
    else:
        context = {}
    return render(request, 'accounts/login.html', context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
