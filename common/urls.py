from django.urls import path
from . import views


app_name = 'common'

api_user_list = views.UserApiViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

api_user_detail = views.UserApiViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})


urlpatterns = [
    path('api/users/', api_user_list, name='api-user-list'),
    path('api/users/<int:pk>/', api_user_detail, name='api-user-detail'),
    # path('login/', views.UserLoginView.as_view(), name='login'),

    path('users/', views.UserListView.as_view(), name='users'),
    path('user/<int:pk>', views.UserDetailView.as_view(), name='user-detail'),

    path('user/create/', views.UserCreateView.as_view(), name='user-create'),
    # path('user/<int:pk>/update/', views.UserUpdateView.as_view(), name='user-update'),
    # path('user/<int:pk>/delete/', views.UserDeleteView.as_view(), name='user-delete'),
]
