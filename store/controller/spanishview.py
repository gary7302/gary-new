from django.shortcuts import render,redirect
from django.contrib import messages
from store.models import *
from store.forms import *
from datetime import datetime
def spanishhome(request):
    category=SpanishCategory.objects.all()
    return render(request,'spanish-store/index.html',{'category':category})

def spanishcomment(request,id):
    eachProduct=SpanishCategory.objects.get(id=id)
    form=SpanishCommentForm()
    context={'form':form,'eachProduct':eachProduct}
    return render(request,'spanish-store/coment.html',context)

def spanishaddcomment(request,id):
    if request.method == "POST":
        form=SpanishCommentForm(request.POST,request.FILES)
        if form.is_valid():
            commenter_name = request.user
            comment_body = form.cleaned_data['comment_body']
            comment_image = form.cleaned_data['comment_image']
            eachProduct = SpanishCategory.objects.get(id=id)
            d = SpanishComment(product=eachProduct, commenter_name=commenter_name, comment_body=comment_body,
                             comment_image=comment_image, created_at=datetime.now())
            d.save()
            return redirect('spanish')
        return HttpResponse('<h1>We are unable to add your comment</h1>')