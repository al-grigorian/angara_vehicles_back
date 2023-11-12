from django.shortcuts import render
from django.shortcuts import render  
from .models import * 

# Create your views here.

def GetOptions(request):
    input_text = request.GET.get('rocketcopm')
    options=Components.objects.all()
    #context={'vars': options}
    if input_text:
        filtered_options = Components.objects.filter(category__icontains=input_text)
        #context = {'vars': filtered_options, 'find': input_text}
        return render(request, 'main_page.html', {'data' : {
        'result': filtered_options, 'find': input_text
    }})
    else:
        return render(request, 'main_page.html', {'data' : {
        'result': options
    }})

def GetOption(request, id):
    result = Components.objects.get(id=id)
    return render(request, 'rocket_page.html', {'data' : {
        'result': result
    }})