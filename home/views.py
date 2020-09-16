from django.shortcuts import render
import africastalking
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

username = "nesjoselyne@gmail.com"
api_key = "7d5ec7e665579ee7ef1a3a71927f74123d0542960de776089cc89b28b4977804"
# Create your views here.

def welcome(request):
    return render(request,'popschools.html') 
def about(request):
    return render(request,'about.html')
def pricing(request):
    return render(request,'pricing.html')
    africastalking.initialize(username,api_key)

@csrf_exempt
def ussdapp(request):
    if request.method == 'POST':
        # mandatory
        session_id = request.POST.get('sessionId')
        service_code = request.POST.get('serviceCode')
        phone_number = request.POST.get('phoneNumber')
        text = request.POST.get('text')
        level = text.split('*')
        response = ''

        if text == '':
            response = 'CON Welcome to Ida USSD app \n'
            response += '1. Girls In Code \n'
            response += '2. SDF Program'
            # girls in code session
        elif text == '1':
            response = 'CON Welcome to Girls In Code '+str(len(level))+'\n'
            response += '1. Join the Program \n'
            response += '2. Get Activity \n'
            response += '3. Leave'

        elif text == '1*1':
            response = 'CON Enter you Name '+str(len(level))+'\n'
        elif  int(len(level))==3 and str(level[2]) in str(level):
            response = 'CON Enter your IDnumber \n'
         elif  int(len(level))==4 and str(level[3]) in str(level):
            response = 'CON Enter your pincode \n'
        elif text == '1*2':
            response = 'CON Enter your PINCode \n'
        elif text == '1*3':
            response = 'CON Enter your Address \n'
         
        elif text == '2':
            response = 'CON Welcome to Girls In Code \n'
            response += '1. Join the Program \n'
            response += '2. Get Activity \n'
            response += '3. Leave'
        else:
            response = 'END Invalid Choice'


            

        return HttpResponse(response)

    return HttpResponse('Welcome')
