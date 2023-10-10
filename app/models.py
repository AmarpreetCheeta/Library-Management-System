from django.db import models


class BooksModel(models.Model):
	bookid = models.CharField(max_length=10)
	title = models.CharField(max_length=500)
	autors = models.CharField(max_length=200)
	average_rating = models.CharField(max_length=100)
	isbn = models.CharField(max_length=100)
	isbn13 = models.CharField(max_length=100)
	language_codes = models.CharField(max_length=100)
	num_pages = models.IntegerField()
	ratings_count = models.IntegerField()
	text_reviews_count = models.IntegerField()
	publication_date = models.CharField(max_length=100)
	publisher = models.CharField(max_length=200)

	def __str__(self):
		return str(self.bookid)


GENDER = (
	('Male', 'Male'),
	('Female', 'Female')
)

STATUS = (
	('Active', 'Active'),
	('No Active', 'No Active'),
)


class MemberModel(models.Model):
	memberid = models.CharField(max_length=10)
	member_name = models.CharField(max_length=200)
	Gender = models.CharField(max_length=10, choices=GENDER)
	bookid = models.ForeignKey(BooksModel, on_delete=models.CASCADE)
	status = models.CharField(max_length=20, choices=STATUS)
	rent = models.IntegerField()
	book_issue_date = models.DateField(auto_now_add=True)

	def __str__(self):
		return str(self.memberid)