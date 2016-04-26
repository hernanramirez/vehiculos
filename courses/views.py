from django.core.urlresolvers import reverse_lazy

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Course


class CourseList(ListView):
    model = Course


class CourseDetail(DetailView):
    model = Course


class CourseCreation(CreateView):
    model = Course
    success_url = reverse_lazy('courses:list')
    fields = ['course_type', 'name', 'start_date', 'end_date']


class CourseUpdate(UpdateView):
    model = Course
    success_url = reverse_lazy('courses:list')
    fields = ['course_type', 'name', 'start_date', 'end_date']


class CourseDelete(DeleteView):
    model = Course
    success_url = reverse_lazy('courses:list')
