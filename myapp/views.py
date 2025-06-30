from django.shortcuts import render,redirect
from myapp.models import Author,Publisher,Book
from myapp.forms import AuthorForm,BookForm,PublisherForm

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import user_passes_test

from django.contrib.auth.decorators import login_required


# Create your views here.


def is_admin(user):
    return user.is_superuser

def homepage(request):
    return render(request,"home.html")

@login_required(login_url='login')
def authorpage(request):    
    authors = Author.objects.all()
    return render(request,"authors.html",{'authors': authors})

@login_required(login_url='login')
def bookpage(request):
    books = Book.objects.all()
    return render(request,"books.html",{'book': books})

@login_required(login_url='login')
def publisherpage(request):
    publishers = Publisher.objects.all()
    return render(request, 'publisher.html', {'pbook': publishers})

@user_passes_test(is_admin)
def addauthor(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authors')
    else:
        form = AuthorForm()
    return render(request, 'authorform.html', {'form': form})

@user_passes_test(is_admin)
def editauthor(request, id):
    
    author = Author.objects.get(id=id)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('authors')
    else:
        form = AuthorForm(instance=author)
    return render(request, 'authorform.html', {'form': form})


@user_passes_test(is_admin)
def deleteauthor(request, id):
    author = Author.objects.get(id=id)
    if request.method == 'POST':
        author.delete()
        return redirect('authors')
    return render(request, 'deleteauthor.html', {'author': author})


@user_passes_test(is_admin)
def addbook(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = BookForm()
    return render(request, 'bookform.html', {'form': form})


@user_passes_test(is_admin)
def editbook(request, id):    
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookform.html', {'form': form})


@user_passes_test(is_admin)
def deletebook(request, id):    
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('books')
    return render(request, 'deletebook.html', {'book': book})


@user_passes_test(is_admin)
def addpublisher(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('publishers')
    else:
        form = PublisherForm()
    return render(request, 'publisherform.html', {'form': form})


@user_passes_test(is_admin)
def editpublisher(request, id):    
    pub = Publisher.objects.get(id=id)
    if request.method == 'POST':
        form = PublisherForm(request.POST, instance=pub)
        if form.is_valid():
            form.save()
            return redirect('publishers')
    else:
        form = PublisherForm(instance=pub)
    return render(request, 'publisherform.html', {'form': form})


@user_passes_test(is_admin)
def deletepublisher(request, id):    
    pub = Publisher.objects.get(id=id)
    if request.method == 'POST':
        pub.delete()
        return redirect('publishers')
    return render(request, 'deletepublisher.html', {'pub': pub})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
def logoutpage(request):
    logout(request)
    return redirect('login')
def loginpage(request):
    af=AuthenticationForm()
    if request.method=='POST':
        af=AuthenticationForm(data=request.POST)
        if af.is_valid():
            user=af.get_user()
            login(request,user)
            return redirect('home')
    return render(request,"login.html",{'form':af})








