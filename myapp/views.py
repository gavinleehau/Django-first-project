# from django.core.exceptions import RequestDataTooBig
# from django.utils import html
# from myapp.forms import ReporterForm
from django.db import reset_queries
from django.db.models.manager import EmptyManager
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http.response import JsonResponse
from .models import Reporter, Article
import time
from .forms import ReporterForm, ArticleForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.db.models import Q
import json

# from .models import Post


# Create your views here.

def index(request):
# 	print(request.GET['name'])
# 	name = request.GET.get('name','')
# 	request.session['name'] = name
# 	response = HttpResponse()
# 	response.write("<h1> Hello From Django Web </h1>")
# 	response.write(" Đây là app đầu tiên ")
# 	return response
	

	all_reporters = Reporter.objects.all()

	return render(
		request=request,
		template_name="index.html",
		context={
			'all_reporters': all_reporters
		}
	)

@login_required(login_url="/login")
def add_reporter(request):
	reporter_form = ReporterForm()
	if request.method == "POST":
		print(request.POST)
		reporter_form = ReporterForm(request.POST)
		if reporter_form.is_valid():
			print(" Luu thanh cong ")
			# data = reporter_form.cleaned_data
			reporter_form.save()
			return redirect("index")
	
	return render(
		request = request,
		template_name='reporter/add.html',
		context={
			'form': reporter_form
		}
	)

@login_required(login_url="/login")
def add_article(request):
	article_form = ArticleForm()
	if request.method == "POST":
		print(request.POST)
		article_form = ArticleForm(request.POST)
		if article_form.is_valid():
			print(" Luu thanh cong ")
			# data = reporter_form.cleaned_data
			article_form.save()
			return redirect("index")
	
	return render(
		request = request,
		template_name='article/add.html',
		context={
			'form': article_form
		}
	)


# thứ tự tạo mới 1 hàm:
# b1: viết hàm. chọn template

# @login_required(login_url="/login")
def list_reporters(request):
	all_reporters= Reporter.objects.all()
	search = request.GET.get('search')
	paginate_by = 2
	if search:
		all_reporters = Reporter.objects.filter(Q(first_name__icontains=search) | Q(last_name__icontains=search))
		# Q để sệch hai bên
	# time.sleep(3)	
	return render(
		request=request,
		template_name="reporter/list.html",
		context={
			'all_reporters': all_reporters
		}
	)
	
	
# def search_reporter(request):
# 	search=request.GET['search']
# 	if search:
# 		all_reporters = Reporter.objects.filter(Q(first_name__icontains=search), Q(last_name__icontains=search))
# 	else:
# 		all_reporters=[]
	
# 	return JsonRespone({
# 		"status":200,
# 		"message":"all_reporters"
# 	})




def view_detail_reporter(request, reporter_id):
	reporter_data = Reporter.objects.get(id = reporter_id)
	return render(
		request=request,
		template_name="reporter/detail.html",
		context={
			'reporter': reporter_data
		}
	)



# def post_create(request):
# 	form = PostForm
# 	context = {
# 		"form": form,
# 	}

# def post_detail(request, id=None):
# 	instance=get_object_or_404(Post, id=id)
# 	context={
# 		"title": instance.title,
# 		"instance": instance,
# 	}
# 	return render(request, "post_detail.html", context)

# def post_list(request):
# 	queryset=Post.objects.all()
# 	context={
# 		"object_list": queryset,
# 		"title": "List"
# 	}