from rest_framework import serializers
from core.models import RiverSegment
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class RiverSegmentSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = RiverSegment
        fields = ['id', 'name', 'geometry']
        geo_field = "geometry"
