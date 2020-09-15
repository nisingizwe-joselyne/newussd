from django.shortcuts import render
import africastalking
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

username = "jojo"
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
       session_id = request.POST.get("sessionID")
       service_code = request.POST.get("servicecode")
       phone_number = request.POST.get("phoneNumber")
       text = request.POST.get("text")
       level = text.split("*")
       response = ""
       if text == '':
          response = "CON welcome to ida technology ussd app \n"
          response += "1. girls in code \n"
          response += "2. sdf program \n"
          response += "3. other"

       elif text =='1':
          response = "CON welcome to girls in code program"
          response += "1. join the program\n"
          response += "2. get activity\n"
          response += "3. leave"

       elif text == '1*1':
          response = "CON Enter your name \n"
       elif text == '1*2':
          response = "CON Enter your name \n"
       elif text == '1*3':
          response = "CON Enter your name \n"
      
       elif text =='2':
          response = "CON welcome to girls in code program \n"
          response += "1. join the program \n"
          response += "2. get \n"
          response += "3. leave \n"
       else:
           response = "END invalid choice "
       return HttpResponse(response)
    return HttpResponse('welcome')