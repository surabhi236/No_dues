#!python
# log/views.py
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template import loader
from .models import Library, CC, Gymkhana, Csedept, Umiamhostel, Dhansarihostel, Subhansrihostel

from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.)
# this login required decorator is to not allow to any
# view without authenticating
@login_required(login_url="login/")
def home(request):
    return render(request, "home.html")


def library(request):
    library_list = Library.objects.all()
    template = loader.get_template('log/library.html')
    context = {'library_list': library_list, }
    return render(request, 'log/library.html', context)


def clearLibrary(request):
    library_list = Library.objects.all()
    if 'clear' in request.POST:
        selected_student = Library.objects.get(pk=request.POST['student'])
        selected_student.clear = True
        selected_student.save()
        template = loader.get_template('log/library.html')

    if 'deselect' in request.POST:
        selected_student = Library.objects.get(pk=request.POST['student'])
        selected_student.clear = False
        selected_student.save()
        template = loader.get_template('log/library.html')

    if 'clearall' in request.POST:
        for student in library_list:
            student.clear = True
            student.save()

    context = {'library_list': library_list, }
    return render(request, 'log/library.html', context)
#
def cc(request):
    cc_list = CC.objects.all()
    template = loader.get_template('log/cc.html')
    context = {'cc_list': cc_list, }
    return render(request, 'log/cc.html', context)


def clearcc(request):
    cc_list = CC.objects.all()
    if 'clear' in request.POST:
        selected_student = CC.objects.get(pk=request.POST['student'])
        selected_student.clear = True
        selected_student.save()
        template = loader.get_template('log/cc.html')

    if 'deselect' in request.POST:
        selected_student = CC.objects.get(pk=request.POST['student'])
        selected_student.clear = False
        selected_student.save()
        template = loader.get_template('log/cc.html')

    if 'clearall' in request.POST:
        for student in cc_list:
            student.clear = True
            student.save()

    context = {'cc_list': cc_list, }
    return render(request, 'log/cc.html', context)


#
def gymkhana(request):
    gymkhana_list = Gymkhana.objects.all()
    template = loader.get_template('log/library.html')
    context = {'gymkhana_list': gymkhana_list, }
    return render(request, 'log/gymkhana.html', context)


def cleargymkhana(request):
    gymkhana_list = Gymkhana.objects.all()
    if 'clear' in request.POST:
        selected_student = Gymkhana.objects.get(pk=request.POST['student'])
        selected_student.clear = True
        selected_student.save()
        template = loader.get_template('log/library.html')

    if 'deselect' in request.POST:
        selected_student = Gymkhana.objects.get(pk=request.POST['student'])
        selected_student.clear = False
        selected_student.save()
        template = loader.get_template('log/library.html')

    if 'clearall' in request.POST:
        for student in gymkhana_list:
            student.clear = True
            student.save()

    context = {'gymkhana_list': gymkhana_list, }
    return render(request, 'log/gymkhana.html', context)


def csedept(request):
    csedept_list = Csedept.objects.all()
    template = loader.get_template('log/library.html')
    context = {'csedept_list': csedept_list, }
    return render(request, 'log/csedept.html', context)


def clearcsedept(request):
    csedept_list = Csedept.objects.all()
    if 'clear' in request.POST:
        selected_student = Csedept.objects.get(pk=request.POST['student'])
        selected_student.clear = True
        selected_student.save()
        #template = loader.get_template('log/library.html')

    if 'deselect' in request.POST:
        selected_student = Csedept.objects.get(pk=request.POST['student'])
        selected_student.clear = False
        selected_student.save()
        #template = loader.get_template('log/library.html')

    if 'clearall' in request.POST:
        for student in csedept_list:
            student.clear = True
            student.save()

    context = {'csedept_list': csedept_list, }
    return render(request, 'log/csedept.html', context)


def umiamhostel(request):
    umiamhostel_list = Umiamhostel.objects.all()
    # template = loader.get_template('log/library.html')
    context = {'umiamhostel_list': umiamhostel_list, }
    return render(request, 'log/umiamhostel.html', context)


def clearumiamhostel(request):
    umiamhostel_list = Umiamhostel.objects.all()
    if 'clear' in request.POST:
        selected_student = Umiamhostel.objects.get(pk=request.POST['student'])
        selected_student.clear = True
        selected_student.save()
        #template = loader.get_template('log/library.html')

    if 'deselect' in request.POST:
        selected_student = Umiamhostel.objects.get(pk=request.POST['student'])
        selected_student.clear = False
        selected_student.save()
        #template = loader.get_template('log/library.html')

    if 'clearall' in request.POST:
        for student in umiamhostel_list:
            student.clear = True
            student.save()

    context = {'umiamhostel_list': umiamhostel_list, }
    return render(request, 'log/umiamhostel.html', context)


def dhansarihostel(request):
    dhansarihostel_list = Dhansarihostel.objects.all()
    # template = loader.get_template('log/dhansarihostel.html')
    context = {'dhansarihostel_list': dhansarihostel_list, }
    return render(request, 'log/dhansarihostel.html', context)


def cleardhansarihostel(request):
    dhansarihostel_list = Dhansarihostel.objects.all()
    if 'clear' in request.POST:
        selected_student = Dhansarihostel.objects.get(pk=request.POST['student'])
        selected_student.clear = True
        selected_student.save()
        #template = loader.get_template('log/library.html')

    if 'deselect' in request.POST:
        selected_student = Dhansarihostel.objects.get(pk=request.POST['student'])
        selected_student.clear = False
        selected_student.save()
        #template = loader.get_template('log/library.html')

    if 'clearall' in request.POST:
        for student in dhansarihostel_list:
            student.clear = True
            student.save()

    context = {'dhansarihostel_list': dhansarihostel_list, }
    return render(request, 'log/dhansarihostel.html', context)


#
def subhansrihostel(request):
    subhansrihostel_list = Subhansrihostel.objects.all()
    # template = loader.get_template('log/library.html')
    context = {'subhansrihostel_list': subhansrihostel_list, }
    return render(request, 'log/subhansrihostel.html', context)


def clearsubhansrihostel(request):
    subhansrihostel_list = Subhansrihostel.objects.all()
    if 'clear' in request.POST:
        selected_student = Subhansrihostel.objects.get(pk=request.POST['student'])
        selected_student.clear = True
        selected_student.save()
        template = loader.get_template('log/subhansrihostel.html')

    if 'deselect' in request.POST:
        selected_student = Subhansrihostel.objects.get(pk=request.POST['student'])
        selected_student.clear = False
        selected_student.save()
        template = loader.get_template('log/subhansrihostel.html')

    if 'clearall' in request.POST:
        for student in subhansrihostel_list:
            student.clear = True
            student.save()

    context = {'subhansrihostel_list': subhansrihostel_list, }
    return render(request, 'log/subhansrihostel.html', context)

def student(request):
    library_list = Library.objects.all()
    cc_list = CC.objects.all()
    csedept_list = Csedept.objects.all()
    gymkhana_list = Gymkhana.objects.all()
    umiamhostel_list = Umiamhostel.objects.all()
    dhansarihostel_list = Dhansarihostel.objects.all()
    subhansrihostel_list = Subhansrihostel.objects.all()
    context = {'library_list': library_list,'cc_list':cc_list ,'csedept_list':csedept_list ,'gymkhana_list' : gymkhana_list,
               'umiamhostel_list':umiamhostel_list ,'dhansarihostel_list': dhansarihostel_list , 'subhansrihostel_list':subhansrihostel_list,}
    return render(request, 'log/student.html', context)

