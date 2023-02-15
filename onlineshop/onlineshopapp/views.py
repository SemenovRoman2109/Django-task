from django.shortcuts import render,redirect
from django.db.utils import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Product,Comment

# Create your views here.
def show_form_reg(request):
    context={}
    if request.method == "POST":
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        print(username)
        context = {
            'password':password,
            'password_confirm':password_confirm,
            'username':username
        }
        if password == password_confirm:
            try:
                User.objects.create_user(username = username, password = password)
                return redirect("form_log")
            except IntegrityError:
                context['error_text']= 'Такий користувач вже існує!'
        else:
            context['error_text'] = "Паролi не спiвпадають"

    return render(request, "onlineshopapp/form_reg.html")
    
def show_form_log(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user != None:
            login(request,user)
            return redirect('product')
        else:
            context['error_text'] = "Помилка не вiрний логiн або пароль"
    return render(request, 'onlineshopapp/form_log.html',context=context)

def show_product(request): 
    if request.method == "POST":
        print(request.POST.get)
        content = request.POST.get('content')
        author = request.user.username
        Comment.objects.create(content = content, author = author)
    product = Product.objects.all()[0]
    list_comment = Comment.objects.all()
    return render(request, 'onlineshopapp/product.html',context={"product":product,"list_comment":list_comment})


