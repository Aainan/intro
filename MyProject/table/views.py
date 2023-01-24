from django.shortcuts import render
from .models import Data

def index_view(request):
    datas = Data.objects.all()
    context = {
        'data': datas
    }
    return render(request, 'table/index.html', context)