from django.contrib import admin
from web.models import Testimonial, Promoter


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',  'designation', 'description')
    # for showing datas on admin


admin.site.register(Testimonial, TestimonialAdmin)


class PromoterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',  'image')
    # for showing datas on admin


admin.site.register(Promoter, PromoterAdmin)
