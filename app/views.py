from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import JsonResponse
import json
import requests
from django.views.decorators.csrf import csrf_exempt
from app.models import *
from app.forms import *
from django.contrib import messages


# Members Starts
class HomeView(TemplateView):
	def get(self, request):
		members_counts = 0
		members = MemberModel.objects.all()
		members_counts = members.count()
		context = {'members': members, 'members_counts':members_counts}
		return render(request, 'home.html', context)


class Create_MemberBooks(TemplateView):
	def get(self, request):
		form = Membersforms()
		context = {'form':form}
		return render(request, 'create_update_member.html', context)

	def post(self, request):
		form = Membersforms(request.POST)
		if form.is_valid():
			memberid = form.cleaned_data['memberid']
			member_name = form.cleaned_data['member_name']
			Gender = form.cleaned_data['Gender']
			bookid = form.cleaned_data['bookid']
			status = form.cleaned_data['status']
			rent = form.cleaned_data['rent']
			reg = MemberModel(memberid=memberid,member_name=member_name,Gender=Gender,bookid=bookid,status=status,rent=rent)
			messages.success(request, 'Your new member has been create successfully.')
			reg.save()
			return redirect('create_update_member')

class Update_Memebers(TemplateView):
	def get(self, request, memberid):
		members = MemberModel.objects.get(memberid=memberid)
		form = Membersforms(instance=members)
		context = {'form':form}
		return render(request, 'create_update_member.html', context)

	def post(self, request, memberid):
		members = MemberModel.objects.get(memberid=memberid)
		form = Membersforms(request.POST, instance=members)
		if form.is_valid():
			form.save()
			return redirect('home')

class Del_member(TemplateView):
	def post(self, request, memberid):
		member = MemberModel.objects.get(memberid=memberid)
		member.delete()
		return redirect('home')

@csrf_exempt
def Search_member(request):
	if request.method == 'POST':
		res_data = json.loads(request.body)
		data = res_data['data']
		members = MemberModel.objects.filter(member_name__icontains=data).values()
		mem_data = list(members)
		return JsonResponse({'status':1, 'members':mem_data})

# Members Ends



# Books Start

class BooksView(TemplateView):
	def get(self, request):
		books_counts = 0
		books = BooksModel.objects.all()
		books_counts = books.count()
		context = {'books':books, 'books_counts':books_counts}
		return render(request, 'books.html', context)


class Create_Books(TemplateView):
	def get(self, request):
		form = BooksForm()
		context = {'form':form}
		return render(request, 'create_books.html', context)

	def post(self, request):
		form = BooksForm(request.POST)
		if form.is_valid():
			bookid = form.cleaned_data['bookid']
			title = form.cleaned_data['title']
			autors = form.cleaned_data['autors']
			average_rating = form.cleaned_data['average_rating']
			isbn = form.cleaned_data['isbn']
			isbn13 = form.cleaned_data['isbn13']
			language_codes = form.cleaned_data['language_codes']
			num_pages = form.cleaned_data['num_pages']
			ratings_count = form.cleaned_data['ratings_count']
			text_reviews_count = form.cleaned_data['text_reviews_count']
			publication_date = form.cleaned_data['publication_date']
			publisher = form.cleaned_data['publisher']
			reg = BooksModel(bookid=bookid,title=title,autors=autors,average_rating=average_rating,isbn=isbn,isbn13=isbn13,
				language_codes=language_codes,num_pages=num_pages,ratings_count=ratings_count,text_reviews_count=text_reviews_count,
				publication_date=publication_date,publisher=publisher)
			messages.success(request, 'Your new book has been inserted successfully.')
			reg.save()
			return redirect('create_books')


class Update_book_data(TemplateView):
	def get(self, request, bookid):
		book_data = BooksModel.objects.get(bookid=bookid)
		form = BooksForm(instance=book_data)
		context = {'form':form}
		return render(request, 'create_books.html', context)

	def post(self, request, bookid):
		book_data = BooksModel.objects.get(bookid=bookid)
		form = BooksForm(request.POST,instance=book_data)
		if form.is_valid():
			form.save()
			return redirect('books')


class Delete_Book(TemplateView):
	def post(self, request, bookid):
		book_data = BooksModel.objects.get(bookid=bookid)
		book_data.delete()
		return redirect('books')

@csrf_exempt
def Search_Books(request):
	if request.method == 'POST':
		res_data = json.loads(request.body)
		data = res_data['data']
		books = BooksModel.objects.filter(autors__icontains=data).values()
		book_data = list(books)
		return JsonResponse({'status':1, 'books':book_data})

# Books Ends
