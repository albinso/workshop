from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from language_rater.models import Language

# Create your views here.
def index(request):
	langs = Language.objects.all() # ModelManager, keeps track of model instances in database. Here, get all languages
	return render(request, "language_rater/vote_page.html", {'langs': langs})