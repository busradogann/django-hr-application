from django.views.generic import ListView, DetailView, FormView, CreateView
from django.views.generic.edit import FormMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from main.forms import ApplicationForm
from main.models import Job, Application


class JobsList(ListView):
    model = Job
    template_name = 'job_list.html'


class JobDetail(FormMixin, DetailView):
    model = Job
    form_class = ApplicationForm
    success_url = '/application-done/'
    template_name = 'job_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        application = form.save(commit=False)
        application.job = self.object
        application.save()
        return super().form_valid(form)


class ManagerJobCreate(FormView):
    model = Job
    form_class = JobForm
    success_url = '/'
    template_name = 'create_job.html'


class ManagerApplicationList(ListView):
    model = Application
    template_name = 'applications.html'


class ManagerApplicationDetail(DetailView):
    model = Application
    template_name = 'application.html'


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
