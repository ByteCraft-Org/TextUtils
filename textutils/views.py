# User Created File
from django.shortcuts import render, redirect

def index(request):
    return render(request, "index.html")

def analyse(request):
    terminaltext = request.POST.get('text', 'default')
    punctuations = """`~!@#$%^&*()-_=+[{]};:'",<.>/?"""
    UpperCase = request.POST.get('UpperCase', 'off')
    LowerCase = request.POST.get('LowerCase', 'off')
    RemovePunctuation = request.POST.get('RemovePunctuation', 'off')
    NewLineRemove = request.POST.get('NewLineRemove', 'off')
    SpaceRemove = request.POST.get('SpaceRemove', 'off')
    CharCount = request.POST.get('CharCount', 'off')

    onFunction = ""
    analyzed = terminaltext

    if UpperCase == "on":
        if onFunction != "":
            onFunction = onFunction + ", "
        onFunction = onFunction + "Upper Case"
        analyzed = analyzed.upper()

    if LowerCase == "on":
        if onFunction != "":
            onFunction = onFunction + ", "
        onFunction = onFunction + "Lower Case"
        analyzed = analyzed.lower()

    sampletext = ""
    if RemovePunctuation == "on":
        onFunction = onFunction + "Remove Punctuation"
        for char in analyzed:
            if char not in punctuations:
                sampletext = sampletext + char

        analyzed = sampletext

    sampletext = ""
    if NewLineRemove == "on":
        if onFunction != "":
            onFunction = onFunction + ", "
        onFunction = onFunction + "Space Remove"
        for char in analyzed:
            if char != "\n" and char != "\r":
                sampletext = sampletext + char
            elif char == "\n":
                sampletext = sampletext + " "
        analyzed = sampletext

    if SpaceRemove == "on":
        if onFunction != "":
            onFunction = onFunction + ", "
        onFunction = onFunction + "Space Remove"
        analyzed = analyzed.replace("  ", "")

    strcount = ""
    if CharCount == "on":
        if onFunction != "":
            onFunction = onFunction + ", "
        onFunction = onFunction + "Character Count"
        count = len(analyzed)

        strcount = "There are total " + str(count) + " characters"

    params = {'purpose': onFunction, 'analyzed_text': analyzed, 'count': strcount}
    return render(request, 'analyse.html', params)
