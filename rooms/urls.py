from django.urls import path

from . import views


app_name = 'rooms'

urlpatterns = [
    path('', views.lobby, name='lobby'),
    path('waiting_room/', views.waiting_room, name='waiting_room'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    # path('setcookie/<str:cookie>/', views.store_cookie, name='setcookie'),
    # path('getcookie/', views.get_cookie, name='getcookie'),
]