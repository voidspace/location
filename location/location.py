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

    def to_tuple(self):
        return tuple(self)

    def __iter__(self):
        for field in ["name", "longitude", "latitude"]:
            yield getattr(self, field)

    def __repr__(self):
        return f"Location({self.name!r}, {self.latitude!r}, {self.longitude!r})"

    def __str__(self):
        return f"<Location name={self.name!r} latitude={self.latitude!r} longitude={self.longitude!r}>"

    def __eq__(self, other):
        if not isinstance(other, Location):
            return False
        return (
            other.name == self.name
            and other.longitude == self.longitude
            and self.latitude == other.latitude
        )
