from .typedproperty import typedproperty


class Location:
    __slots__ = ["_name", "_latitude", "_longitude"]

    name = typedproperty("name", str)
    latitude = typedproperty("latitude", float)
    longitude = typedproperty("longitude", float)

    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def __iter__(self):
        for field in ["name", "longitude", "latitude"]:
            yield getattr(self, field)

    def __repr__(self):
        return f"Location({self.name:!r}, {self.latitude:!r}, {self.longitude:!r})"
