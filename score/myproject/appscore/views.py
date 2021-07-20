from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from appscore import forms
from appscore import models
def vw_Question(request):
    q=models.Mdl_Question.objects.all()
    form=forms.frm_Answer(request.POST or None)
    if request.POST:
        model=form.save()
        model.save()
        return HttpResponseRedirect("/")
    else:
        form=forms.frm_Answer()   
    return render(request,'home.html',{"form":form,"q":q},)      

