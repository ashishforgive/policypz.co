from django.shortcuts import render

def home(request):
    return render(request, 'websiteApp/home.html')

def registration(request):
    return render(request, 'websiteApp/registration.html')

def userLogin(request):
    return render(request, 'websiteApp/login.html')

def aboutPolicy(request):
    return render(request, 'websiteApp/about-policy.html')

def privacy(request):
    return render(request, 'websiteApp/privacy.html')

def howToVote(request):
    return render(request, 'websiteApp/how-to-vote.html')

def term(request):
    return render(request, 'websiteApp/term.html')

def allElections(request):
    return render(request, 'websiteApp/all-elections.html')

def yourFavourites(request):
    return render(request, 'websiteApp/your-favourites.html')

def school(request):
    return render(request, 'websiteApp/school.html')


