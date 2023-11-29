from django.shortcuts import render
import datetime

# Create your views here.
context_dict = {'name': 'Rahim',
                      'age': 20,
                      'numbers': [1, 2, 3, 4, 5],
                      'list': ['I', 'am', 'learning', 'django'],
                      'quato': 'i\'m Rahim',
                      'courses': [
                            {'name': 'python', 'teacher': 'Rahim', 'length': 5, 'fees': 1000},
                            {'name': 'django', 'teacher': 'Rahim', 'length': 4, 'fees': 2000},
                      ],
                      'sentence': 'Programming is fun',
                      'date': datetime.datetime.now(),
                      'empty': "",
                      "new_msg": 2,
            }

def geeksfor(request):
      return render(request, 'geeksfor.html', context=context_dict)

def earthly(request):
      return render(request, 'earthly.html', context=context_dict)