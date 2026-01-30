from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.contrib import messages

def accueil(request):
    apropos = Apropos.objects.all()  
    services = Service.objects.all() 
    realisations = Realisation.objects.all() 
    partenaires = Partenaire.objects.all()
    pays_list = Pays.objects.prefetch_related('visas').all()

    context={
        'apropos':apropos,
        'services':services,
        'realisations':realisations,
        'partenaires':partenaires,
        'pays_list':pays_list
    }
    return render(request,'genova/nextgenova.html',context)


def contact(request):
    if request.method == "POST":
        email = request.POST.get("email")
        message = request.POST.get("message")

        if email and message:
            try:
                send_mail(
                    subject="Nouveau message de contact",
                    message=f"Email: {email}\n\nMessage:\n{message}",
                    from_email=email,  
                    recipient_list=["ton_email@gmail.com"],  
                    fail_silently=False,
                )
                messages.success(request, "Votre message a été envoyé avec succès !")
            except Exception as e:
                messages.error(request, "Erreur lors de l'envoi du message.")

        return redirect("contact")  

    return render(request, "genova/nextgenova.html")
