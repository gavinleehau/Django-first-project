from django.contrib import admin
from django.db import reset_queries
# from .models import Python2104, Place, Restaurant, Reporter, Article, Publication, baiBao,Post
from .models import Reporter, Article

# class PostModelAdmin(admin.ModelAdmin):
# 	list_display = ["title","updated", "timestamp"]
# 	list_display_link = ["updated"]
# 	list_edittable =["title"]
# 	list_filter = ["updated", "timestamp"]
# 	class Meta:
# 		model = Post



# admin.site.register(Python2104)
# admin.site.register(Restaurant)
# admin.site.register(Place)
admin.site.register(Reporter)
admin.site.register(Article)
# admin.site.register(Publication)
# admin.site.register(baiBao)
# admin.site.register(Post, PostModelAdmin)
# admin.site.register(Post)

# Register your models here.
