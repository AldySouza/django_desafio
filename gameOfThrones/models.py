from django.db import models

#tentativa de converter em base64 no código
""" with open(f'./images/*.png', 'rb') as ImgFile:
    byteform = base64.b64encode(ImgFile.read())

f = open('output.bin', 'wb') """

# Criação das migrations
class Characters(models.Model):
    id = models.IntegerField(max_length=3, primary_key=True)
    name = models.CharField(max_length=35, null=False, blank=False)
    gender = models.CharField(max_length=12)
    culture = models.CharField(max_length=20, null=True, blank=True)
    born = models.CharField(max_length=20, null=True, blank=True)
    died = models.CharField(max_length=20, null=True, blank=True)
    titles = models.JSONField(blank=False, null=False)
    aliases = models.JSONField()
    father = models.TextField()
    mother = models.TextField()
    spouse = models.CharField(max_length=100, null=True, blank=True)
    allegiances = models.JSONField()
    books = models.JSONField()
    povBooks = models.JSONField()
    tvSeries = models.JSONField()
    playedBy = models.JSONField()


    def __str__(self):
        return self.name









