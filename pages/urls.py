from django.urls import path
from .views import home, about, course_detail, UserInterest, razorpaycheck,success, razorpaycheckmonth

app_name = 'pages'
urlpatterns = [
    path('', home, name='home' ),
    path('about/', about, name='about'),
    path('courses/',course_detail, name='courses' ),
    path('interested/', UserInterest.as_view(), name='join' ),
    path('checkout-onetime/', razorpaycheck, name='checkout'),
    path('checkout-monthly/', razorpaycheckmonth, name='checkout-monthly'),
    path('coding/', UserInterest.as_view(), name='coding'),

 path('checkout-monthly/success/', success, name='checkout-monthly-success'),
    path('checkout-onetime/success/', success, name='checkout-onetime-success'),

]