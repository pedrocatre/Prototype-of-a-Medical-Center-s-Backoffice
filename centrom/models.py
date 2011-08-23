from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import get_template
from django.template import Context
from django.conf import settings
import os, Image

TINY_SIZE = (80,80)

class Specialty(models.Model):
    title = models.CharField(max_length=200)
    position = models.IntegerField()    # The position field
    slug = models.SlugField(max_length=50, unique=True, help_text = "Valor unico para o URL de Specialty")
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    meta_keywords = models.CharField("Meta Keywords", max_length=255, help_text = "Palavras chaves, separadas por virgulas, para optimizacao de motores de busca")
    meta_description = models.CharField("Meta description", max_length=255, help_text = "Conteudo para a meta tag de descricao")
    
    def __unicode__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        model = self.__class__
        
        if self.position is None:
            # Append
            try:
                last = model.objects.order_by('-position')[0]
                self.position = last.position + 1
            except IndexError:
                # First row
                self.position = 0
        
        return super(Specialty, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ('position',)
    
class SubSpecialty(models.Model):
    title = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(max_length=50, unique=True, help_text = "Valor unico para o URL de SubSpecialty")
    description = models.TextField()
    specialty = models.ForeignKey(Specialty)
    is_active = models.BooleanField(default=True)
    
    def __unicode__(self):
        return u'%s, %s' % (self.title, self.specialty.title)
    
class HealthWorker(models.Model):
    name = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(max_length=50, unique=True, help_text = "Valor unico para o URL de HealthWorker")
    specialties = models.ManyToManyField(Specialty)
    image = models.ImageField(upload_to='images/healthworkers')
    is_active = models.BooleanField(default=True)
    #photo
    def __unicode__(self):
        return self.name
    
    def admin_image(self):# http://stackoverflow.com/questions/2443752/django-display-image-in-admin-interface
        return '<img src="%s"/>' % self.image
    admin_image.allow_tags = True
    
    def thumb(self):# http://djangosnippets.org/snippets/239/
        return """<a href="/site_media/%s"><img src="/site_media/%s" alt="tiny thumbnail image" /></a>"""%(self.image,self.image)
        tinythumb = self.image.replace('\\','/').split('/')
        tinythumb[-1] = 'tiny/'+tinythumb[-1]
        tinythumb = '/'.join(tinythumb)
        return "pedro"
        if not os.path.exists(MEDIA_ROOT+tinythumb):
            im = Image.open(MEDIA_ROOT+self.image)
            im.thumbnail(TINY_SIZE,Image.ANTIALIAS)
            im.save(MEDIA_ROOT+tinythumb,"JPEG")
        return """<a href="/site_media/%s"><img src="/site_media/%s" alt="tiny thumbnail image" /></a>"""%(self.image,tinythumb)
    thumb.allow_tags = True
    
class ExamPreparation(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, unique=True, help_text = "Valor unico para o URL de Preparacao de Exame")
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.title

