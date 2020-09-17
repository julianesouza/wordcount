from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    mostcounted = {}

    for word in wordlist:
        if word not in mostcounted:
            mostcounted[word] = 1
        else:
            mostcounted[word] += 1

    sortedWords = sorted(mostcounted.items(), key=lambda kx:kx[1], reverse=True)
    return render(request, 'count.html', {'formtext': fulltext, 'wordcount': len(wordlist), 'sortedWords': sortedWords})

def about(request):
    return render(request, 'about.html')
