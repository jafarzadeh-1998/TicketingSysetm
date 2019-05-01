from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.shortcuts import get_object_or_404

from . import models
from . import forms


def loginu(request):
    if request.method == 'POST':
        form_login = forms.login_form(request.POST,auto_id=False)
        if form_login.is_valid():
            username=form_login.cleaned_data['username']
            password=form_login.cleaned_data['password']
            user = authenticate(request,username=username, password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('dashboard')
            else:
                form_login = forms.login_form(auto_id=False)
                form_signup = forms.signup_form(auto_id=False)
                return render(request, 'index/index.html', {'form1': form_login,'form2': form_signup})

    form_login = forms.login_form(auto_id=False)
    form_signup = forms.signup_form(auto_id=False)
    return render(request, 'index/index.html', {'form1': form_login,'form2': form_signup})


def signin(request):
    if request.method == 'POST':
        form_signup = forms.signup_form(request.POST,auto_id=False)
        if form_signup.is_valid():
            username=form_signup.cleaned_data['username']
            password=form_signup.cleaned_data['password']
            user = User.objects.create_user(username=username,password=password)
            user.save()
    form_login = forms.login_form(auto_id=False)
    form_signup = forms.signup_form(auto_id=False)
    return render(request, 'index/index.html', {'form1': form_login,'form2': form_signup})


# def dashboard(request):


#     print(request.user)
#     if(request.user.is_authenticated):
#         if request.method == 'POST':
#             mf= message_form(request.POST,auto_id=False)
#             if mf.is_valid():
#                 mess=mf.cleaned_data['message']
#                 t=Ticket(title=mess,user=request.user.username)
#                 print(request.user.username)
#                 t.save()    
#         lst=Ticket.objects.all()
#         mf= message_form(auto_id=False)
#         return render(request, 'dashboard/index.html',{'list1':lst,'form':mf} )
#     else:
#         return HttpResponseRedirect('/ticket')

class TicketList(generic.ListView):
    model = models.Ticket
    template_name = "dashboard/ticket_list.html"

class TicketDetail(generic.DetailView):
    model = models.Ticket
    template_name = "dashboard/ticket_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["creatMassegForm"] = forms.message_form
        return context

def createMassage(request ,pk):
    if request.method == 'POST':
        mf= forms.message_form(request.POST,auto_id=False)
        if mf.is_valid():
            mess=mf.cleaned_data['message']
            m=models.TicketMessage(message=mess ,ticket= get_object_or_404(models.Ticket, pk = pk))
            m.save()
        return HttpResponseRedirect('/ticket/detail/'+str(pk))


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['ticket_list'] = Ticket.objects.all()
    #     return context
