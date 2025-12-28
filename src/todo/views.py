from django.shortcuts import render

# Create your views here.

def index(request):
    data: Dict[str, str] = {
        'insert_something': "views.pyのinsert_something部分です。",
    }

    return render(request, "index.html", data)
