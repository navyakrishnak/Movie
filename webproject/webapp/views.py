from django.http import HttpResponse
from django.shortcuts import render, redirect
from . forms import Bookform
from . models import Books

# Create your views here.
def index(request):
    book=Books.objects.all()
    context={
        'Book_list':book
    }

    return render(request,'index.html',context)

def detail(request,book_id):
    book=Books.objects.get(id=book_id)
    return render(request,"detail.html",{'book':book})

def add_book(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        desc = request.POST.get('desc', )
        year = request.POST.get('year', )
        img = request.FILES['img']
        book=Books(name=name,desc=desc,year=year,img=img)
        book.save()
        return redirect('/')
    return render(request,'add.html')

def update(request,id):
    book=Books.objects.get(id=id)
    form=Bookform(request.POST or None,request.FILES,instance=book)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'book':book})

def delete(request,id):
    if request.method=='POST':
        book=Books.objects.get(id=id)
        book.delete()
        return redirect('/')
    return render(request,'delete.html')