from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyse(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    # Initialize variables
    analysed = djtext
    purpose = ""

    # Check which checkbox is on and apply corresponding transformation
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analysed = "".join(char for char in djtext if char not in punctuations)
        purpose += 'Removed Punctuations '

    if fullcaps == "on":
        analysed = analysed.upper()
        purpose += 'Changed to Uppercase '

    if newlineremover == "on":
        analysed = analysed.replace("\n", "").replace("\r", "")
        purpose += 'Removed New Lines '

    if extraspaceremover == "on":
        analysed = " ".join(analysed.split())
        purpose += 'Removed Extra Spaces '

    # Check if no transformation is selected
    if purpose == "":
        return HttpResponse("Error: No operation selected")

    params = {'purpose': purpose, 'analysed_text': analysed}
    return render(request, 'analyse.html', params)
