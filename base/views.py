from django.shortcuts import render, redirect, HttpResponse
from .models import *
from .forms import *

# Create your views here.
def addartwork(request):
    if "id" in request.session:
        user_id = int(request.session['id'])
        user = User.objects.get(id=user_id)
    else:
        return redirect('/login/')
    if request.method == 'POST':
        form = AddArtWork(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            artwork = Artwork(
            face = cd['face'],
            name = cd['name'],
            description = cd['description'],
            uncompressed_img = cd['uncompressed_img'],
            object3d = cd['object3d'],
            )
            artwork.save() 
            user.artworks.add(artwork)
            tags = cd['tags'].split(', ')

            for tag in tags:
                tmp_user = User.objects.get(tag=tag)
                if tmp_user:
                    tmp_user.artworks.add(artwork)
                else:
                    print("Error: User with this tag does not exist")
            try:
                form.save()
                return redirect('/artwork/')
            except :
                form.add_error(None, "error add post")

        else:
            print("Error")
    else:
        form = AddArtWork()

    return render(request, 'addartwork.html', {'form': form})


def regist(request):
    if "id" in request.session:
        return redirect('/account/')
    if request.method == 'POST':
        form = RegistForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                form.save()
                return redirect('/login/')
            except :
                form.add_error(None, "error add post")

        else:
            print("Error")
    else:
        form = RegistForm()
    return render(request, 'regist.html', {'form': form})



def artwork(request, pk):
    artwork = Artwork.objects.get(id=pk)
    coun = artwork.comments.count()
    usr = artwork.users.all()
    context = {'artwork': artwork, 'coun': coun, 'usr': usr}
    return render(request, 'artwork.html', context)

def home(request):
    return render(request, 'home.html')

def art_works(request):
    art_works = Artwork.objects.all()
    context = {'artworks': art_works}
    return render(request, 'blog.html', context=context)

def maps(request):
    art_works = Artwork.objects.all()
    context = {'artworks': art_works}
    return render(request, 'maps.html', context=context)

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            cd = form.cleaned_data
            try:
                usr_account = User.objects.get(login=cd["login"])   
            except User.DoesNotExist:
                print("Error Account")
            if(usr_account.password == cd["password"]):
                id_usr = int(usr_account.id)
                request.session.set_expiry(24*3600)
                request.session['id'] = id_usr
                return redirect("/account/")
            else:
                print("wrong password")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def account(request):
    if "id" in request.session:
        user_id = int(request.session['id'])
        user = User.objects.get(id=user_id)
        coun = user.artworks.count()
        form = {"user":user, 'coun': coun}
        response = render(request, 'account.html', context=form)
        response.set_cookie('In_Account', 'True')
        return response
    else:
        return redirect("/login/")
    

def post_comment(request):
    if "id" in request.session:
        user_id = int(request.session['id'])
        user = User.objects.get(id=user_id)
        if request.method == "POST":
            text = request.POST.get('text', None)
            index = int(request.POST.get('index', None))
            tmp = Comment(author=user, text=text,)
            tmp.save()
            artwork = Artwork.objects.get(id=index)
            artwork.comments.add(tmp)
            print("success!")
            coun = artwork.comments.count()
            usr = artwork.users.all()
            context = {'artwork': artwork, 'coun': coun, 'usr': usr}
            return render(request, "artwork_comments.html", context=context)
    else:
        return redirect("/login/")
