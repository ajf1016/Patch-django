import json
from django.shortcuts import render,redirect
from web.models import Testimonial, Promoter, Faq,Subscribe
from django.urls import reverse
from django.http.response import HttpResponse


def index(request):
    testimonials = Testimonial.objects.all()
    promoters = Promoter.objects.all()
    rent_tracking_faqs = Faq.objects.filter(faq_type="rent_tracking")
    new_deposite_faqs = Faq.objects.filter(faq_type="new_deposite")
    existing_deposite_faqs = Faq.objects.filter(faq_type="existing_deposite")

    context = {
        'testimonials': testimonials,
        'promoters': promoters,
        'rent_tracking_faqs': rent_tracking_faqs,
        'new_deposite_faqs': new_deposite_faqs,
        'existing_deposite_faqs': existing_deposite_faqs,
    }
    return render(request, "index.html", context=context)


def subcribe(request):
    email = request.POST.get('email')
    if not Subscribe.objects.filter(email = email).exists():
        Subscribe.objects.create(
            email = email,
        )
        
        response_data = {
            "status": "success",
            "message": "You have successfully subscribed to our newsletter."
        }
    else:
        response_data = {
            "status": "Success",
            "message": "You already have a subscription to our newsletter"
        }
    
    # return redirect(reverse('web:home'))
    return HttpResponse(json.dumps(response_data),content_type="application/json")
