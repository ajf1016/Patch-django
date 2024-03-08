from django.shortcuts import render
from web.models import Testimonial

def index(request):
    testimonial = Testimonial.objects.all()
    context = {
        'testimonial': testimonial
    }
    return render(request,"index.html",context=context)