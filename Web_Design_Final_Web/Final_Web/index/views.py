from django.shortcuts import render
from .models import Store
from login.models import Users
from django.views import generic
# Create your views here.

#可以連上首頁而已
def index(request):
    return render(request,'final-web/index.html')


#store 這邊要爬資料，讓每個店家有自己的頁面
#目前未完成
class store(generic.DetailView):
    model = Store
    template_name='final-web/store.html'
    pk=Store.store_name
    def get_queryset(self):
        return Store.objects.all()
    #return render(request,'final-web/store.html')

def shops(request):
    #爬每個店家的資料放到列表上
    stores=Store.objects.all()
    return render(request,'final-web/shops.html',{'stores':stores})
    #return render(request,'final_web/index.html')
    
