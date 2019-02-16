from django.urls import path
from django.views.decorators.cache import cache_page
from .views import (SearchView,
                    DishDetailView,
                    DishListView,
                    AddDishView,
                    AddOrderView,
                    OrderListView,
                    OrderDetailView,
                    DeleteDishView,
                    UpdateDishView,
                    AddIngredientView,
                    RegistrationView,)

app_name = 'coocking_book'

urlpatterns = [
    path('', DishListView.as_view(), name='dish_list'),
    path('dish/<int:pk>', DishDetailView.as_view(), name='dish_detail'),
    path('dish/delete/<int:pk>', DeleteDishView.as_view(), name='delete_dish'),
    path('dish/update/<int:dish_id>',
         UpdateDishView.as_view(), name='update_dish'),

    path('dish_search/result', SearchView.as_view(), name='dish_search'),
    path('add_dish', cache_page(300)(AddDishView.as_view()), name='add_dish'),
    path('add_order_list/<int:dish_id>',
         AddOrderView.as_view(), name='add_order_list'),
    path('orders/', OrderListView.as_view(), name='order_list'),
    path('orders/<int:pk>', OrderDetailView.as_view(), name='order_detail'),
    path('dish_<int:dish_id>/add_ingredients',
         AddIngredientView.as_view(), name='add_ingredients'),
    path('accounts/registration/', RegistrationView.as_view(), name='registration'),

]
