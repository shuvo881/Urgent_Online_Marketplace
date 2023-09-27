from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from user_profile.forms import Form_profile_edit


def user_profile(request, username):
    user = User.objects.get(username=username)
    print(user)
    return render(request, 'user_profile/user_profile.html', {
        'user': user
    })


@login_required(login_url='signin')
def _profile_edit(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        form = Form_profile_edit(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile edit successful...')
            print(user)
            return redirect('user_profile', username=request.user)
        else:
            messages.error(request, 'error')

    form = Form_profile_edit(instance=user)
    return render(request, 'user_profile/profile_edit.html', {
        'form': form
    })


@login_required(login_url='signin')
def user_delete(request):
    user = User.objects.get(username=request.user)
    try:
        user.delete()
        messages.success(request, 'User delete successful')
        return redirect('browser')
    except EnvironmentError as ex:
        messages.error(request, ex)
    return render('user_profile', username=request.user)
