from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'app' : 'CS Corner',
        'name': 'Putri Hamidah Riyanto',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)