import re


class DomainException(Exception):
    """Raised when an invalid is created."""


class Domain:

    def __init__(self, name: str):
        # validate a current domain (r'.*\.[a-z]{2,3}$' is fine)
        if re.match(r'.*\.[a-z]{2,3}$', name):
            self.name = name
        else:  # if not valid, raise a DomainException
            raise DomainException

    # next add a __str__ method and write 2 class methods
    # called parse_url and parse_email to construct domains
    # from an URL and email respectively
    def __str__(self) -> str:
        return self.name

    @classmethod
    def parse_url(cls, name: str) -> str:
        '''Create a domain from a url.'''
        return cls(name.split('/')[2])

    @classmethod
    def parse_email(cls, name: str) -> str:
        '''Create a domain from an email.'''
        return cls(name.split('@')[-1])
