from django.db import models

class Apropos(models.Model):
    nom= models.CharField(max_length=100)
    description= models.TextField()
    image = models.ImageField(upload_to= 'apropos_image/')

    def __str__(self):
        return self.nom
    

class Service(models.Model):
    nom= models.CharField(max_length=100)
    description= models.TextField()

    def __str__(self):
        return self.nom
    


class Realisation(models.Model):
    nom= models.CharField(max_length=100)
    description= models.TextField()
    image = models.ImageField(upload_to= 'realisation_image/')
    icon_realisation=models.ImageField(upload_to= 'icon_image/')
    nom_ecrivain=models.CharField(max_length=100)
    profession=models.CharField(max_length=100)

    def __str__(self):
        return self.nom
    

class Contact(models.Model):
    email = models.EmailField(max_length=100)
    messages = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.email} - {self.date}"



class Partenaire(models.Model):
    nom = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='partenaire_logo/')
    site_web = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    ordre = models.IntegerField(default=0)

    class Meta:
        ordering = ['ordre', 'nom']

    def __str__(self):
        return self.nom


class Pays(models.Model):
    nom = models.CharField(max_length=100)
    code = models.CharField(max_length=10, help_text="Code ISO (ex: FR, SN)")
    drapeau = models.ImageField(upload_to='pays_drapeau/')
    ordre = models.IntegerField(default=0)

    class Meta:
        ordering = ['ordre', 'nom']
        verbose_name_plural = "Pays"

    def __str__(self):
        return self.nom


class Visa(models.Model):
    pays = models.ForeignKey(Pays, on_delete=models.CASCADE, related_name='visas')
    image = models.ImageField(upload_to='visa_images/')
    titre = models.CharField(max_length=100, blank=True, help_text="Titre indicatif ou description courte")
    ordre = models.IntegerField(default=0)

    class Meta:
        ordering = ['ordre', 'titre']

    def __str__(self):
        return f"{self.titre} - {self.pays.nom}"
