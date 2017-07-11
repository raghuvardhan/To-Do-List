from django.views.generic import *
from onlineapp.models import *
from django.contrib.auth.mixins import *
from django.urls import reverse_lazy

class CollegeView(ListView):
    model = College
    context_object_name = "colleges_list"

class CollegeViewLocation(ListView):
    model = College
    #slug_field = "location"
    context_object_name = "colleges_list"

    def get_queryset(self):
        return College.objects.filter("location")

class StudentViewId(DetailView):
    model = College
    slug_field = "id"

    def get_context_data(self, **kwargs):
        context = super(StudentViewId, self).get_context_data(**kwargs)
        college = context["college"]
        context["student"] = college.student_set.order_by("mocktest1")
        return context

class StudentViewAcronym(DetailView):
    model = College
    slug_field = "acronym"

    def get_context_data(self, **kwargs):
        context =  super(StudentViewAcronym, self).get_context_data(**kwargs)
        college = context["college"]
        context["student"] = college.student_set.order_by("mocktest1")
        return context

"""class StudentView(ListView):
    model = College
    slug_field = "location"

    def get_context_data(self,**kwargs):"""

class CreateCollegeView(LoginRequiredMixin,CreateView):
    model = College
    fields = ["name","location","acronym","contact"]
    success_url = reverse_lazy("colleges")

class UpdateCollegeView(LoginRequiredMixin,UpdateView):
    model = College
    fields = ["name","location","acronym","contact"]
    success_url = "../../../colleges/"

class DeleteCollegeView(DeleteView):
    model = College
    success_url = "../../../colleges/"
