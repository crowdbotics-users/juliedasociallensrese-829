from django.shortcuts import render

# Create your views here.

from home.models import CustomText, HomePage


def home(request):
    packages = [
	{'name':'twilio', 'url': 'http://pypi.python.org/pypi/twilio/6.10.1'},
	{'name':'pinax-notifications', 'url': 'http://pypi.python.org/pypi/pinax-notifications/5.0.1'},
	{'name':'django-todo', 'url': 'http://pypi.python.org/pypi/django-todo/1.6.2'},
	{'name':'wq', 'url': 'http://pypi.python.org/pypi/wq/1.0.0'},
	{'name':'django-file-upload', 'url': 'http://pypi.python.org/pypi/django-file-upload/1.0.0'},
	{'name':'django-allauth', 'url': 'http://pypi.python.org/pypi/django-allauth/0.34.0'},
    ]
    context = {
        'customtext': CustomText.objects.first(),
        'homepage': HomePage.objects.first(),
        'packages': packages
    }
    return render(request, 'home/index.html', context)
