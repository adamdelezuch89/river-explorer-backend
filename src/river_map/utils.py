from .constants import RIVERS, ZOOM_LEVELS
from itertools import chain

def get_zoom_settings(zoom):
    for level in ZOOM_LEVELS:
        if zoom <= level['max_zoom']:
            return level['tolerance'], level['river_count']
    return 0, None

def get_filter_condition(river_count):
    if river_count is None:
        return "", []
    
    # Flatten the nested river names by splitting comma-separated values
    rivers = list(chain.from_iterable(RIVERS[:river_count]))
    return "AND name IN %s", [tuple(rivers)]
