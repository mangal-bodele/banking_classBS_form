from django.shortcuts import render,redirect
from .models import Banking
from .forms import BankingForm
from django.views import View


class Create_Banking(View):
    def get(self, request):
        template_name = 'crud_app/create.html'
        form = BankingForm()
        context = {'form':form}
        return render(request, template_name, context)

    def post(self, request):
        form = BankingForm()
        if request.method == "POST":
            form = BankingForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('show_url')


class Show_Banking(View):
    def get(self,request):
        template_name = 'crud_app/show.html'
        bankings = Banking.objects.all()
        context = {'bankings':bankings}
        return render(request, template_name, context)

class Update_Banking(View):
    def get(self,request,pk):
        template_name = 'crud_app/create.html'
        obj = Banking.objects.get(id=pk)
        form = BankingForm(instance=obj)
        context = {'form':form}
        return render(request, template_name, context)

    def post(self,request,pk):
        template_name = 'crud_app/create.html'
        obj = Banking.objects.get(id=pk)
        form = BankingForm(instance=obj)
        if request.method == "POST":
            form = BankingForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                return redirect('show_url')
        context = {'form': form}
        return render(request, template_name, context)


class Delete_Banking(View):
    def get(self, request, pk):
        obj = Banking.objects.get(id=pk)
        template_name = 'crud_app/confirm.html'
        return render(request, template_name)

    def post(self, request, pk):
        obj = Banking.objects.get(id=pk)
        template_name = 'crud_app/confirm.html'
        if request.method == "POST":
            obj.delete()
            return redirect('show_url')
        return render(request, template_name)

