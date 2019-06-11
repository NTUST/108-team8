from django.shortcuts import render_to_response, get_object_or_404, render ,redirect
from .models import Store
from login.models import Users
from django.views import generic
from django.core.paginator import Paginator
from django.contrib import messages
from django.db import models
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect

# Create your views here.
from django.template import RequestContext
#可以連上首頁而已
# CSRF_COOKIE_SECURE=True
# @csrf_exempt
# @csrf_protect
def index(request):
    if request.method=='POST':
        if 'loginAccount' in request.POST:
            loginAccount=request.POST['loginAccount']
            loginPassword=request.POST['loginPassword']

            if Users.objects.filter(user_account=loginAccount):
                user=Users.objects.get(user_account=loginAccount)
                if(user.password==loginPassword):
                    msg=loginAccount+'登入成功'
                    isLogin=True
                    return render_to_response('final-web/index.html',locals())
                else:
                    msg='密碼錯誤'
                    return render_to_response('final-web/index.html',locals())
            else:
                msg='無此帳號'
                return render_to_response('final-web/index.html',locals())

        else:
            uName=request.POST['uName']
            uAccount=request.POST['uAccount']
            uPassword=request.POST['uPassword']
            againPassword=request.POST['againPassword']
            uemail=request.POST['uemail']      
            if Users.objects.filter(user_account=uAccount):
                msg='相同的帳號'
                return render_to_response('final-web/index.html',locals())
            elif uPassword==againPassword:
                msg='註冊成功'
                isSucce=True
                user=Users(name=uName,email=uemail,password=uPassword,user_account=uAccount)
                user.save()
                return render_to_response('final-web/index.html',locals())
            else:
                msg='確認密碼不同'
                isSucce=False
                return render_to_response('final-web/index.html',locals())
    st3=Store.objects.all().order_by('id')[:3] 
    st6=Store.objects.all().order_by('id')[:6] 
    return render_to_response('final-web/index.html',locals())

# def indexlike(request):
     
#     context={}
#     context['shoplike']=st3
#     return render(request,'final-web/index.html',context)
#store 這邊要爬資料，讓每個店家有自己的頁面
#目前未完成
class StoreView(generic.DetailView):
    model=Store
    template_name ='final-web/store.html'
    def get_queryset(self):
        return Store.objects.all()
    # def shoplike_3(request):
       
def store(request,store_id):
    store=get_object_or_404(Store,pk=store_id)
    st3=Store.objects.all().order_by('id')[:3]  
    return render(request,'final-web/store.html',locals()) 
     


# def shoplike_4(request):
#     st3=Store.objects.all().order_by('id')[:3]  
#     context={}
#     context['shoplike']=st3
#     return render(request,'final-web/index.html',context)

def shops(request):
    #爬每個店家的資料放到列表上
  
    st3=Store.objects.all().order_by('id')[:3]  
    stores=Store.objects.all().order_by('id')
    paginator = Paginator(stores,6)
    page_num=request.GET.get('page',1)
    page_of_stores= paginator.get_page(page_num)
    current_page_num=page_of_stores.number

    page_range = list(range(max(1, current_page_num - 2), current_page_num)) + list(range(current_page_num, min(paginator.num_pages, current_page_num + 2)))

    if page_range[0]-1>=2:
        page_range.insert(0,'...')
    if page_range[-1]+2<=paginator.num_pages:
        page_range.append('...')

    if page_range[0]!=1:
        page_range.insert(0,1)
    if page_range[-1]!=paginator.num_pages:
        page_range.append(paginator.num_pages)
    context={}
    context['shoplike']=st3
    context['store']=page_of_stores.object_list
    context['page_of_stores']=page_of_stores
    context['page_range']=page_range
    return render(request,'final-web/shops.html',context)
    #return render(request,'final_web/index.html')
def statement(request):
    st3=Store.objects.all().order_by('id')[:3]  
    context={}
    context['shoplike']=st3
    return render(request,'final-web/generic_2.html',context)
def fight(request):
    st3=Store.objects.all().order_by('id')[:3]  
    context={}
    context['shoplike']=st3
    return render(request,'final-web/generic_1.html',context)
def addStore(request):
    if request.method=='POST':
        #get_object_or_404(Users,all)
        uStoreName=request.POST['uStoreName']
        uAddress=request.POST['uAddress']
        uPhone=request.POST['uPhone']
        uOpen=request.POST['uOpen']
        uIntroduction=request.POST['uIntroduction']
        use=Users.objects.get(id=1)
        store=Store(store_name=uStoreName,store_introduction=uIntroduction,store_address=uAddress,store_phone=uPhone,store_opening_time=uOpen,account=use)
        store.save()

    st3=Store.objects.all().order_by('id')[:3]
    return render(request,'final-web/addStore.html',locals())
      

