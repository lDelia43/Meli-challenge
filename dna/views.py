from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import DnaSequence
from .utils import is_mutant

@csrf_exempt
def mutant_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            dna = data['dna']
            dna_sequence, _ = DnaSequence.objects.get_or_create(
                dna=dna,
                defaults={'is_mutant': is_mutant(dna)}
            )
            if dna_sequence.is_mutant:
                return JsonResponse({'is_mutant': True}, status=200)
            else:
                return JsonResponse({'is_mutant': False}, status=200)
        except (KeyError, json.JSONDecodeError):
            return JsonResponse({'error': 'Invalid DNA data'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
