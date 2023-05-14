from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import SignUpForm, Profile_EditForm, PostForm
from django.contrib.auth import get_user_model
from .models import User_profile, Post
# Create your views here.

user = get_user_model()


def signUp(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        user = form.save()

        profile = User_profile.create(user)
        profile.save()
        return redirect('home')


    else:
        form = SignUpForm()
    return render(request, 'registration\signUp.html', {"form":form})



def home(request):
    return render(request, 'empty.html')


@login_required(login_url="/login")
def profile_editing(request, slug):
    profile_QuerySet = User_profile.objects.filter(username=slug)
    
    if request.method == 'POST':
       
        form = Profile_EditForm(request.POST)
        
        updated_profile = form.save(commit=False)
       
        profile_QuerySet.update(username= updated_profile.username, name=updated_profile.name, email=updated_profile.email, bio=updated_profile.bio)

        return redirect('home')
    else:
        form = Profile_EditForm(instance = profile_QuerySet[0])

    return render(request, 'profile/ProfilePage.html', {"form": form})


def profile_screen(request,slug):
        
        profile = User_profile.objects.get(username=slug)
        
        context = {
                'name': profile.name,
                'email':profile.email,
                'username':profile.username,
                'bio':profile.bio,

        }
        return render(request, 'profile/Profile_Screen.html',context=context)


@login_required(login_url='/login')
def post(request):

    if request.method == 'POST':
        post_user = request.user
        form = PostForm(request.POST)
        post = form.save(commit=False)
        post._id = post_user

        post.save()
        return redirect('home')
    
    else:
        form = PostForm()

    return render(request,'post/PostPage.html', {'form':form})


def screenpost(request, slug):
    post_data = Post.objects.get(id=slug)
    print(post_data.post_data)
    context = {
        'post_data':post_data.post_data,
        'title': post_data.title,
        'place': post_data.place,
        'date': post_data.date,
        'username': post_data._id.username,
    }
    return render(request,'post/ScreenPost.html',context=context) 