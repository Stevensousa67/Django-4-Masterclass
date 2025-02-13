from django.urls import path
from . import views

app_name = 'food'
urlpatterns = [
    path('', views.index, name='index'),    # This is the home page (/food/)
    path('<int:item_id>/', views.detail, name='detail'),    # This is the detail page (/food/1/)
    path('item/', views.Item, name='item'),     # This is the item page (/food/item/)
    path('add', views.create_item, name='create_item'),    # This is the add page (/food/add/)
    path('update/<int:item_id>', views.update_item, name='update_item' ), # This is the edit page (/food/edit/)
    path('delete/<int:item_id>', views.delete_item, name='delete_item'), # This is the delete page (/food/delete/)
]