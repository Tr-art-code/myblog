from django.shortcuts import redirect, render, HttpResponse
from app01.models import UserInfo

# Create your views here.
def index(request):
    # return HttpResponse("Hello World".encode('utf-8'))
    return render(request, "index.html")

def clock(request):
    return render(request, "clock.html")

def main(request):
    return render(request, "main.html")

def posts(request):
    return render(request, "posts.html")
    
def archive(request):
    return render(request, "archive.html")

def about(request):
    return render(request, "about.html")

def login(request):
    print(request.method)
    print(request.GET)
    print(request.POST)
    return render(request, "login.html")

def test(request):
    return render(request, "test.html")

def redirection(request):
    return redirect("/login/")
    # return redirect("https://www.baidu.com")

def infolist(request):
    if request.method == "POST":
        # 获取表单数据
        username = request.POST.get("name")
        password = request.POST.get("password")
        age = request.POST.get("age")
        
        # 创建新用户
        UserInfo.objects.create(
            username=username,
            password=password,
            age=int(age)
        )
        
        # 重定向到用户列表页面
        return redirect("/infolist/")
    
    # 获取所有用户信息
    user_list = UserInfo.objects.all()
    
    return render(request, "infolist.html", {"user_list": user_list})
def deleteinfo(request):
    nid = request.GET.get("nid")
    UserInfo.objects.filter(id=nid).delete()
    return redirect("/infolist/")