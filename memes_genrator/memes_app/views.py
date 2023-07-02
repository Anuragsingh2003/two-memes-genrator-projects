from django.shortcuts import render, redirect

def generate_meme(request):
    return render(request, 'meme_form.html')

