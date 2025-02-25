from django.shortcuts import render
from .models import Survey_Data

def Indexpageview(request):
    return render(request, "myapp/index.html")

def InsertData(request):
    pid = request.POST.get('pid')  # सुरक्षित रूप से डेटा प्राप्त करें
    if Survey_Data.objects.filter(Initial_ID=pid).exists():  # PID पहले से मौजूद है
        return render(request, "myapp/error.html")  # Error Page पर भेजें
    else:
        request.session['pid'] = pid  # सत्र (session) में PID सेव करें
        newuser = Survey_Data.objects.create(Initial_ID=pid)  # नया यूज़र बनाएँ
        request.session['user_id'] = newuser.id  # यूज़र ID को session में सेव करें
        return render(request, "myapp/age.html")

def InsertAge(request):
    age = request.POST.get('age')
    user_id = request.session.get('user_id')  # Session से user_id प्राप्त करें
    age_range = list(range(18, 66))  #  18 से 65 तक की सही लिस्ट

    if user_id:
        user = Survey_Data.objects.get(id=user_id)
        user.Age = age
        user.save()  # डेटा अपडेट करें
        return render(request, "myapp/gender.html", {'age_range': age_range})
    else:
        return render(request, "myapp/error.html", {'age_range': age_range})  # अगर user_id नहीं मिली तो error दिखाएँ
def InsertGender(request):
    gender = request.POST.get('gender')
    user_id = request.session.get('user_id')

    if user_id:
        user = Survey_Data.objects.get(id=user_id)
        user.Gender = gender
        user.save()
        return render(request, "myapp/open_end.html")
    else:
        return render(request, "myapp/error.html")

def InsertOpen_End(request):
    open_end = request.POST.get('open_end')
    user_id = request.session.get('user_id')

    if user_id:
        user = Survey_Data.objects.get(id=user_id)
        user.Open_End = open_end
        user.save()
        
        # केवल user_id को हटाएँ, पूरा session flush न करें
        del request.session['user_id']  

        return render(request, "myapp/complete.html")
    else:
        return render(request, "myapp/error.html")

#  Error Page View
def ErrorPage(request):
    return render(request, "myapp/error.html")
def clientpage1page(request):
    pid = request.session.get('pid')  # सेशन से PID प्राप्त करें

    if not pid:  # अगर PID None आ रहा है, तो error पेज दिखाएँ
        return render(request, "myapp/error.html", {"error": "Session expired or PID not found!"})

    return render(request, "myapp/clientpage1.html", {"pid": pid})
