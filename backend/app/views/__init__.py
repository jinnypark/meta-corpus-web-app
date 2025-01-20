"""
These view functions and classes implement API endpoints
"""
from rest_framework.decorators import api_view
from rest_framework.response import Response

# from .models import ()
# from .serializers import ()

@api_view(['GET'])
def example(request, example_id):
    """
    API example endpoint.
    """
    data = {
        'name': 'Example',
        'id': example_id,
    }
    return Response(data)

# import other views for directory
from .score import (
    handler_score as score,
    handler_text as text,
    handler_facts as facts
)
from .search import handler as search