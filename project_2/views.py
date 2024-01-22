from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import userform,calc1,subjectform
from service2.models import service
from django.core.paginator import Paginator
from service2.models import savedata
from django.conf import settings
from django.core.mail import send_mail,EmailMultiAlternatives

def try1(request):
    data={
        'title':'home page',
        'clist':['c','java','python'],
        'tables':[{'name':'smit', 'no':'123456'},{'name':'karan', 'no':'98765'}],
        'number':[10,20,30,40,50,60]
    }
    return render(request,'try.html',data)

def homepage(request):
    dict1={}
    data = service.objects.all()
    if request.method == "GET" :
       search1 = request.GET.get('datasearch')
       if search1 != None:
        data = service.objects.filter(service_title__icontains=search1)
    return render(request,"index.html",{'data': data})

def web(request):
    return render(request,"web.html")
def c_language(request):
    return render(request,"c_language.html")
def java(request):
    return render(request,"java.html")

def login(request):
    return render(request,"login.html")

def signup(request):
    return render(request,"signup.html")


def get_method(request):
    dict1={
        "name" : "Nun",
        "email" : "Nun",
        "number" : "Nun",
        "address" : "Nun"
    }
    try:
        if request.method == "GET":
            dict1={
                "name" : request.GET.get('name'),
                "email" : request.GET.get('email'),
                "number" : int(request.GET.get('number')),
                "address" : request.GET.get('address')
                }
    except:
        dict1={
        "name" : "enter all field",
        "email" : "enter all field",
        "number" : "enter all field",
        "address" : "enter all field"
    }
    return render(request,"get.html",dict1)
    
def post_method(request):
    fn=userform()
    dict1={'form' : fn}
    try:
        if request.method == "POST":
            dict1={
                'form' : fn,
                "name" : request.POST.get('name'),
                "email" : request.POST.get('email'),
            }

            # url="/?output={}".format(dict1["name"])
            # return HttpResponseRedirect(url)
    except:
        dict1={
        "name" : "enter all field",
        "email" : "enter all field",    
    }
    return render(request,"post.html",dict1)

def output1(request):
    try:
        dict1={
        'name': request.POST.get("name"),
        'email': request.POST.get("email"),
        'number': request.POST.get("number"),
        'address': request.POST.get("address")
        }
    except:
        pass
    return HttpResponse(dict1['name'])

def calculator(request):
    cal1 = calc1()
    dict2={"form" : cal1}
    result = 0
    try:
        if request.method == "POST":
            value1=int(request.POST.get("value1"))
            value2= int(request.POST.get("value2"))
            match request.POST.get("dropdown1"):
                case "+" :
                    result= value1+value2
                case "-" :
                    result= value1-value2
                case "*" :
                    result= value1*value2
                case "/" :
                    result= value1/value2

            dict2={
            "form" : cal1,
            "result": result 
            }
    except:
        dict2={"form" : cal1,
            #    "result": result
        }
    return render(request,"calculator.html",dict2)

def subjectavg(request):
    sub = subjectform()
    avg = 0
    if request.method == "POST" :
        if (request.POST.get("sub1") == ""  or request.POST.get("sub2") == "" or request.POST.get("sub3") == ""):
            return render(request,"avg.html",{"error":True,"sub":sub})

        value1 = int(request.POST.get("sub1"))
        value2 = int(request.POST.get("sub2"))
        value3 = int(request.POST.get("sub3"))
        avg = (value1 + value2 + value3)/3
    else :
        avg = -1
    return render(request,"avg.html",{"avg":avg,"sub":sub})


def model_demo(request):
    ser = service.objects.all().order_by('service_icon')

    return render(request,"model_demo.html",{'data' : ser})


def detailpage(request,slug):
    detail = service.objects.get(slug_name=slug)
    send_mail(
        'testing mail',
        'hello there smit here',
        settings.EMAIL_HOST_USER,
        ['smitrajani28@gmail.com'],
        fail_silently=False
    )

    return render(request,"details.html",{'detail' : detail})

def paging(request):
    servicedata = service.objects.all()
    paginator1 = Paginator(servicedata,2)
    # page_number = 1 
    if request.method == "GET" :
        page_number = request.GET.get('page')
    print(page_number)
    databypage = paginator1.get_page(page_number,)
    total_pages = databypage.paginator.num_pages
    list1 = [i+1 for i in range(total_pages)]
    return  render(request,"paging.html",{'data': databypage, 'last_page': total_pages , 'list1' : list1})

def save_data(request):
    if request.method == "POST" :
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        address = request.POST.get('address')
    en = savedata(name=name, email=email, number=number, address=address)
    en.save()
    return render(request,"post.html")

def sendingmail(request):
    subject = "just testing"
    from_email = settings.EMAIL_HOST_USER
    message = '<p>hello there <b>user</b></p>'
    to_mail = ['padshalahimanshi05@gmail.com','smitrajani28@gmail.com']
    msg = EmailMultiAlternatives(subject,message,from_email,to_mail)
    msg.content_subtype = 'html'
    msg.send()
    return render(request,"index.html")