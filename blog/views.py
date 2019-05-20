from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.utils import timezone
from .models import Post, Comment
from .forms import PostForm, LoginForm, CommentForm
from django.http import HttpResponse

# email test
from django.core.mail import EmailMessage

#lte : less than equal
# lt : less than
# gte :  greater than equal
# gt :  greater than


def post_list(request):
    if request.GET.get('item'):
        var_col = request.GET.get('fd_name')
        search_type='contains'
        filter = var_col + '__' + search_type
        print(filter)
        posts = Post.objects.filter(**{filter: request.GET.get('item')}).order_by('-published_date')
        return (request, 'blog/post_list.html',{'posts':posts})
    
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html',{'posts':posts})

def post_detail(request, pk):
    # try:
    #     post = Post.objects.get(pk=pk) # Post.DoesNotExist pk 가 없을 경우 500에러 처리를 막아준다.
    # except Post.DoesNotExist:
    #     raise Http404   # django.http.Http404

    post = get_object_or_404(Post, pk=pk) # 위의 4줄과 같은 역할
    return render(request, 'blog/post_detail.html', {'post':post})

#로그인 요구를 위한 장식자
@login_required(login_url='admin:login')
def post_new(request):
    if request.method =='POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()
            post.save()

            #email test#######
            # try:
            #     email = EmailMessage('email test', '새로운 글이 등록되었습니다.',  to=['5hyung@datasolution.kr'])
            #     email.send()
            # except:
                
            #########
            return redirect('post_detail', post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form':form})

@login_required(login_url='admin:login')
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form  =  PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk = post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html',{'form':form})

def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts':posts})

def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form  = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html',{'form':form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail',pk=comment.post.pk)


# def post_search(request):

    
    
