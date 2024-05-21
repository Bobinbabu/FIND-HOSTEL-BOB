from django.urls import path
from myapp1 import views

urlpatterns = [
    path('', views.display),
    path('uprofile',views.uprofile,),
    path('hprofile', views.hprofile),
    path('display',views.display),
    path('user', views.userreg,name='user'),
    path('usignin', views.usignin),
    path('hostel', views.hostelreg,name='hostel1'),
    path('hsignin', views.hsignin),
    path('reg', views.uandhreg),
    path('uregistered',views.uregistered),
    path('ulogged',views.ulogged),
    path('ulogout',views.ulogout),
    path('hregistered',views.hregistered),
    path('hlogged',views.hlogged),
    path('hlogout',views.hlogout),
]