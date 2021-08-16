from django.shortcuts import render, redirect, HttpResponsePermanentRedirect
from django.contrib.auth import authenticate, login
from .forms import RegisterForm, LoginForm
from django.contrib import messages

def register_user(request):
    form = RegisterForm
    if request.method =="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save_user()
            return redirect('index')
    
    return render(
        request=request,
        template_name= "user/register.html",
        context={
            'form':form
        }
    )

def login_user(request):
    # form = LoginForm
    message= ""
    if request.method =="POST":
        # form = LoginForm(request.POST)
        # if form.is_valid():
            # authenticate nhận taikhoan va matkhau
            # check xem dun ko
        user=authenticate(
            username=request.POST['username'],
            password=request.POST['password'],
        )
        if user is not None:
            print("Dung")
            login(request, user)
            return redirect('index')
        else:
            print("sai")
            messages.info(request, "Tài khoản hoặc mật khẩu không đúng. Vui lòng thử lại")

        # if user:
        #     print("Dung")
        #     login(request,user) # giu trang thai dang nhap
        #     # Đưa thẳng đến trang cần làm ko cấn qua index
        #     if request.GET.get('next'): 
        #         return HttpResponsePermanentRedirect(request.GET.get('next'))
        #     return redirect('index')
        # else:
        #     print("sai")
        #     message= "Tên đăng nhập hoặc mật khẩu không trùng khớp. Vui lòng thử lại"
    
    return render(
        request=request,
        template_name="user/login.html",
        context={
            # 'form':form,
            'message':message
        }
    )