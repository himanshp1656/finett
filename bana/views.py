from django.http import JsonResponse
from django.shortcuts import render , HttpResponse , redirect , HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login , logout 
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.views import View
import stripe
from django.http import HttpResponseBadRequest
import razorpay
stripe.api_key=settings.STRIPE_SECRET_KEY
#from payTm import Checksum
#from PayTm import Checksum
#from payTm import checksum
#from paytm import Checksum

#from payTm import Checksum
# from django.contrib.auth.forms import UserCreationForm
# from django.db import models
MERCHANT_KEY = 'none'



# Create your views here.
def home(request):
    return render(request, 'index.html')
def stripegateway(request):
    return render(request, 'stripe.html')
def free_wifi(request):
    return render(request, 'free_wifi.html')
def own_a_router(request):
    return render(request, 'own_a_router.html')
def subscription_plans(request):
    return render(request, 'subscription_plans.html')
def askinggateway(request):
    return render(request, 'askinggateway.html')

    
def handlesignup(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        fname=request.POST.get('fname')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        if pass1!=pass2:
            messages.error(request,'password and confirm password should be same')
            return HttpResponseRedirect('/home/')
        else:
            myuser=User.objects.create_user(username, email, pass1)               
            myuser.first_name=fname 
            myuser.save()
            messages.success(request, 'account is created succefully')
            return HttpResponseRedirect('/home/')
           
def handlelogin(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    print(username,password)
    User=authenticate(request,username=username , password=password)

    if User is not None:
        login(request, User)
        username=User.get_username
        messages.success(request, 'Loggedin succefully')
        return HttpResponseRedirect('/home/')
    else:
        messages.error(request,'wrong password or email')
        return HttpResponseRedirect('/home/')
    
        
    
def handlesignout(request):
    logout(request)
    messages.success(request, 'Loggedout succefully')
    return HttpResponseRedirect('/home/')
    return render(request, 'index.html')
#paytm integration
def paytmgateway(request):
    id=User.email
    param_dict = {

            'MID': 'VoGqSa6977837046',
            'ORDER_ID': User.username,
            'TXN_AMOUNT': '1',
            'CUST_ID': User.email,
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL':'http://127.0.0.1:8000/handlerequest/',
    }
    return render(request, 'paytm.html', {'param_dict': param_dict})
 #   return HttpResponse('redirecting you to the payment page please do not refresh the page........')
@csrf_exempt
def handlerequest(request):
    return HttpResponse('done done done')
    # form = request.POST
    # response_dict = {}
    # for i in form.keys():
    #     response_dict[i] = form[i]
    #     if i == 'CHECKSUMHASH':
    #         checksum = form[i]

    # verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    # if verify:
    #     if response_dict['RESPCODE'] == '01':
    #         print('order successful')
    #     else:
    #         print('order was not successful because' + response_dict['RESPMSG'])
    # return render(request, 'shop/paymentstatus.html', {'response': response_dict})

    
razorpay_client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
def createcheckoutsessionview(request):  
   currency = 'INR'
   amount=20000
   razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                       currency=currency,
                                                       payment_capture='1'))
 
   razorpay_order_id = razorpay_order['id']
   callback_url = 'paymenthandler/'
 
    # we need to pass these details to frontend.
   context = {}
   context['razorpay_order_id'] = razorpay_order_id
   context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
   context['razorpay_amount'] = amount
   context['currency'] = currency
   context['callback_url'] = callback_url
 
   return render(request, 'index.html', context=context)
@csrf_exempt
def paymenthandler(request):
 
    # only accept POST request.
    if request.method == "POST":
        try:
           
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
 
            # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)
            if result is not None:
                amount = 20000  # Rs. 200
                try:
 
                    # capture the payemt
                    razorpay_client.payment.capture(payment_id, amount)
 
                    # render success page on successful caputre of payment
                    return render(request, 'paymentsuccess.html')
                except:
 
                    # if there is an error while capturing payment.
                    return render(request, 'paymentfail.html')
            else:
 
                # if signature verification fails.
                return render(request, 'paymentfail.html')
        except:
 
            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
       # if other than POST request is made.
        return HttpResponseBadRequest()

