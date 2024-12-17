from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponse
from django.views.generic import ListView, TemplateView, DetailView     #LIST VIEW ES UNA CLASE QUE CREA UNA LISTA GENERICA. ESTA LA PUEDO MODIFICAR SEGUN MIS NECESIDADES. TEMPLATE VIEW ES UNA VISTA GENERICA QUE NO NECESITA DE MODELOS ESPECIFICOS. DETAILVIEW ES UNA VISTA OPTIMIZADA PARA MOSTRAR UN UNICO "ALGO" 

from blog.models import User, Post, Comment

# Create your views here.

class BienvenidoView(TemplateView):    #ESTA DEBE SER TEMPLATE VIEW
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mensaje'] = 'BIENVENIDO AL BLOG DEL ROCK'
        context['descripcion'] = 'Este es un blog creado con Django. Explora las secciones para encontrar más información.'
        context['creador'] = 'crisrock'
        return context



class UserListView(ListView):
    model = User
    template_name = 'user.html'

    context_object_name = 'usuarios'    # NUEVO NOMBRE DEL DICCIONARIO CONTEXTO, DONDE SE ALMACENAN LAS VARIABLES DE LA CLASE EN LOS MODELOS ESTABLECIDOS

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mensaje'] = 'USUARIOS DEL BLOG'
        context['descripcion'] = 'Usuarios actualmente registrados'
        context['creador'] = 'crisrock'
        return context
    


class UserDetailView(DetailView):
    model = User
    template_name = 'userdetail.html'
    context_object_name = 'usuario'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mensaje'] = 'USUARIO'
        context['descripcion'] = 'Detalles de usuario'
        context['posts'] = self.object.post_set.all()    #ACA AGREGO TODOS LOS POST QUE HA INGRESADO
        context['creador'] = 'crisrock'
        return context



class PostListView(ListView):
    model = Post
    template_name = 'post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mensaje'] = 'ENTRADAS DE BLOG'
        context['descripcion'] = 'Navega por las entradas del blog'
        context['creador'] = 'crisrock'
        return context
        


class PostDetailView(DetailView):
    model = Post
    template_name = 'postdetail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(autor=self.object.autor)  # Obtener posts del usuario
        return context



class CommentListView(ListView):
    model = Comment
    template_name = 'comment.html'

