from django.shortcuts import redirect, render
from .models import Exampledatabase
def home(request):
    if request.method=='POST':
        director=request.POST['direct_name']
        movie_name=request.POST['movie_name']
        total_directed=request.POST['total_movies']
        exampledatabase=Exampledatabase.objects.create(
            director=director,
            movie_name=movie_name,
            total_directed=total_directed,
        )
        exampledatabase.save()
        return redirect('retrived')

    return render(request,'home.html')

def retrived(request):
    exampledatabase=Exampledatabase.objects.all()
    context={
        'exampledatabase':exampledatabase
    }
    return render(request,'retrived.html',context)
# Create your views here.