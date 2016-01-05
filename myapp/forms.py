from myapp.models_main import Article, Comment
from django import forms
from django.contrib.admin import widgets


class ArticleForm(forms.ModelForm):

	class Meta:
		model = Article
		fields =('title', 'category', 'thumbnail', 'pub_date') 

	def __init__(self, *args, **kwargs):
		super(ArticleForm, self). __init__(*args, **kwargs )
		self.fields['pub_date'].widget = widgets.AdminDateWidget()

		


class CommentForm(forms.ModelForm):
	
	class Meta:
		model = Comment
		fields = ('body', 'pub_date')		





