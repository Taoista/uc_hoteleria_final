from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    # path('hoteles/create', views.create, name="index"),
    # path('hoteles/ver', views.ver, name="ver"),

    path('hotel/<int:id_hotel>/', views.hotel, name="hotel"),
    path('contacto', views.contacto, name="contacto"),
    path('reservar', views.reservar, name="reservar"),
    path('checkout', views.checkout, name="checkout"),

    path('create-reservation', views.create_reservacion, name="create-reservation"),
    # ? mustra la vista final
    path('success_reserva/<int:id_reserva>/', views.success_reserva, name="success_reserva"),

    

    # ? lectura (read)

    # ? edita (update)
    # path('admin/editar', views.editar, name="editar"),
    # # ? crear (create)
    # path('admin/crear', views.crear, name="crear"),
    # # ? eliminar (detele)
    # path('admin/eliminar', views.eliminar, name="eliminar"),




]