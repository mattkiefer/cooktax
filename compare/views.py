# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response
from compare.models import Property


def lookup(request,pin):
    home = Property.objects.filter(pin=pin)
    return render_to_response('compare/lookup.html',{'object_list':home})

def comps(request,pin):
    home = Property.objects.get(pin=pin)
    n = home.nbhd
    bc = home.bldg_cls
    t = home.town
    comps = Property.objects.filter(bldg_cls=bc,nbhd=n,town=t)
    comps = sort(comps)
    return render_to_response('compare/comps.html',{'object_list':comps,'home':home})

def sort(comps): 
    """a sorting function that will go away
    once we get this derivation on the model"""
    scomps = sorted(list(comps), key = lambda x: x.quo_cmv_bsf)[:10]
    return scomps
