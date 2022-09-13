from django.contrib import admin
from django.urls import path
import mainapp.views as mainapp

urlpatterns = [
    path('', mainapp.main, name='main'),
    path('back', mainapp.back, name='back'),
    path('biceps', mainapp.biceps, name='biceps'),
    path('breast', mainapp.breast, name='breast'),
    path('legs', mainapp.legs, name='legs'),
    path('press', mainapp.press, name='press'),
    path('shoulders', mainapp.shoulders, name='shoulders'),
    path('triceps', mainapp.triceps, name='triceps'),
    path('admin/', admin.site.urls),
]
