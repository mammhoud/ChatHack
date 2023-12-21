from django.shortcuts import render
from apps.boards.models import Board
from django.core import serializers


def index(request):
    channels = serializers.serialize('json', Board.objects.all())
    context = {
        'segment'  : 'boards',
        'parent'   : 'apps',
        'boards': boards
    }
    return render(request, 'apps/boards.html', context)


def update_data(request):
  if request.method == 'POST':
    # Update your component data based on request data
    # Example:
    component_data['value'] = 'new_value'
    return JsonResponse({'new_value': component_data['value']})
  return HttpResponseNotAllowed(['POST'])