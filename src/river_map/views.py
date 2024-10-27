from django.http import JsonResponse
from django.contrib.gis.geos import Polygon
from django.db import connection
from core.models import RiverSegment
from .utils import get_zoom_settings, get_filter_condition


def get_river_map(request):
    # Get the bounding box from the request parameters
    min_x, min_y = float(request.GET.get("min_x")), float(request.GET.get("min_y"))
    max_x, max_y = float(request.GET.get("max_x")), float(request.GET.get("max_y"))
    zoom = int(request.GET.get("zoom", 10))

    # Determine simplification tolerance and filter condition based on zoom level
    tolerance, river_count = get_zoom_settings(zoom)
    filter_condition, filter_params = get_filter_condition(river_count)

    # Create a bounding box polygon
    bbox = Polygon.from_bbox((min_x, min_y, max_x, max_y))

    # Query the database for rivers within the bounding box
    with connection.cursor() as cursor:
        query = f"""
            SELECT id, name, ST_AsGeoJSON(ST_Simplify(geometry, %s)) AS geometry
            FROM core_riversegment
            WHERE ST_Intersects(geometry, ST_SetSRID(ST_MakeEnvelope(%s, %s, %s, %s), 4326))
            {filter_condition}
        """
        params = [tolerance, min_x, min_y, max_x, max_y] + filter_params
        cursor.execute(query, params)

        rivers = [
            {"id": row[0], "name": row[1], "geometry": row[2]}
            for row in cursor.fetchall()
        ]

    # Return the river data as JSON
    return JsonResponse(rivers, safe=False)
