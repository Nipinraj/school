
from django.urls import path
from . import views



urlpatterns = [
    path('',views.depart),
    path('student/',views.stu),
    path('student/addstudent/',views.addstu),
    path('student/viewstudent/',views.viewstu),

    path('teacher/',views.teach),
    path('teacher/addteacher/',views.addteach),
    path('teacher/viewteacher/',views.viewteach),

    path('editstudent/',views.editstu),
    path('editteacher/',views.editteacher),

    # path('',views.hom)


]