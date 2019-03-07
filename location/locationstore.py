from math import cos, asin, sqrt
from .formatters import create_formatter


class LocationStore:

    def __init__(self, formatter_name):
        self._formatter = create_formatter(formatter_name)
        self._places = {}

    def __getitem__(self, name):
        return self._places[name]

    def __setitem__(self, name, value):
        self._places[name] = value

    def __delitem__(self, name):
        del self._places[name]

    def __len__(self):
        return len(self._places)

    def __contains__(self, name):
        return name in self._places

    def __iter__(self):
        for item in self._places.values():
            yield item

    def fetch_places(self, source):
        places = source.fetch()
        for place in places:
            self[place.name] = place

    def get_place(self, name):
        return self[name]

    def all_names(self):
        return list(self._places.keys())

    def distance(self, name1, name2):
        """Haversine geographic distance. Returns distance in kilometres."""
        loc1 = self.get_place(name1)
        loc2 = self.get_place(name2)
        return self._distance(loc1, loc2)

    def _distance(self, location1, location2):
        lat1 = location1.latitude
        lat2 = location2.latitude
        lon1 = location1.longitude
        lon2 = location2.longitude

        p = 0.017453292519943295     #Pi/180
        a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
        return 12742 * asin(sqrt(a))

    def display_locations(self):
        self._formatter.headings(['Name', 'Latitude', 'Longitude'])
        for name in self.all_names():
            self._formatter.row(self[name])

