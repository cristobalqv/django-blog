from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.TextField(max_length=5000)
    autor = models.ForeignKey(User,on_delete=models.CASCADE)   #CASCADE = SI SE ELIMINA AUTOR, SE ELIMINAN TODOS LOS POST
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class Comment(models.Model):
    contenido = models.TextField(max_length=1000)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    entrada_perteneciente = models.ForeignKey(Post, on_delete=models.CASCADE)
    fecha_comentario = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentario: "{self.contenido}". Autor: {self.autor}. En: "{self.entrada_perteneciente}"'





#EJEMPLO
# usuario1=User(username='cris', password='asdasdasd')

# post1 = Post.objects.create(titulo='primerpost',
#                             contenido="Este es el contenido del post.",
#                             autor=usuario1)

# comentario1 = Comment.objects.create(contenido="¡Qué buen post!",
#                                     autor=usuario1,
#                                     entrada_perteneciente=post1)

# VER COMENTARIOS DE UN POST 

# comentarios = post1.comment_set.all()
# for comentario in comentarios:
#     print(comentario.contenido)