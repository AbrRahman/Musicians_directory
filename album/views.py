from django.shortcuts import render,redirect
from album.forms import AlbumForm
from album.models import AlbumModel
# Create your views here.
def add_album(request):
    if request.method=="POST":
        album_form=AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect("add_album")
        
    else:
        album_form=AlbumForm()
    return render(request,"album_form.html",{"form":album_form})

def edit_album(request,id):
    data=AlbumModel.objects.get(pk=id)
    album_form=AlbumForm(instance=data)
    if request.method=="POST":

        album_form=AlbumForm(request.POST,instance=data)
        if album_form.is_valid():
            album_form.save()
            return redirect("home")
        
    return render(request,"album_form.html",{"form":album_form})

def delete_album(request,id):
    data=AlbumModel.objects.get(pk=id)
    data.delete()
    return redirect("home")