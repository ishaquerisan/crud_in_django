
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book


# Create your views here.
def bookList(request):  
    books = Book.objects.all()  
    return render(request,"book-list.html",{'books':books})  

def bookCreate(request):  
    if request.method == "POST":  
        ob = Book()
        ob.title=request.POST['title']
        ob.year=request.POST['year']
        ob.country=request.POST['country']
        ob.description=request.POST['description']
        ob.file = request.FILES['file']
        ob.save()
        return redirect('book-list')
    else:  
        form = BookForm()  
    return render(request,'book-create.html',{'form':form})  

def bookUpdate(request, id):
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        # Handle the case where the book with the given ID doesn't exist.
        # You can raise an Http404 exception or redirect to an error page.
        return HttpResponseNotFound("Book not found")

    if request.method == "POST":
        # Update the book instance with new data from the form
        book.title = request.POST['title']
        book.year = request.POST['year']
        book.country = request.POST['country']
        book.description = request.POST['description']
        book.file = request.FILES['file']
        
        # Save the updated book instance
        book.save()
        
        # Redirect to a success page or wherever you want to go after the update.
        books = Book.objects.all()  
        return render(request,"book-list.html",{'books':books})  
        # If the form is not valid, it will be redisplayed with error messages.
    else:
        form = BookForm(instance=book)

    return render(request, 'book-update.html', {'form': form, 'book': book})


def bookDelete(request, id):
    book = Book.objects.get(id=id)
    try:
        book.delete()
    except:
        pass
    return redirect('book-list')

