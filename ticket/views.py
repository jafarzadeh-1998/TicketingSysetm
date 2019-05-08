from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate,login ,logout ,mixins
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.shortcuts import get_object_or_404 ,reverse
from django.utils import timezone

from . import models
from . import forms


def MyLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse('ticket:home'))
        else:
            return render(request, 'ticket/login_page.html', {})
    return render(request, 'ticket/login_page.html', {})


def signup(request):
    if request.method == 'POST':
        form_signup = forms.signup_form(request.POST,auto_id=False)
        if form_signup.is_valid():
            username=form_signup.cleaned_data['username']
            password=form_signup.cleaned_data['password']
            user = User.objects.create_user(username=username,password=password)
            user.save()
    return HttpResponseRedirect(reverse('ticket:login'))

def MyLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('ticket:home'))

class Index(generic.TemplateView):
    template_name = 'ticket/index.html'

class TicketList(mixins.LoginRequiredMixin ,generic.ListView):
    model = models.Ticket
    template_name = "ticket/ticket_list.html"

    login_url = '/login/'
    redirect_field_name = 'ticket_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_superuser:
            context['ticket_list'] = models.Ticket.objects.all()
        else:
            context['ticket_list'] = models.Ticket.objects.all().filter(user = self.request.user)
        return context

class TicketDetail(mixins.LoginRequiredMixin ,generic.DetailView):
    model = models.Ticket
    template_name = "ticket/ticket_detail.html"

    login_url = '/login/'
    redirect_field_name = "/detail/"+str(model.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["creatMassegForm"] = forms.message_form
        return context

class CreateMessage(mixins.LoginRequiredMixin ,generic.TemplateView):
    template_name = 'ticket/create_message.html'
    http_method_names = ['get' ,'post']
    
    def post(self ,request ,*args, **kwargs):
        mess = request.POST['message']
        pk = int(kwargs['pk'])
        if mess:
            m = models.TicketMessage(message=mess ,
                                     ticket = get_object_or_404(models.Ticket, pk = pk))
                                    #  pub_date = timezone.now)
            m.save()
            return HttpResponseRedirect(reverse('ticket:ticket-detail', args=[pk]))
        else:
            return HttpResponseRedirect(reverse('ticket:new_message' ,args=[pk]))

class CreateTicket(mixins.LoginRequiredMixin ,generic.TemplateView):
    template_name = 'ticket/create_ticket.html'
    http_method_names = ['post' ,'get']

    login_url = '/login/'
    redirect_field_name = '/create_ticket'

    def post(self, request, *args, **kwargs):
        title = request.POST['title']
        if title:
            ticket=models.Ticket(title=title ,user=request.user)
            ticket.save()
            return HttpResponseRedirect(reverse('ticket:ticket-list'))
        else:
            return HttpResponseRedirect(reverse('ticket:new-ticket'))

class ReplyList(generic.TemplateView):
    template_name = 'ticket/reply_list.html'
    context = {"message_list" :models.TicketMessage.objects.all().filter(reply="")}
    
    def get(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return render(request ,self.template_name ,{})
        else:      
            return render(request ,self.template_name ,self.context)
    
class Reply(generic.TemplateView):
    template_name = 'ticket/reply.html'
    http_method_name = ['post' ,'get']

    def post(self ,request ,*args, **kwargs):
        rep = request.POST['reply']
        PK = int(kwargs['pk'])
        TM = models.TicketMessage.objects.all().filter(pk=PK)[0]
        if rep:
            TM.reply = rep
            TM.save()
        else:
            return HttpResponseRedirect(request.path)
        return HttpResponseRedirect(reverse('ticket:reply-list'))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ticketMessage"] = models.TicketMessage.objects.all().filter(pk=int(kwargs['pk']))[0]
        return context
    