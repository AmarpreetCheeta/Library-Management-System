from django import forms
from app.models import *



class BooksForm(forms.ModelForm):
	class Meta:
		model = BooksModel
		fields = ['bookid','title','autors','average_rating','isbn','isbn13','language_codes',
				  'num_pages','ratings_count','text_reviews_count','publication_date','publisher']

		widgets = {
			'bookid': forms.TextInput(attrs={'class':'form-control'}),
			'title': forms.TextInput(attrs={'class':'form-control'}),
			'autors': forms.TextInput(attrs={'class':'form-control'}),
			'average_rating': forms.TextInput(attrs={'class':'form-control'}),
			'isbn': forms.TextInput(attrs={'class':'form-control'}),
			'isbn13': forms.TextInput(attrs={'class':'form-control'}),
			'language_codes': forms.TextInput(attrs={'class':'form-control'}),
			'num_pages': forms.NumberInput(attrs={'class':'form-control'}),
			'ratings_count': forms.NumberInput(attrs={'class':'form-control'}),
			'text_reviews_count': forms.NumberInput(attrs={'class':'form-control'}),
			'publication_date': forms.TextInput(attrs={'class':'form-control'}),
			'publisher': forms.TextInput(attrs={'class':'form-control'})
		}


class Membersforms(forms.ModelForm):
	class Meta:
		model = MemberModel
		fields = ['memberid','member_name','Gender','bookid','status','rent']
		widgets = {
			'memberid':forms.TextInput(attrs={'class':'form-control'}),
			'member_name': forms.TextInput(attrs={'class':'form-control'}),
			'Gender': forms.Select(attrs={'class':'form-control'}),
			'bookid': forms.Select(attrs={'class':'form-control'}),
			'status': forms.Select(attrs={'class':'form-control'}),
			'rent': forms.NumberInput(attrs={'class':'form-control'})
		}