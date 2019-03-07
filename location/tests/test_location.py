import pytest
from location import Location


class TestLocation:
    def test_construction(self):
        location = Location("NAME", 55.3, 1.6)

        assert location.name == "NAME"
        assert location.latitude == 55.3
        assert location.longitude == 1.6

    def test_incorrect_types(self):
        with pytest.raises(TypeError):
            Location(55, 55.3, 1.6)

        with pytest.raises(TypeError):
            Location("NAME", "55.3", 1.6)

        with pytest.raises(TypeError):
            Location("NAME", 55.3, "1.6")
