from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from car.models import Comment, CommentForm, Reservation, ReservationForm


def index(request):
    return HttpResponse("Car Page")


@login_required(login_url='/login')
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
            messages.success(request, "Yorumunuz Başarı İle Gönderilmiştir. Teşekkürler ")

            return HttpResponseRedirect(url)

    messages.warning(request, "Yorumunuz Kaydedilmedi. Lütfen Kontrol Ediniz ")
    return HttpResponseRedirect(url)


@login_required(login_url='/login')
def addreservation(request, id, ):
    url = request.META.get('HTTP_REFERER')

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            current_user = request.user

            data = Reservation()

            data.user_id = current_user.id
            data.car_id = id
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.phone = form.cleaned_data['phone']
            data.address = form.cleaned_data['address']
            data.days = form.cleaned_data['days']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Rezervasyon Kaydınız Başarıyla Alınmıştır.Onay için Bekleyiniz. ")

            return HttpResponseRedirect(url)

    messages.warning(request, "Rezervasyon Kaydınız Yapılmadı. Lütfen Bilgilerinizi Kontrol Ediniz!! ")
    return HttpResponseRedirect(url)
