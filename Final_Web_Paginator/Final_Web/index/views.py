from django.shortcuts import render_to_response, get_object_or_404, render 
from .models import Store
from login.models import Users
from django.views import generic
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
# Create your views here.

#可以連上首頁而已
CSRF_COOKIE_SECURE=True
@csrf_exempt
@csrf_protect
def index(request):
    if request=='POST':
        get_object_or_404(Users,all)
        uName=request.POST['uName']
        uAccount=request.POST['uAccount']
        uPassword=request.POST['uPassword']
        againPassword=request.POST['againPassword']
        uemail=request.POST['uemail']
        if uPassword==againPassword:
            msg='註冊成功'
            isSucce=True
            user=Users.objects.create(name=uName,email=uemail,password=uPassword,user_account=uAccount)
            user.save()
            #RequestContext=[msg,isSucce]
            return render_to_response('final-web/index.html',{'msg':msg,'isSucce':isSucce})
        else:
            msg='確認密碼不同'
            isSucce=False
            #RequestContext=[msg,isSucce]
    return render_to_response('final-web/index.html',{'msg':msg,'isSucce':isSucce})
#store 這邊要爬資料，讓每個店家有自己的頁面
#目前未完成
class StoreView(generic.DetailView):
    model=Store
    template_name ='final-web/store.html'
    def get_queryset(self):
        return Store.objects.all()
def store(request,store_id):
    store=get_object_or_404(Store,pk=store_id)
    

def shops(request):
    #爬每個店家的資料放到列表上
    stores=Store.objects.all()
    paginator = Paginator(stores,6)
    page_num=request.GET.get('page',1)
    page_of_stores= paginator.get_page(page_num)
    current_page_num=page_of_stores.number

    page_range = list(range(max(1, current_page_num - 2), current_page_num)) + list(range(current_page_num, min(paginator.num_pages, current_page_num + 2) + 1))

    if page_range[0]-1>=2:
        page_range.insert(0,'...')
    if page_range[-1]+2<=paginator.num_pages:
        page_range.append('...')

    if page_range[0]!=1:
        page_range.insert(0,1)
    if page_range[-1]!=paginator.page_range:
        page_range.append(paginator.num_pages)
    context={}
    context['store']=page_of_stores.object_list
    context['page_of_stores']=page_of_stores
    context['page_range']=page_range
    return render(request,'final-web/shops.html',context)
    #return render(request,'final_web/index.html')
    
