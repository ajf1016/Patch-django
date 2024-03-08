from django.contrib import admin
from web.models import Testimonial


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name',  'designation','description')
    # for showing datas on admin 
    
admin.site.register(Testimonial,TestimonialAdmin)
