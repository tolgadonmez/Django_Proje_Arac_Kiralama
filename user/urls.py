from django.urls import path

from . import views

urlpatterns = [
    # ex: /home/
    path('', views.index, name='index'),
    path('update/', views.user_update, name='user_update'),
    path('password/', views.change_password, name='change_password'),
    path('comments/', views.comments, name='comments'),
    path('reservations/', views.reservations, name='reservations'),
    path('deletecomment/<int:id>', views.deletecomment, name='deletecomment'),
    path('deletereservation/<int:id>', views.deletereservation, name='deletereservation')




    # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),

]
