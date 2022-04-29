from django.shortcuts import render
from django.views import View

# Create your views here.
class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'landing/index.html')



#fra: https://www.youtube.com/watch?v=BlXQCPsdcDc&list=PLPSM8rIid1a3TkwEmHyDALNuHhqiUiU5A&index=11
#kommet til part 4, 18:46