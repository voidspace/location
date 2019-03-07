import pathlib

name = 'location'
version = '0.1.0'

from .location import Location
from .locationstore import LocationStore
from .sources import FileSource, NetworkSource


def get_store(path=None, formatter_name='txt'):
    """Fetch a store using the file provides (defaults to the included data file) and the specified formatter name
    (defaults to 'txt')."""
    if path is None:
        this_dir = pathlib.Path(__file__).parent
        path = this_dir / 'coords.csv'
    source = FileSource(path)
    store = LocationStore(formatter_name)
    store.fetch_places(source)
    return store
