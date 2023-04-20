from django.shortcuts import render,redirect
from django.contrib import messages
from store.models import *
from store.forms import *
from datetime import datetime
def hindihome(request):
    category=HindiCategory.objects.all()
    return render(request,'hindi-store/index.html',{'category':category})

def hindicomment(request,id):
    eachProduct = HindiCategory.objects.get(id=id)

    form = HindiCommentForm()
    context = {'form': form, 'eachProduct': eachProduct}
    return render(request, 'hindi-store/coment.html', context)

def hindiaddcomment(request,id):
    if request.method == "POST":
        form = HindiCommentForm(request.POST, request.FILES)
        if form.is_valid():
            commenter_name = request.user
            comment_body = form.cleaned_data['comment_body']
            comment_image = form.cleaned_data['comment_image']
            eachProduct = HindiCategory.objects.get(id=id)
            d = HindiComment(product=eachProduct, commenter_name=commenter_name, comment_body=comment_body,comment_image=comment_image, created_at=datetime.now())
            d.save()
            return redirect('hindi')
    return HttpResponse('<h1>We are unable to add your comment</h1>')
