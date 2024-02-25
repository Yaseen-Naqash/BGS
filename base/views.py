from django.db.models import Q
from django.shortcuts import render
from .models import Deal,Topic

# Create your views here.
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    deals = Deal.objects.filter(Q(stock__topics__name__icontains=q)).distinct()
    topics = Topic.objects.all()


    context = {'deals':deals,'topics':topics}
    return render(request,'base/home.html',context)
