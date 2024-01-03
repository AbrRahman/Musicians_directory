from django.shortcuts import render,redirect
from album.forms import AlbumForm
from album.models import AlbumModel
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def add_album(request):
    if request.method=="POST":
        album_form=AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect("add_album")
        
    else:
        album_form=AlbumForm()
    return render(request,"album_form.html",{"form":album_form})

@login_required
def edit_album(request,id):
    data=AlbumModel.objects.get(pk=id)
    album_form=AlbumForm(instance=data)
    if request.method=="POST":

        album_form=AlbumForm(request.POST,instance=data)
        if album_form.is_valid():
            album_form.save()
            return redirect("home")
        
    return render(request,"album_form.html",{"form":album_form})

@login_required
def delete_album(request,id):
    data=AlbumModel.objects.get(pk=id)
    data.delete()
    return redirect("home")