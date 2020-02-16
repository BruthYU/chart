from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
# Create your views here.
def index(request):
    if request.method == "POST":
        body = request.POST.get("body")
        if body == "sick":
            return redirect('detail')
    return render(request, 'frontPage/index.html')

def detail(request):

    if request.method == "POST":
        temp = request.POST.get("temp")
        ge   = request.POST.get("ge")
        situation = request.POST.get("situation")
        return HttpResponse(str(temp)+'\n'+str(ge)+'\n'+str(situation))
    return render(request, 'frontPage/detail.html')



def login(request):
    if request.method == "POST":
        number = request.POST.get('number')
        name = request.POST.get('name')

        if number and name:
            pass
            return redirect('index')
           #how to verify will be written later
           #return redirect('/index/')
    return render(request, 'frontPage/login.html')





