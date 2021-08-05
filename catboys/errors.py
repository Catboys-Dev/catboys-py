class CatboyException(Exception):
    """ Base exception class for catboys.py """

    pass


class NothingFound(CatboyException):
    """ The API didn't return anything """

    pass


class EmptyArgument(CatboyException):
    """ When no target is defined """

    pass


class InvalidArgument(CatboyException):
    """ Invalid argument within the category """

    pass
