from django.shortcuts import render
from django.http import  HttpResponse
from django.http import QueryDict
from django.http import QueryDict,Http404
from hello.models   import  User
from django.shortcuts import get_list_or_404

# def index(request):
#     return HttpResponse("<p>hello world,hello Django</p>")
# Create your views here.
#普通传参
# def index(request):
#     year=request.GET.get("year","2020")
#     #month=request.GET["month"]
#     month = request.GET.get("month","03")
#     return HttpResponse("year is {},month is {}".format(year,month))

#位置传参
# def index(request,year,month):
#     return HttpResponse("year is {},month is {}".format(year,month))
#关键字传参
# def index(request, **kwargs):
#     print(kwargs)
#     year=kwargs.get('year')
#     month=kwargs.get('month')
#     return HttpResponse("year is {},month is {}".format(year, month))

# def index(request):
#     print(request.scheme)
#     print(request.method)
#     print(request.headers)
#     print(request.headers)
#     print(request.path)
#     print(request.META)
#     print(request.GET)
#     data=request.GET
#     year=data.get("year","2020")
#     month=data.get("month","10")
#     if request.method == 'POST':
#         print(request.method)
#         print(request.body)
#         print(QueryDict(request.body).dict())
#         print(request.POST)
#         data=request.POST
#         year=data.get("year","2020")
#         month=data.get("month","10")
#     return HttpResponse("year is {},month is {}".format(year, month))

def index(request):
    classname="Devops"
    books=['python','java','django']
    user={'name':'kk','age':18}
    userlist=[{'name':'kk','age':18},{'name':'rock','age':19},{'name':'mage','age':30}]
    return render(request,'hello/hello.html',{'classname':classname,"books":books,"user":user,"userlist":userlist})

def list(request):
    messages=['1','2','22','2223','33']
    users = [
        {'username': 'kk1','name_cn': 'kk1', 'age': 19},
        {'username': 'kk2','name_cn': 'kk2', 'age': 19},
        {'username': 'kk3','name_cn': 'kk3', 'age': 19},
        ]
    value=['python','django','java']
    return render(request,'userlist1.html',{"users":users,"messages":messages,"value":value})

def userlist(request):
    users=User.objects.all()
    return render(request, 'hello/../templates/index.html', {'users':users})
