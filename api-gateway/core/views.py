import requests
from django.http import HttpResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name='dispatch')
class GatewayProxyView(View):
    def dispatch(self, request, *args, **kwargs):
        path = kwargs.get('path', '')

        # Enrutamiento
        if path.startswith('auth/'):
            target_url = f"http://identity-service:8001/api/{path}"
        else:
            target_url = f"http://business-service:8000/api/{path}"

        # Reenviar headers (incluyendo Authorization)
        headers = {}
        for key, value in request.headers.items():
            if key.lower() not in ['host', 'content-length']:
                headers[key] = value

        try:
            response = requests.request(
                method=request.method,
                url=target_url,
                headers=headers,
                data=request.body,
                params=request.GET,
                allow_redirects=False
            )

            django_response = HttpResponse(
                response.content,
                status=response.status_code
            )

            for key, value in response.headers.items():
                if key.lower() not in [
                    'content-encoding',
                    'transfer-encoding',
                    'connection',
                    'content-length'
                ]:
                    django_response[key] = value

            return django_response

        except requests.exceptions.RequestException as e:
            return HttpResponse(f"Error en el API Gateway: {str(e)}", status=503)