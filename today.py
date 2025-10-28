from datetime import date
import json

def handler(request):
    """
    Vercel serverless fonksiyonu için handler.
    request: Vercel'in otomatik olarak verdiği request objesi
    """
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
        },
        'body': json.dumps({
            'today': date.today().isoformat()
        })
    }
