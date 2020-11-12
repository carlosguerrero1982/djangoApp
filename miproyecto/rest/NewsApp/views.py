from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Blog,News
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django import forms
from django.forms import ModelForm
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.views.generic.edit import UpdateView 
from django.views.generic.edit import DeleteView 
from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import SingleObjectMixin
# Create your views here.

@login_required
def news(request):

    obj = News.objects.get(pk=1)

    context = {

       "data":obj

    }

    return render(request,'news.html',context)


def home(request):

    context = {

       "list":["python","java","c++","php"],
       "mynumb":50
    }


    return render(request,'home.html',context)

@login_required
def contact(request):
     return render(request,'contact.html')

class BlogList(ListView): 
  
    # specify the model for list view 
    model = Blog 
    context_object_name = 'blog_list'   # your own name for the list as a template variable
    template_name = 'blog_details.html' 
 
    
  
    def get_queryset(self, *args, **kwargs): 
        qs = super(BlogList, self).get_queryset(*args, **kwargs) 
        qs = qs.order_by("name") 
        return qs 

class BlogDetailView(DetailView): 
    # specify the model to use 
    model = Blog 
       # your own name for the list as a template variable
    template_name = 'Blog_detail.html' 


class BlogDetaileView(DetailView): 
    # specify the model to use 
    model = Blog 
      # your own name for the list as a template variable
    template_name = 'Blog_detail.html' 
    slug_field = 'name' # slug field

class Blogs(ListView):
    model = Blog
    template_name = 'blog_details.html'
    context_object_name = 'blog_list'

class BlogCreateForm(forms.ModelForm):
    class Meta:
        model = Blog  
        fields = ('name', 'tagline','pub_date')
        success_url = "/"

class BlogCreateView(CreateView):
    template_name = 'blog-create.html'
    form_class = BlogCreateForm

    def get_absolute_url(self): # new
        return reverse('/blogs', args=[str(self.id)])
    
class BlogUpdateView(UpdateView): 
    # specify the model you want to use 
    model = Blog 
  
    # specify the fields 
    fields = [ 
        "name", 
        "tagline",
        "pub_date"
    ] 
  
    # can specify success url 
    # url to redirect after successfully 
    # updating details 
    success_url ="/"

class BlogDeleteView(DeleteView): 
    # specify the model you want to use 
    model = Blog 
      
    # can specify success url 
    # url to redirect after sucessfully 
    # deleting object 
    success_url ="/"

def welcome(request):
     if request.user.is_authenticated:
            return render(request, "welcome.html")
    # En otro caso redireccionamos al login
     return redirect('/login')
        

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = UserCreationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():

            # Creamos la nueva cuenta de usuario
            user = form.save()

            # Si el usuario se crea correctamente 
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/home')

    # Si llegamos al final renderizamos el formulario
    return render(request, "register.html", {'form': form})

def login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/home')

    # Si llegamos al final renderizamos el formulario
    return render(request, "login.html", {'form': form})

def logout(request):
    # Redireccionamos a la portada
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('home/')


class BlogByUserListView(LoginRequiredMixin,ListView):
    
    model = Blog
    template_name ='Blog_detail.html'
    paginate_by = 5
    
    def get_queryset(self):
        return Blog.objects.filter(name=self.request.user).filter(name__exact='lito').order_by('pub_date')

class PublisherDetail(SingleObjectMixin, ListView):
    paginate_by = 10
    template_name = "publisher_detail.html"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Blog.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['publisher'] = self.object
        return context

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Blog.objects.all()
        else:
            return Blog.objects.filter(name="pepe")