import pathlib

from .location import Location  # NOQA
from .locationstore import LocationStore  # NOQA
from .sources import FileSource, NetworkSource  # NOQA

name = "location"
version = "0.1.0"

__all__ = [
    "name",
    "version",
    "get_store",
    "Location",
    "LocationStore",
    "FileSource",
    "NetworkSource",
]


def get_store(path=None, formatter_name="txt"):
    """
    Fetch a store using the file provided (defaults to the included data file) and the
    specified formatter name (defaults to 'txt')."""
    if path is None:
        this_dir = pathlib.Path(__file__).parent
        path = this_dir / "coords.csv"
    source = FileSource(path)
    store = LocationStore(formatter_name)
    store.fetch_places(source)
    return store
