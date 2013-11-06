# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response
from compare.models import Property


def foo(request):
    # return render_to_response(print 'hello world!')
    property = Property.objects.all()
    return render_to_response('compare/foo.html',{'object_list':property})
    print 'property'
