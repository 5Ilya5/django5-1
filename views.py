from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Person
 
# получение данных из бд
def index(request):
    people = Person.objects.all()
    return render(request, "index.html", {"people": people})
 
# сохранение данных в бд
def create(request):
    if request.method == "POST":
        person = Person()
        person.name = request.POST.get("name")
        person.age = request.POST.get("age")
        person.save()
    return HttpResponseRedirect("/")
 
# изменение данных в бд
def edit(request, id):
    try:
        person = Person.objects.get(id=id)
 
        if request.method == "POST":
            person.name = request.POST.get("name")
            person.age = request.POST.get("age")
            person.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"person": person})
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")
     
# удаление данных из бд
def delete(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")

        def profile(request):
        user_orders = Order.objects.filter(user=request.user)
        user_order_item = OrderItem.objects.all()
    
        data = {
            'user_orders': user_orders,
            'user_order_item': user_order_item,
        }
        return render(request, 'store/main_pages/profile.html', data)
    
    from django.shortcuts import render
from .forms import GeeksForm

def home_view(request):
    context = {}
    context['form'] = GeeksForm()
    return render( request, "home.html", context)

from django.shortcuts import render
from .forms import GeeksForm
from .models import GeeksModel
 
def home_view(request):
    context = {}
    if request.method == "POST":
        form = GeeksForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            img = form.cleaned_data.get("geeks_field")
            obj = GeeksModel.objects.create(
                                 title = name,
                                 img = img
                                 )
            obj.save()
            print(obj)
    else:
        form = GeeksForm()
    context['form']= form
    return render(request, "home.html", context)

def landing(request):
    peopless = Peoples.objects.all()
    return render(request, 'landing/landing.html', locals())

class Peoples(models.Model):
    FIO = models.CharField(max_length=128)
    birthday = models.DateField()