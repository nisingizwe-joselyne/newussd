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
        numb = text[:3]

        if text == '':
            response = 'CON welcome to  digital ikigega platform for farmers: \n'
            response += '1. Girls In Code \n'
            response += '2. SDF Program'
            # girls in code session
        elif text == '1':
            response = 'CON Welcome to Girls In Code '+str(len(level))+'\n'
            response += '1. Join the Program \n'
            response += '2. Get Activity \n'
            response += '3. Leave'

        elif text == '1*1':
            response = 'CON Enter you Name '+str(len(level))+' \n'
        elif numb == '1*1' and int(len(level))==3 and str(level[2]) in str(level):
            response = 'CON Enter your IDnumber \n'
        elif numb == '1*1' and int(len(level))==4 and str(level[3]) in str(level):
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
@csrf_exempt
def digitalapp (request):
    if request.method == 'POST':
        session_id = request.POST.get('sessionId')
        service_code = request.POST.get('serviceCode')
        phone_number = request.POST.get('phoneNumber')
        text = request.POST.get('text')
        level = text.split('*')
        response = ''
        numb = text[:3]
        if text == '':
            response = 'CON welcome to  digital ikigega platform for farmers: \n'
            response += '1. rice \n'
            response += '2. milk \n'
            response += '3.coffee \n'
            response += '4.Fruits \n'
            response += '5.beans'
            #  harvesting session
        elif text == '1':
            response = 'CON welcome to  digital ikigega platform for farmers '+str(len(level))+'\n'
            response += '1. Harvesting services \n'
            response += '2. financial service \n'
            response += '3. other services'
            # current harvesting session
        elif text == '1*1':
            response = 'CON  harvesting checking '+str(len(level))+': \n'
            response += '1.current total harvesting \n'
            response += '2.currently monthly harvesting \n'
            response += '3.other '
        elif numb == '1*1' and int(len(level))==3 and str(level[2]) in str(level):
            response = 'CON Enter farmers code or phone number '
        elif numb == '1*1' and int(len(level))==4 and str(level[3]) in str(level):
            response = 'CON your total  harvesting in 3 months is \n'
            response += '1.july:215kg \n'
            response += '2.august:260kg \n'
            response += '3.sept:60kg '
        #  financial session
        elif text == '1*2':
            response = 'CON Welcome to the financial services  \n'
            response += '1. direct loan \n'
            response += '2. pay loan \n'
            response += '3. how to get loan'
            # direct loan session
        elif text == '1*2*1':
            response = 'CON Enter farmers code or phone number '+str(len(level))+' \n'
        elif numb == '1*2*1' and int(len(level))==4 and str(level[3]) in str(level):
            response = 'CON you want to get : \n'
            response += '1.direct loan  of 2 months/allowed loan (20000rwf) \n'
            response += '2.direct loan of 4 months/allowed loan (40000rwf) \n'
            response += '3.dierect loan of 6 months/allowed loan (80000rwf) \n'
            response += '4.dierect loan of 12 months/allowed loan (120000rwf)\n'
        elif numb == '1*2*1' and int(len(level))==5 and str(level[4]) in str(level):
            response = 'CON Enter the money you want: \n'
        elif numb == '1*2*1' and int(len(level))==6 and str(level[5]) in str(level):
            response = 'CON  you have required to get 25000 rwf loan Enter mobile money pin code to confirm that will be paid in 2 months: \n'
        elif text == '1*2*2':
            response = 'CON Enter farmers code '+str(len(level))+' \n'
        elif numb == '1*2*2' and int(len(level))==4 and str(level[3]) in str(level):
            response = 'CON Enter the money you want pay: \n'   
        elif numb == '1*2*2' and int(len(level))==5 and str(level[4]) in str(level):
            response = 'CON Enter mobile-money pin to pay: \n'   
        elif numb == '1*2*2' and int(len(level))==6 and str(level[5]) in str(level):
            response = 'CON you have succesfully paid the loan thanks: \n'   
        elif text == '1*3':
            response = 'CON Other services: \n'
            response += '1.how to become our platform user \n'
            response += '2.how to get loan \n'
        elif text == '1*3*1':
            response = 'END how to use our platform: \n'
            response += 'in order to become the user you have to be a member of any registrated cooperative \n'
        elif text == '1*3*2':
            response = 'END you have to be a user of our platform atleast 4 month before getting the loan '
        else:
            response = 'END Invalid Choice'


            

        return HttpResponse(response)

    return HttpResponse('ikigega')