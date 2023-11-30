from django.shortcuts import render, redirect, HttpResponse
from .models import *
from .forms import *
from json import dumps
# Create your views here.
def exhibition(request):
    user = None
    if "id" in request.session:
        user_id = int(request.session['id'])
        user = User.objects.get(id=user_id)
    exe = Exhibition.objects.all()
    data=[]
    for i in exe:
        temp = {'title':i.title, 'start':str(i.date_start)[0:10], 'end':str(i.date_end)[0:10]}
        data.append(temp)
    dataJSON = dumps(data)
    print
    print(dataJSON)
    return render(request, 'exhibition.html', {'data':dataJSON, 'exe':exe, 'user':user})


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
            place = cd['place'],
            )
            artwork.save() 
            user.artworks.add(artwork)
            tags = cd['tags'].split(', ')
            print(len(tags))
            print(tags)
            if(len(tags)-1):
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
    user = None
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
    return render(request, 'regist.html', {'form': form, 'user':user})



def artwork(request, pk):
    user = None
    if "id" in request.session:
        user_id = int(request.session['id'])
        user = User.objects.get(id=user_id)
    artwork = Artwork.objects.get(id=pk)
    coun = artwork.comments.count()
    usr = artwork.users.all()
    context = {'artwork': artwork, 'coun': coun, 'usr': usr, 'user': user}
    return render(request, 'artwork.html', context)

def home(request):
    return render(request, 'home.html')

def art_works(request):
    user = None
    if "id" in request.session:
        user_id = int(request.session['id'])
        user = User.objects.get(id=user_id)
    art_works = Artwork.objects.all()
    context = {'artworks': art_works, 'user': user}
    return render(request, 'blog.html', context=context)

def maps(request):
    user = None
    if "id" in request.session:
        user_id = int(request.session['id'])
        user = User.objects.get(id=user_id)
    art_works = Artwork.objects.all()
    context = {'artworks': art_works, 'user': user}
    return render(request, 'maps.html', context=context)

def login(request):
    user= None
    usr_account = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            cd = form.cleaned_data
            try:
                usr_account = User.objects.get(login=cd["login"])   
            except User.DoesNotExist:
                print("Error Account")
            if (usr_account):
                if(usr_account.password == cd["password"]):
                    id_usr = int(usr_account.id)
                    request.session.set_expiry(24*3600)
                    request.session['id'] = id_usr
                    return redirect("/account/")
                else:
                    print("wrong password")
                    form.add_error("password", "Пароль неправильный!")
            else:
                print("Error Account")
                form.add_error("login", "Такого аккаунта не существует!")

    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form, 'user': user})

def account(request):
    if "id" in request.session:
        user_id = int(request.session['id'])
        user = User.objects.get(id=user_id)
        coun = user.artworks.count()
        exe = user.favorite.all()
        data=[]
        for i in exe:
            temp = {'title':i.title, 'start':str(i.date_start)[0:10], 'end':str(i.date_end)[0:10]}
            data.append(temp)
        dataJSON = dumps(data)


        form = {"user":user, 'coun': coun, 'data': dataJSON}
        response = render(request, 'account.html', context=form)
        response.set_cookie('In_Account', 'True')
        return response
    else:
        return redirect("/login/")
    

def post_comment(request):
    user = None
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
            context = {'artwork': artwork, 'coun': coun, 'usr': usr, 'user':user}
            return render(request, "artwork_comments.html", context=context)
    else:
        return redirect("/login/")
    
def liked_exhibition(request):
    if 'id' in request.session:
        id_per = request.session['id']
        account = User.objects.get(id=id_per)
    else: 
        return redirect("/login/")
    if request.method == 'POST':
        liked_id = request.POST.get('liked_id', None)
        account.favorite.add(Exhibition.objects.get(id=liked_id))
        return HttpResponse("<h1>Nice!</h1>")

def unliked_exhibition(request):
    if 'id' in request.session:
        id_per = request.session['id']
        account = User.objects.get(id=id_per)
    else: 
        return redirect("/login/")
    if request.method == 'POST':
        liked_id = request.POST.get('liked_id', None)
        account.favorite.remove(Exhibition.objects.get(id=liked_id))
        return HttpResponse("<h1>Nice!</h1>")


def liked_artwork(request):
    if 'id' in request.session:
        id_per = request.session['id']
        account = User.objects.get(id=id_per)
    else: 
        return redirect("/login/")
    if request.method == 'POST':
        liked_id = request.POST.get('liked_id', None)
        account.liked.add(Artwork.objects.get(id=liked_id))
        return HttpResponse("<h1>Nice!</h1>")

def unliked_artwork(request):
    if 'id' in request.session:
        id_per = request.session['id']
        account = User.objects.get(id=id_per)
    else: 
        return redirect("/login/")
    if request.method == 'POST':
        liked_id = request.POST.get('liked_id', None)
        account.liked.remove(Artwork.objects.get(id=liked_id))
        return HttpResponse("<h1>Nice!</h1>")



