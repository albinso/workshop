from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from language_rater.models import Language

# Lists all languages and corresponding vote count
def index(request):
	# ModelManager, keeps track of model instances in database. Here, get all languages sorted from most to least votes
	langs = Language.objects.order_by('-num_votes') 

	# Pass set of Language to the template which can process them as a list
	return render(request, "language_rater/vote_page.html", {'langs': langs})

def upvote(request, lang_id):
	language = Language.objects.get(pk=lang_id)
	language.vote()
	language.save()
	return HttpResponseRedirect("/rate")