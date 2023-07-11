from django.shortcuts import render,  redirect
from .forms import ImageForm
from .models import Image
from django.http import HttpResponse

# Create your views here.

def index(request):

    if request.method == "POST":
        form = ImageForm(data=request.POST, files=request.FILES)
        if form.is_valid():

            form.save()
            obj = form.instance #create context and passed to template
            return render(request, "index.html", {"obj":obj})
    else:

        form = ImageForm()
        img = Image.objects.all() #take all fields of the objects
        return render(request, "index.html", { "img": img, "form": form})


# Create your views here.
