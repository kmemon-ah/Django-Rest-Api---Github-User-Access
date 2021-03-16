from django.shortcuts import render
import requests

def index(request):
    if request.method == "POST":
        username = request.POST.get('username')
        url = f"https://api.github.com/users/{username}"
        response = requests.get(url)
        r = str(response)
        if r == ('<Response [200]>'):

            usr = response.json()
            return render(request,'githubapi/gitprofile.htm',context={'usr':usr})
        else:
            ur = "Invalid Username"
            return render(request,'githubapi/index.html',context={'ur':ur})


    return render(request,'githubapi/index.html')

def profile(request):
    return render(request,'githubapi/gitprofile.htm')
