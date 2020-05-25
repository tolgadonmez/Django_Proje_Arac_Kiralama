from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from car.models import Category, Comment, Reservation, Car
from home.models import UserProfile
from user.forms import UserUpdateForm, ProfileUpdateForm


def index(request):
    category = Category.objects.all()
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {'category': category,
               'profile': profile}
    return render(request, 'user_profile.html', context)


@login_required(login_url='/login')
def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Hesabınız Başarıya Güncellendi!')
            return redirect('/user')
    else:
        category = Category.objects.all()
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)
        context = {
            'category': category,
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, 'user_update.html', context)


@login_required(login_url='/login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Şifreniz Başarıyla Güncellendi !')
            return redirect('change_password')
        else:
            messages.warning(request, 'Lütfen Aşağıdaki Hatayı Düzeltin.<br>' + str(form.errors))
            return HttpResponseRedirect('/user/password')
    else:
        category = Category.objects.all()
        form = PasswordChangeForm(request.user)

        return render(request, 'change_password.html', {
            'form': form, 'category': category
        })


@login_required(login_url='/login')
def comments(request):
    category = Category.objects.all()
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    comments = Comment.objects.filter(user_id=current_user.id)
    context = {
        'category': category,
        'comments': comments,
        'profile' : profile
    }
    return render(request, 'user_comments.html', context)


@login_required(login_url='/login')
def deletecomment(request,id):
    Car.objects.get(pk=id)
    current_user = request.user
    Comment.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request, 'Yorum Silindi.')
    return HttpResponseRedirect('/user/comments')


@login_required(login_url='/login')
def reservations(request):
    category = Category.objects.all()
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    reservations = Reservation.objects.filter(user_id=current_user.id)
    context = {
        'category': category,
        'reservations': reservations,
        'profile': profile,

    }
    return render(request, 'user_reservations.html', context)


@login_required(login_url='/login')
def deletereservation(request,id):
    Car.objects.get(pk=id)
    current_user = request.user
    Reservation.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request, 'Rezervasyon Silindi.')
    return HttpResponseRedirect('/user/reservations')


@login_required(login_url='/login')
def newreservation(request, id):
    car = Car.objects.get(pk=id)
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    category = Category.objects.all()
    reservation = Reservation.objects.filter(user_id=current_user.id)
    context = {'category': category,
               'reservation': reservation,
               'profile': profile,
               'car': car,
               }
    return render(request, 'newreservation.html', context)



