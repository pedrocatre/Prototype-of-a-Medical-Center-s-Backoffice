from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.template import RequestContext

from centrom.models import *

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from datetime import datetime, timedelta
from django.db.models import Q
from django.core.paginator import Paginator, InvalidPage
import smtplib



def main_page(request):
    
    health_workers = HealthWorker.objects.order_by('-id')
    variables = RequestContext(request, {
                                         'health_workers': health_workers
                                         })
    #output = u'''<html> <head>%s</head><p>what</p></html>''' % (u'Django bookmarks')
    return render_to_response(
                              'main_page.html',
                              variables
                             )
