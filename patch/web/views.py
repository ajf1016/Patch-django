from django.shortcuts import render
from web.models import Testimonial,Promoter

def index(request):
    testimonials = Testimonial.objects.all()
    promoters = Promoter.objects.all()
    
    print(promoters)
    
    context = {
        'testimonials': testimonials,
        'promoters' : promoters
    }
    return render(request,"index.html",context=context)