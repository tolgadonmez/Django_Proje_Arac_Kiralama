import json


from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from car.models import Car, Category, Images, Comment, Reservation
from home.forms import SearchForm, SignUpForm
from home.models import Setting, ContactFormu, ContactFormMessage, UserProfile, FAQ


def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Car.objects.all()    #sliderda kaçtane araba gözükeceği
    category = Category.objects.all()
    cars = Car.objects.all()       #contentte kaçtane araba gözükeceği

    if request.user.is_authenticated:
        current_user = request.user

        profile = UserProfile.objects.get(user_id=current_user.id)
        context = {'setting': setting,
                    'category': category,
                    'page': 'home',
                    'sliderdata': sliderdata,
                    'cars': cars,
                    'profile': profile
                }
    else:
        context = {'setting': setting,
                   'category': category,
                   'page': 'home',
                   'sliderdata': sliderdata,
                   'cars': cars,
                   }

    return render(request, 'index.html', context)


def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    if request.user.is_authenticated:
        current_user = request.user
        profile = UserProfile.objects.get(user_id=current_user.id)
        context = {'setting': setting,
                'category': category,
               'profile': profile
                }
    else:
        context = {'setting': setting,
                   'category': category,
                   }

    return render(request, 'hakkimizda.html', context)


def referanslar(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    if request.user.is_authenticated:
        current_user = request.user
        profile = UserProfile.objects.get(user_id=current_user.id)
        context = {'setting': setting,
               'category': category,
               'profile': profile}

    else:
        context = {'setting': setting,
                   'category': category,
                   }
    return render(request, 'referanslarimiz.html', context)


def iletisim(request):
    if request.method == 'POST':
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, 'Mesajınız Başarıyla Gönderilmiştir.Teşekkür Ederiz.')
            return HttpResponseRedirect('/iletisim')

    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    form = ContactFormu()
    if request.user.is_authenticated:
        current_user = request.user
        profile = UserProfile.objects.get(user_id=current_user.id)
        context = {'setting': setting,
                   'form': form,
                   'category': category,
                   'profile': profile}
    else:
        context = {'setting': setting,
                   'form': form,
                   'category': category,
                   }
    return render(request, 'iletisim.html', context)


def category_cars(request, id, slug):
    cars = Car.objects.filter(category_id=id)
    category = Category.objects.all()
    categorydata = Category.objects.get(pk=id)
    if request.user.is_authenticated:
        current_user = request.user
        profile = UserProfile.objects.get(user_id=current_user.id)
        context = {'cars': cars,
               'category': category,
               'slug': slug,
               'categorydata': categorydata,
               'profile': profile
                   }
    else:
        context = {'cars': cars,
                   'category': category,
                   'slug': slug,
                   'categorydata': categorydata,
                   }
    return render(request, 'cars.html', context)


def car_detail(request, id, slug):
    category = Category.objects.all()
    car = Car.objects.get(pk=id)
    images = Images.objects.filter(car_id=id)
    comments = Comment.objects.filter(car_id=id, status='True')
    reservations = Reservation.objects.filter(car_id=id)
    if request.user.is_authenticated:
        current_user = request.user
        profile = UserProfile.objects.get(user_id=current_user.id)
        context = {'car': car,
                   'category': category,
                   'images': images,
                   'comments': comments,
                   'reservations': reservations,
                   'profile': profile}
    else:
        context = {'car': car,
                   'category': category,
                   'images': images,
                   'comments': comments,
                   'reservations': reservations,
                   }

    return render(request, 'car_detail.html', context)


def car_search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            category = Category.objects.all()


            query = form.cleaned_data['query']
            catid = form.cleaned_data['catid']

            if catid == 0:
                cars = Car.objects.filter(title__icontains=query)
            else:
                cars = Car.objects.filter(title__icontains=query, category_id=catid)
            if request.user.is_authenticated:
                current_user = request.user
                profile = UserProfile.objects.get(user_id=current_user.id)
                context = {'cars': cars,
                           'category': category,
                           'profile': profile}
            else:
                context = {'cars': cars,
                           'category': category,
                           }

            return render(request, 'cars_search.html', context)

    return HttpResponseRedirect('/')


def car_search_auto(request):

    if request.is_ajax():

        q = request.GET.get('term', '')
        car = Car.objects.filter(title__icontains=q)
        results = []
        for rs in car:
            car_json = {}
            car_json = rs.title
            results.append(car_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, 'Kullanıcı adı veya şifre yanlış! ')
            return HttpResponseRedirect('/login')

    category = Category.objects.all()
    if request.user.is_authenticated:
        current_user = request.user
        profile = UserProfile.objects.get(user_id=current_user.id)
        context = {'category': category,
                   'profile': profile}
    else:
        context = {'category': category,
                   }

    return render(request, 'login.html', context)


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            current_user = request.user
            data = UserProfile()
            data.user_id = current_user.id
            data.image = "images/users/user.png"
            data.save()
            messages.success(request, 'Sitemize başarılı bir şekilde kayıt oldunuz.  ')
            return HttpResponseRedirect('/')

    form = SignUpForm()

    category = Category.objects.all()
    if request.user.is_authenticated:
        current_user = request.user
        profile = UserProfile.objects.get(user_id=current_user.id)
        context = {'category': category,
                   'form': form,
                   'profile': profile}
    else:
        context = {'category': category,
                   'form': form,
                   }

    return render(request, 'signup.html', context)


def faq(request):
    category = Category.objects.all()
    #menu = Menu.objects.all()
    faq = FAQ.objects.all()
    if request.user.is_authenticated:
        current_user = request.user
        profile = UserProfile.objects.get(user_id=current_user.id)
        context = {'category': category,
               'faq': faq,
               'profile': profile
                }
    else:
        context = {'category': category,
                   'faq': faq,
                   }
    return render(request, 'faq.html', context)
