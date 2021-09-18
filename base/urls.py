from django.urls import path
from .views import BookList, BookDetail, BookCreate, BookUpdate, BookDelete, CustomLoginView, RegisterPage, HomeView
from django.contrib.auth.views import LogoutView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('shelf/logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('shelf/', BookList.as_view(), name='Books'),
    path('shelf/book/<int:pk>/', BookDetail.as_view(), name='book'),
    path('shelf/book-create/', BookCreate.as_view(), name='book-create'),
    path('shelf/book-update/<int:pk>/', BookUpdate.as_view(), name='book-update'), 
    path('shelf/book-delete/<int:pk>/', BookDelete.as_view(), name='book-delete'), 
]