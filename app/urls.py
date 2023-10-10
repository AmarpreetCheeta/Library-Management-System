from django.urls import path
from app.views import *

urlpatterns = [
	# Members Urls 
	path('', HomeView.as_view(), name='home'),
	path('create_update_member_books/', Create_MemberBooks.as_view(), name='create_update_member'),
	path('update_member/<memberid>/', Update_Memebers.as_view(), name='update_member'),
	path('del_member/<memberid>/', Del_member.as_view(), name='del_member'),
	path('search_member/', Search_member, name='search_member'),

	# Books Urls
	path('books/', BooksView.as_view(), name='books'),
	path('create_books/', Create_Books.as_view(), name='create_books'),
	path('update_books/<bookid>/', Update_book_data.as_view(), name='update_books'),
	path('del_book/<bookid>/', Delete_Book.as_view(), name='del_book'),
	path('search_books/', Search_Books, name='search_books'),
]