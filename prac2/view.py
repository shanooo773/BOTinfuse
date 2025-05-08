from django.http import HttpResponse
import requests
from django.shortcuts import render

def HOME(request):
    return render(request, "index.html")

def about_us(request):
    return render(request, "about.html")
def blog(request):
    return render(request, "blog.html")
def blog_d(request):
    return render(request, "blog-details.html")
def contact_us(request):
    msg = "Please fill out the form to contact us."

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Replace with your actual webhook URL
        webhook_url = "https://prod-207.westeurope.logic.azure.com:443/workflows/0f5ce6ba9dcd4f589b3153142e334b68/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=xd-Pj90i8YpA1jnfkhnLKLGLs4FtjdWcBx2wrOBWAZc"

        payload = {
            "name": name,
            "email": email,
            "message": message
        }

        try:
            response = requests.post(webhook_url, json=payload)
            response.raise_for_status()  # raises exception for 4xx/5xx errors
            msg = f"Thanks {name}! We’ve received your message."
        except Exception as e:
            print("Error sending to Power Automate:", e)
            msg = "Oops—there was a problem saving your message."

    return render(request, "contact.html", {"msg": msg})