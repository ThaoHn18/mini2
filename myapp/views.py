from django.shortcuts import get_object_or_404, render,redirect,get_list_or_404
from django.http import HttpResponse
from .models import Book,Author
from .forms import AuthorForm, Bookform
# Create your views here.
def index(request): # Tham số bắt buộc phải có các hàm views.py 
    # # là resquest : httpresquest
    # print(request.GET['name']) #request.get nằm trên url khi mình gõ
    # name= request.GET.get('name','')
    # request.session['name'] = name
    # response= HttpResponse()
    # response.write("<h1> Alo Hello Thao</h1>")
    # response.write("Đây là app đầu tiên của Thao")
 
    age=12
    name="Alice"
    all_authors=Author.objects.all()
    return render(
        request=request,
        template_name="index.html",
        context={
            'all_authors':all_authors
        }
    )
def home(request):
    name= request.session.get('name','')
    return HttpResponse('Hello' + name)

def add_author(request):
    author_form=AuthorForm()
    if request.method == "POST":
        print(request.POST)
        author_form = AuthorForm(request.POST)
        if author_form.is_valid():   # hàm is_valid() nó gọi tất cả các hàm mà bắt đầu clean_
            print("Form validate OK")
            data = author_form.cleaned_data # cleand_data trong is_valid. tý bật lên sau
            author_form.save()
            return redirect("index")
    return render(
        request=request,
        template_name='author/add.html',
        context={
            'form': author_form
        }
    )

def add_book(request):
    form_book = Bookform()
    if request.method == "POST":
        print(request.POST)
        form_book = Bookform(request.POST)
        if form_book.is_valid():   # hàm is_valid() nó gọi tất cả các hàm mà bắt đầu clean_
            print("Form validate OK")
            data = form_book.cleaned_data # cleand_data trong is_valid. tý bật lên sau
            form_book.save()
            return redirect("index")
    return render(
        request=request,
        template_name='book/add.html',
        context={
            'form': form_book
        }
    )

def view_detail_author(request, author_id):
    author_data = Author.objects.get(id=author_id)
    return render(
        request=request,
        template_name= 'author/detail.html',
        context={
            'author': author_data
        }
    )

def update_author(request, author_id):
    author_data = get_object_or_404(Author,id=author_id)
    author_form=AuthorForm(instance=author_data)
    if request.method == 'POST':
        author_data.first_name = request.POST.get('first_name',author_data.first_name)
        author_data.last_name = request.POST.get('last_name',author_data.last_name)
        author_data.email = request.POST.get('email',author_data.email)
        author_data.save()
        return redirect ("index")
    return render(
        request=request,
        template_name='author/update.html',
        context={
            'form': author_form
        }

    )

def delete_author(request, author_id):
     author_data = get_object_or_404(Author,id=author_id)
     author_data.delete()
     return redirect ("index")