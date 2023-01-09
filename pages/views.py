from django.views.generic.edit import CreateView
from django.shortcuts import render

from django.contrib.auth.decorators import login_required




import razorpay
from .models import UserInfo

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def course_detail(request):
    return render(request, 'courses.html')

@login_required
def razorpaycheck(request):
    if request.method == "POST":
        order_amount = 699
        order_currency = "INR"
        client = razorpay.Client(auth=('rzp_live_Wk8Xsfot2Nw2zA', 'LmyqZxDxN92tWDKlzWqsx306'))
        payment = client.order.create({'amount': order_amount, 'currency': order_currency, 'payment_capture': "1"})
    return render(request, 'checkout.html')

@login_required
def razorpaycheckmonth(request):
    if request.method == "POST":
        order_amount = 299
        order_currency = "INR"
        client = razorpay.Client(auth=('rzp_live_Wk8Xsfot2Nw2zA', 'LmyqZxDxN92tWDKlzWqsx306'))
        payment = client.order.create({'amount': order_amount, 'currency': order_currency, 'payment_capture': "1"})
    return render(request, 'checkoutmonth.html')


class UserInterest(CreateView):
    template_name = 'join.html'
    model = UserInfo
    fields = ['student_name', 'phone', 'mail',]

def success(request):
    return render(request, 'success.html')