
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path("createdepartment", views.home, name="home"),
    path("departments", views.departments, name="departments"),
    path("removedepartment/<int:id>", views.removedepartment, name="removedepartment"),
    path("employeedata", views.employee, name="employeedata"),
    path("employeedetails", views.employeedetails, name="employeedetails"),
    path("searchemployee", views.searchemployee, name="searchemployee"),
    path("removeemployee/<int:id>", views.removeemployee, name="removeemployee"),
    path("searchbydate", views.searchbydate, name="searchbydate")
]
