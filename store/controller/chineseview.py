from django.shortcuts import render,redirect
from django.contrib import messages
from store.models import *
from store.forms import *
from datetime import datetime
def chinesehome(request):
    category=ChineseCategory.objects.all()
    return render(request,'chinese-store/index.html',{'category':category})

def chinesegetpatch(request):
    return render(request,'chinese-store/getpatch.html')

def chineseusepatch(request):
    return render(request,'chinese-store/usepatch.html')

def chinesedetails(request):
    return render(request,'chinese-store/details.html')

def comment(request,id):
    eachProduct = ChineseCategory.objects.get(id=id)


<<<<<<< HEAD
    form = ChinaCommentForm()
=======
    form = CommentForm()
>>>>>>> dbd2428dbb022ddde7293e2f42e68deee4422436
    context={'form':form,'eachProduct':eachProduct}
    return render(request,'chinese-store/coment.html',context)

def addComment(request,id):
    if request.method == "POST":
<<<<<<< HEAD
        form = ChinaCommentForm(request.POST, request.FILES)
=======
        form = CommentForm(request.POST, request.FILES)
>>>>>>> dbd2428dbb022ddde7293e2f42e68deee4422436
        if form.is_valid():
            commenter_name = request.user
            comment_body = form.cleaned_data['comment_body']
            comment_image = form.cleaned_data['comment_image']
            eachProduct = ChineseCategory.objects.get(id=id)
<<<<<<< HEAD
            c = ChinaComment(product=eachProduct, commenter_name=commenter_name, comment_body=comment_body,comment_image=comment_image, created_at=datetime.now())
            c.save()
            return redirect('chinese')
    return HttpResponse('<h1>We are uable to add your comment</h1>')
=======
            c = Comment(product=eachProduct, commenter_name=commenter_name, comment_body=comment_body,comment_image=comment_image, created_at=datetime.now())
            c.save()
            return redirect('chinese')
    return HttpResponse('<h1>We are unable to add your comment</h1>')
>>>>>>> dbd2428dbb022ddde7293e2f42e68deee4422436
