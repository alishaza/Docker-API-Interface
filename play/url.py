from django.urls import path
from . import views

#urlconfig
urlpatterns = [
    path('containers/' , views.Overall_ContainerStatus.as_view()),
    path('containers/<imagename>' , views.Specific_Container_Status.as_view()),
    path('<name>/' , views.app_detail.as_view()),
    path('run/<appname>' , views.container.as_view()),
    path('' , views.app_all_detail.as_view()),


]
