from django.contrib import admin

from .models import Pelicula, ComentarioPelicula, Serie, ComentarioSerie, Recomendacion

admin.site.register(Pelicula)
admin.site.register(ComentarioPelicula)
admin.site.register(Serie)
admin.site.register(ComentarioSerie)
admin.site.register(Recomendacion)


# Register your models here.
