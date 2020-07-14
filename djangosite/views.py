# code in this file is created by Vishwas
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # para = {'name':'vishwas', 'place':'mumbai'}
    # return HttpResponse('''<h1>Hello Vishwaschandra</h1> <a href='https://www.flanoyinfotech.com/' target="blank">Flanoy Infotech</a>''')
    return render(request, 'index.html')

# def about(request):
#     return HttpResponse('''<h1>Hello Vishwaschandra</h1> <a href="www.flanoyinfotech.com">Flanoy Infotech></a>''')
#
# def contact(request):
#     return HttpResponse("<h1>Hello Vishwaschandra</h1>")

def analyze(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    capitalize = request.POST.get('capitalize', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ''
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        param = {'purpose':'Removed Punctuation', 'analyzed_text':analyzed}
        # return render(request, 'analyze.html', param)
        djtext = analyzed
    if (capitalize == 'on'):
        analyzed = ''
        for char in djtext:
            analyzed += char.upper()
        param = {'purpose': 'Capitalize All', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', param)
        djtext = analyzed
    if (newlineremover == 'on'):
        analyzed = ''
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed += char
        param = {'purpose': 'New Line Remover', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', param)
        djtext = analyzed
    if (spaceremover == 'on'):
        analyzed = ''
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] ==" "):
                analyzed += char
        param = {'purpose': 'Extra Space Removed', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', param)
        djtext = analyzed
    if (charcount == 'on'):
        analyzed = ''
        count = 0
        for char in djtext:
            if not(char == " "):
                count += 1
                analyzed = count
        param = {'purpose': 'Character Counted', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', param)
        # djtext = analyzed
    if (removepunc != "on" and newlineremover != "on" and spaceremover != "on" and capitalize != "on" and charcount!="on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', param)
