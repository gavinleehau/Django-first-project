from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Reporter,Article
# from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from .forms import ReporterForm

class ReportListView(ListView):
	model = Reporter
	context_object_name = "all_reporters" #đổi object_list thành "all_reporters"
	# đổi teample qua template_name
	template_name = "class_base/list_view.html"
	paginate_by = 3

@method_decorator(login_required(login_url="/login"),name="dispatch")
class ReportDetailView(DetailView):
	model = Reporter
	context_object_name = "view_reporter"

@method_decorator(login_required(login_url="/login"),name="dispatch")
class ReporterCreateView(CreateView):
	model = Reporter
	fields = "__all__"
	# form_class = ReporterForm
	template_name = "class_base/create_view.html"
	success_url="/all-reporter"

@method_decorator(login_required(login_url="/login"),name="dispatch")
class ReporterUpdateView(UpdateView):
	model = Reporter
	# fields = "__all__"
	form_class = ReporterForm
	template_name = "class_base/update_view.html"
	success_url="/all-reporter"

@method_decorator(login_required(login_url="/login"),name="dispatch")
class ReporterDeleteView(DeleteView):
	model = Reporter
	# fields = "__all__"
	form_class = ReporterForm
	template_name = "class_base/confirm_delete.html"
	success_url="/all-reporter"







