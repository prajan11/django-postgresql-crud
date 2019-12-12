from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.employee_form, name="employee_insert"),
    path('<int:id>/',views.employee_form, name="employee_update"),
    path('list/', views.employee_list, name="employee_list"),
    path('delete/<int:id>', views.employee_delete, name='employee_delete')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
