from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from car.models import Comment, CommentForm


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


