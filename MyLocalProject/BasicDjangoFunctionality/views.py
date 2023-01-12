from django.shortcuts import render, HttpResponseRedirect, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'BasicDjangoFunctionality/index.html')

def GETform(request):
    return render(request, 'BasicDjangoFunctionality/GETform.html')

def GETinfoDisplay(request):
    fname = request.GET['fname']
    mailid = request.GET['mailid']
    password = request.GET['password']
    return render(request, 'BasicDjangoFunctionality/GETinfoDisplay.html', {'FullName':fname, 'EmailAddress':mailid, 'Password':password})

def POSTform(request):
    return render(request, 'BasicDjangoFunctionality/POSTform.html')

def POSTinfoDisplay(request):
    val1 = int(request.POST.get("value1"))
    val2 = int(request.POST.get("value2"))
    sum = val1 + val2
    return render(request, "BasicDjangoFunctionality/POSTinfoDisplay.html", {'output': sum})