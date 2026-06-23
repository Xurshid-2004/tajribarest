import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def test_api(request):
    if request.method == 'GET':
        return JsonResponse({
            'success': True,
            'message': 'API ishlayapti',
            'method': 'GET',
        })

    if request.method == 'POST':
        try:
            data = json.loads(request.body or '{}')
        except json.JSONDecodeError:
            return JsonResponse({
                'success': False,
                'message': "JSON noto'g'ri yuborildi",
            }, status=400)

        return JsonResponse({
            'success': True,
            'message': "POST ma'lumot qabul qilindi",
            'data': data,
        })

    return JsonResponse({
        'success': False,
        'message': 'Faqat GET va POST methodlari ishlaydi',
    }, status=405)
