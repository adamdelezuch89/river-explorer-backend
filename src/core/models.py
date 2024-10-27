from django.db import models

from django.contrib.gis.db import models
from django.contrib.postgres.fields import ArrayField


class RiverSegment(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=255)
    flow_direction = models.CharField(
        max_length=20,
        choices=[
            ("upstream", "Upstream"),
            ("downstream", "Downstream"),
        ],
        null=True,
        blank=True,
    )
    flow_rate = models.FloatField(null=True, blank=True)
    geometry = models.LineStringField(srid=4326)

    class Meta:

        indexes = [
            models.Index(
                fields=["geometry"],
                name="idx_river_segment_geometry",
                opclasses=["gist_geometry_ops_2d"],
            ),
        ]
        constraints = [
            models.CheckConstraint(
                check=models.Q(flow_rate__gt=0) | models.Q(flow_rate__isnull=True),
                name="valid_flow_rate",
            ),
        ]
