from django.contrib import admin
from web.models import Testimonial, Promoter

# for showing datas on admin
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',  'designation', 'description')

admin.site.register(Testimonial, TestimonialAdmin)


class PromoterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',  'image')
    
admin.site.register(Promoter, PromoterAdmin)
