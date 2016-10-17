from django.shortcuts import render,RequestContext
#from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

from .forms import EnterSentiForm

def index(request):
    form=EnterSentiForm(request.POST or None)
    if form.is_valid():
        save_it=form.save(commit=False)
        save_it.save()
    return render_to_response('display.html',locals(),context_instance=RequestContext(request))


'''def index(request) :  
    c={}
    c.update(csrf(request))
    return render_to_response('display2.html',c)'''

