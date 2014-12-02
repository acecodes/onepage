"""
Placeholder project
"""

import os
import sys

"""
Settings
"""

from django.conf import settings

DEBUG = os.environ.get('DEBUG', 'on') == 'on'

SECRET_KEY = os.environ.get('SECRET_KEY', ')4*fk*az97t-v+bs^mj)49i(c$q3kjypp87s+e-r+n5pjs1xf5')

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')

settings.configure(
    DEBUG=DEBUG,
    SECRET_KEY=SECRET_KEY,
    ALLOWED_HOSTS=ALLOWED_HOSTS,
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        ),
    )

"""
Views
"""

from django.conf.urls import url
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse, HttpResponseBadRequest
from django import forms
from io import BytesIO
from PIL import Image


class ImageForm(forms.Form):
    """Form to validate request placeholder image."""

    height = forms.IntegerField(min_value=1, max_value=2000)
    width = forms.IntegerField(min_value=1, max_value=2000)

def index(request):
    return HttpResponse('Testing, 123...')

def placeholder(request, width, height):
    form = ImageForm({'height':height, 'width':width})
    if form.is_valid():
        height = form.cleaned_data['height']
        width = form.cleaned_data['width']
        return HttpResponse('To be replaced...')
    return HttpResponseBadRequest('Invalid image request')

urlpatterns = (
    url(r'^$', index, name='homepage'),
    url(r'^image/(?P<width>[0-9]+)x(?P<height>[0-9]+)/$', placeholder, name='placeholder')
    )

application = get_wsgi_application()

if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)