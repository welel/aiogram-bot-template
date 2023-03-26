import os


class ImproperlyConfigured(Exception):
    """Raises when a environment variable is missing."""

    def __init__(self, variable_name: str, *args, **kwargs):
        self.variable_name = variable_name
        self.message = f"Set the {variable_name} environment variable."
        super().__init__(self.message, *args, **kwargs)


def getenv(var_name: str, cast_to=str) -> str:
    """Gets an environment variable or raises an exception.

    Args:
        var_name: An environment variable name.
        cast_to: A type to cast.

    Returns:
        A value of the environment variable.

    Raises:
        ImproperlyConfigured: If the environment variable is missing.
    """
    try:
        value = os.environ[var_name]
        return cast_to(value)
    except KeyError:
        raise ImproperlyConfigured(var_name)
    except ValueError:
        raise ValueError(f"The value {value} can't be cast to {cast_to}.")
