import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .video_list_service import video_list
from requests import Request
from .rocket_manager import RocketManager

@csrf_exempt
def rocket_view(request: Request):
    """
    This view handles rocket-related requests. It can handle GET and POST requests.
    GET: Retrieves rocket metadata using RocketManager.
    POST: Accepts JSON data containing 'img_data', processes it using RocketManager,
          and returns the result in JSON format.
    """
    if request.method == "GET":
        return get_rocket()
    elif request.method == "POST":
        return post_image(request)

def get_rocket():
    """
    Retrieves metadata about a rocket image and returns it as a JSON response.
    """
    meta_data = RocketManager.get_rocket_image()._asdict()
    return JsonResponse(meta_data, status=200)

def post_image(request: Request):
    """
    Processes an image related to a rocket and returns the result in JSON format.
    """
    request_body = request.body.decode("utf-8")
    try:
        body_data = json.loads(request_body)
        img_data = body_data.get("img_data")
        
        if img_data is None:
            return JsonResponse({"error": "img_data is missing"}, status=400)

        img_data_result = RocketManager.get_next_image(img_data)._asdict()
        return JsonResponse(img_data_result, status=200)
    
    except Exception as error:
        return JsonResponse({"error": f"Error getNextImage: {error}"}, status=500)
