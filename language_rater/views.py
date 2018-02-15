from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from language_rater.models import Language
from language_rater.forms import VoteForm

# Create your views here.
def index(request):
	langs = Language.objects.all() # ModelManager, keeps track of model instances in database. Here, get all languages
	return render(request, "language_rater/vote_page.html", {'langs': langs})

def upvote(request, lang_id):
	language = Language.objects.get(pk=lang_id)
	language.vote()
	language.save()
	return HttpResponseRedirect("/rate")