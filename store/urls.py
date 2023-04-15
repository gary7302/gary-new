from django.urls import path
from .views import *
from store.controller import authview,cartview,checkview,chineseview,paymentview,hindiview,spanishview
from django.views.i18n import set_language

urlpatterns = [
    path('',home,name='home'),
    path('type/<str:slug>',type,name='type'),
    path('register',authview.register,name='register'),
    path('login',authview.loginpage,name='loginpage'),
    path('logout',authview.logoutpage,name='logoutpage'),
    path('add-to-cart',cartview.addtocart,name='addtocart'),
    path('cart',cartview.showCart,name='cart'),
    path('update-cart',cartview.updatecart,name="updatecart"),
    path('delete-cart-item',cartview.deletecartitem,name="deletecartitem"),
    path('checkout',checkview.checkout,name='checkout'),
    path('maincheckout',checkview.maincheckout,name='maincheckout'),
    path('place-order',checkview.placeorder,name="placeorder"),
    path('charge', paymentview.charge, name='charge'),
    path('success/', paymentview.success, name='success'),
    path('type/comment/<int:id>/', comment, name='comment'),
    path('chinese-comment/<int:id>',chineseview.comment,name='chinese-comment'),
    path('addComment/<int:id>', addComment, name='addComment'),
    path('chinese-addcomment/<int:id>',chineseview.addComment,name='chinese-addcomment'),
    #path('set-language/', set_language, name='set_language'),
    path('chinese',chineseview.chinesehome,name='chinese'),
    path('hindi',hindiview.hindihome,name='hindi'),
    path('spanish',spanishview.spanishhome,name='spanish'),
    path('details',details,name='details'),
    path('chinese-details',chineseview.chinesedetails,name='chinese-details'),
    path('getpatch',getpatch,name='getpatch'),
    path('chinese-getpatch',chineseview.chinesegetpatch,name='chinese-getpatch'),
    path('usepatch',usepatch,name='usepatch'),
    path('chinese-usepatch',chineseview.chineseusepatch,name='chinese-usepatch'),
]