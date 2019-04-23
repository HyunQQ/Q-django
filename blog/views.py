from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

#lte : less than equal
# lt : less than
# gte :  greater than equal
# gt :  greater than


def post_list(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html',{'posts':posts})

def post_detail(request, pk):
    # try:
    #     post = Post.objects.get(pk=pk) # Post.DoesNotExist pk 가 없을 경우 500에러 처리를 막아준다.
    # except Post.DoesNotExist:
    #     raise Http404   # django.http.Http404

    post = get_object_or_404(Post, pk=pk) # 위의 4줄과 같은 역할
    return render(request, 'blog/post_detail.html', {'post':post})