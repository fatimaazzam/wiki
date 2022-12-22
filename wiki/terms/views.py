from django.views.generic import ListView
from .models import Keyword

class AllKeywordsView(ListView):
    model = Keyword
    template_name = "terms/base.html"
