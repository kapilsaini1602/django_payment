from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
import hashlib
from django.shortcuts import render
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt
from . import Checksm
from django.conf import settings
#######additonal
from django.shortcuts import render, HttpResponse, redirect, \
    get_object_or_404, reverse
from django.contrib import messages
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from decimal import Decimal

#######additonal
MISD = 'JU78@Z_IBrWJcA30'


# Create your views here.
def homep(request):
    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('password')
        ammount = request.POST.get('ammount')
        obj = OrderDetails.objects.create(username=username, password=password, ammount=ammount)
        obj.save()

        param_dict = {
            'MID': 'yRKdgL21634551259403',
            'ORDER_ID': str(obj.id),
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL': 'http://127.0.0.1:8000/paytm_integ/handlepayment/',
            'CUST_ID': username,
            'TXN_AMOUNT': str(ammount),
        }
        param_dict['CHECKSUMHASH'] = Checksm.generate_checksum(param_dict, 'JU78@Z_IBrWJcA30')
        return render(request, 'paytm.html', {'param_dict': param_dict})
    return render(request, 'index.html')


@csrf_exempt
def handlerequest(request):
    form = request.POST
    print(form['ORDERID'])
    response_dict = {}
    # checksum = ''
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksm.verify_checksum(response_dict, MISD, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'paymentstatus.html', {'response': response_dict})
