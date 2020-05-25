from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from car.models import Comment, CommentForm, Reservation, ReservationForm, Category, Car
from home.models import UserProfile


def index(request):
    return HttpResponse("Car Page")



def addcomment(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            current_user = request.user

            data = Comment()
            data.user_id = current_user.id
            data.car_id = id
            data.subject = form.cleaned_data['subject']
            data.comment = form.cleaned_data['comment']
            data.rate = form.cleaned_data['rate']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, 'Yorumunuz Başarı İle Gönderilmiştir. Teşekkürler ')

            return HttpResponseRedirect(url)

    messages.warning(request, 'Yorumunuz Kaydedilmedi. Lütfen Kontrol Ediniz ')
    return HttpResponseRedirect(url)



def addreservation(request, id):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            current_user = request.user
            #profile = UserProfile.objects.get(user_id=current_user.id)
            #category = Category.objects.all()
            #reservations = Reservation.objects.filter(user_id=current_user.id)
            data = Reservation()
            data.user_id = current_user.id
            data.car_id = id
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.phone = form.cleaned_data['phone']
            data.location = form.cleaned_data['location']
            data.address = form.cleaned_data['address']
            data.days = form.cleaned_data['days']
            data.checkin = form.cleaned_data['checkin']
            data.checkout = form.cleaned_data['checkout']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, 'Rezervasyon Kaydınız Başarıyla Alınmıştır.Onay için Bekleyiniz. ')
            return HttpResponseRedirect('/user/reservations/')

    messages.warning(request, 'Rezervasyon Kaydınız Yapılmadı. Lütfen Bilgilerinizi Kontrol Ediniz!! ')
    return HttpResponseRedirect('/user')
