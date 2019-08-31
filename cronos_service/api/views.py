from django.shortcuts import render

# Create your views here.
from django.views import View


class HomeView(View):

    @staticmethod
    def get(request):
        return render(request, template_name="home.html")
