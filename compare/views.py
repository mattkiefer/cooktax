# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response
from django.core.urlresolvers import reverse
from compare.models import Property
from compare.forms import PinLookup

def lookup(request,pin):
    home = Property.objects.filter(pin=pin)
    return render_to_response('compare/lookup.html',{'object_list':home})

def comps(request,pin):
    home = Property.objects.get(pin=pin)
    n = home.nbhd
    bc = home.bldg_cls
    t = home.town
    comps = Property.objects.filter(bldg_cls=bc,nbhd=n,town=t)
    comps = compSort(comps)
    return render_to_response('compare/comps.html',{'object_list':comps,'home':home})

def lookup2(request):
    form = PinLookup(request.GET)
    if form.is_bound:
        if form.is_valid():
            cd = form.cleaned_data
            home = getHome(cd['pin'])
	    comps = comps2(home)
            #import pdb; pdb.set_trace()
	    return render_to_response('compare/comps2.html',{'object_list':comps,'home':home})
        else:
            return render_to_response('compare/lookup2.html',{'form':form}) # should return a response with form html
    else:
        return render_to_response('compare/lookup2.html',{'form':form}) # should return a response with form html

def getHome(pin):
    return Property.objects.get(pin=pin)

def comps2(home):
    n = home.nbhd
    bc = home.bldg_cls
    t = home.town
    return compSort(Property.objects.filter(bldg_cls=bc,nbhd=n,town=t))

    

def compSort(comps): 
    """a sorting function that will go away
    once we get this derivation on the model"""
    scomps = sorted(list(comps), key = lambda x: x.quo_cmv_bsf)[:10]
    return scomps
