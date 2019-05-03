from django.shortcuts import render,HttpResponse,loader,HttpResponseRedirect
from  . import  models

# Create your views here.

#
# def hom(request):
#     t=loader.get_template('firstpage.html')
#     return HttpResponse(t.render({},request))
def depart(request):
    t=loader.get_template('firstpage.html')
    return HttpResponse(t.render({},request))
    # return  HttpResponse('welcom to our class')
def stu(request):
    t=loader.get_template('student.html')
    return  HttpResponse(t.render({},request))
def addstu(request):
    t=loader.get_template('addstudent.html')
    msg=''
    if request.method=="POST":
        a=models.students()
        a.name=request.POST.get('nam')
        a.clas = request.POST.get('clas')
        a.age = request.POST.get('ag')
        a.place = request.POST.get('plac')
        a.mobile = request.POST.get('mobil')
        a.save()
        msg='Add success'
    return HttpResponse(t.render({'msgs':msg},request))

def viewstu(request):
    t=loader.get_template('viewstudent.html')
    dis=''
    dis = models.students.objects.all()
    if request.method=="POST":
        d=models.students.objects.get(id=request.POST.get('cid'))
        d.delete()

    return HttpResponse(t.render({'disu':dis},request))

def editstu(request):
    a=loader.get_template('editstudent.html')
    edi=''
    if request.method=="POST" and 'stuedit' in request.POST:

        s=models.students.objects.get(id=request.POST.get('stuedit'))
        s.name = request.POST.get('nam')
        s.clas = request.POST.get('clas')
        s.age = request.POST.get('ag')
        s.place = request.POST.get('plac')
        s.mobile = request.POST.get('mobil')
        s.save()
        edi='Edit success '
        return HttpResponseRedirect ('/student/viewstudent/')
    e=models.students.objects.get(id=request.POST.get('cc'))
    return HttpResponse(a.render({'edi':e},request))




def teach(request):
    t=loader.get_template('teacher.html')

    return  HttpResponse(t.render({},request))

def addteach(request):
    t=loader.get_template('addteacher.html')
    msg=''
    if request.method == "POST":
        a = models.teachers()
        a.name = request.POST.get('nam')
        a.department= request.POST.get('departmen')
        a.age = request.POST.get('ag')
        a.place = request.POST.get('plac')
        a.mobile = request.POST.get('mobil')
        a.save()
        msg='teacher add success'

    return HttpResponse(t.render({'msgs':msg},request))
def viewteach(request):
    t=loader.get_template('viewteacher.html')
    dis = ''
    dis = models.teachers.objects.all()
    if request.method == "POST":
        d = models.teachers.objects.get(id=request.POST.get('mid'))
        d.delete()

    return HttpResponse(t.render({'diss':dis},request))

def editteacher(request):
    d=loader.get_template('editteacher.html')
    edt=''
    if request.method=="POST" and 'tedit' in request.POST:
        k=models.teachers.objects.get(id=request.POST.get('tedit'))
        k.name = request.POST.get('nam')
        k.department = request.POST.get('departmen')
        k.age = request.POST.get('ag')
        k.place = request.POST.get('plac')
        k.mobile = request.POST.get('mobil')
        k.save()
        edt='edit success'
        return HttpResponseRedirect('/teacher/viewteacher/')
    e=models.teachers.objects.get(id=request.POST.get('ddc'))

    return HttpResponse(d.render({'edt':e},request))
