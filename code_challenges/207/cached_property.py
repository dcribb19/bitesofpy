# from property_manager import cached_property -
# PASSES TESTS LOCALLY BUT NOT SUPPORTED ON pybit.es
# https://property-manager.readthedocs.io/en/latest/_modules/property_manager.html
import os
from random import random
from time import sleep
from typing import Hashable

NOTHING = object()


def set_property(obj, name, value):
    obj.__dict__[name] = value


def clear_property(obj, name):
    obj.__dict__.pop(name, None)


class custom_property(property):
    cached = False
    dynamic = False
    environment_variable = None
    key = False
    repr = True
    required = False
    resettable = False
    usage_notes = True
    writable = False

    def __new__(cls, *args, **options):
        if options:
            name = args[0] if args else 'customized_property'
            options['dynamic'] = True
            return type(name, (cls,), options)
        else:
            return super(custom_property, cls).__new__(cls, *args)

    def __init__(self, *args, **kw):
        super(custom_property, self).__init__(*args, **kw)
        self.ensure_callable('fget')
        for name in 'fset', 'fdel':
            if getattr(self, name) is not None:
                self.ensure_callable(name)
        for name in '__doc__', '__module__', '__name__':
            value = getattr(self.fget, name, None)
            if value is not None:
                setattr(self, name, value)

    def ensure_callable(self, role):
        value = getattr(self, role)
        if not callable(value):
            raise ValueError

    def __get__(self, obj, type=None):
        if obj is None:
            return self
        else:
            if self.key or self.writable or self.cached:
                value = obj.__dict__.get(self.__name__, NOTHING)
                if value is not NOTHING:
                    return value
            if self.environment_variable:
                value = os.environ.get(self.environment_variable, NOTHING)
                if value is not NOTHING:
                    return value
            value = super(custom_property, self).__get__(obj, type)
            if self.cached:
                set_property(obj, self.__name__, value)
            return value

    def __set__(self, obj, value):
        try:
            super(custom_property, self).__set__(obj, value)
        except AttributeError:
            if self.writable:
                set_property(obj, self.__name__, value)
            else:
                if self.key and obj.__dict__.get(self.__name__, None):
                    if not isinstance(value, Hashable):
                        raise ValueError
                    set_property(obj, self.__name__, value)
                else:
                    raise AttributeError

    def __delete__(self, obj):
        try:
            super(custom_property, self).__delete__(obj)
        except AttributeError:
            if self.resettable:
                clear_property(obj, self.__name__)
            else:
                raise AttributeError


class lazy_property(custom_property):
    cached = True


class cached_property(lazy_property):
    resettable = True


class Planet:
    """the nicest little orb this side of Orion's Belt"""
    GRAVITY_CONSTANT = 42
    TEMPORAL_SHIFT = 0.12345
    SOLAR_MASS_UNITS = 'M\N{SUN}'

    def __init__(self, color):
        self.color = color
        self._mass = self.mass

    def __repr__(self):
        return f'{self.__class__.__name__}({repr(self.color)})'

    @cached_property
    def mass(self):
        scale_factor = random()
        sleep(self.TEMPORAL_SHIFT)
        self._mass = (f'{round(scale_factor * self.GRAVITY_CONSTANT, 4)} '
                      f'{self.SOLAR_MASS_UNITS}')
        return self._mass
