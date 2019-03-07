def typedproperty(name, _type):
    """
    Create type checking properties that store values in a private backing variable.
    """
    private_name = "_" + name

    @property
    def _typedproperty(self):
        return getattr(self, private_name)

    @_typedproperty.setter
    def _typedproperty(self, value):
        if not isinstance(value, _type):
            raise TypeError(f"{name} expected type {_type:!r} got {value:!r}")
        setattr(self, private_name, value)

    return _typedproperty
