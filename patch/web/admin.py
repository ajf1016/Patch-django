from django.contrib import admin
from web.models import Testimonials


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Description', 'Designation')
    # for showing datas on admin 
    
admin.site.register(Testimonials,TestimonialAdmin)
