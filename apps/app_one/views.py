from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string


def index(request):
    if not "word" in request.session:
        request.session["word"] = 'Empty'
    if not "count" in request.session:
        request.session["count"] = 0
    if request.method == "GET":
        return render(request, "app_one/index.html")
    if request.method == "POST":
        request.session['word'] = get_random_string(length=14)
        request.session['count'] += 1
        return redirect('/')

# def generator(request):
    
#     return redirect('/')

def reset(request):
    request.session['count'] = 0
    return redirect('/')