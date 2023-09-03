"""Example Google style docstrings.

This module demonstrates documentation as specified by the ``Google Python
Style Guide``. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Example:
    Examples can be given using either the ```Example``` or ```Examples```
    sections. Sections support any reStructuredText formatting, including
    literal blocks::

        $ python example_google.py

Section breaks are created by resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.

Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

        Either form is acceptable, but the two should not be mixed. Choose
        one convention to document module level variables and be consistent
        with it.

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""

module_level_variable1 = 12345

module_level_variable2 = 98765
"""int: Module level variable documented inline.

The docstring may span multiple lines. The type may optionally be specified
on the first line, separated by a colon.
"""


def function_with_types_in_docstring(param1, param2):
    """Example function with types documented in the docstring.

    `PEP 484`_ type annotations are supported. If attribute, parameter, and
    return types are annotated according to `PEP 484`_, they do not need to be
    included in the docstring:

    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.

    Returns:
        bool: The return value. True for success, False otherwise.

    .. _PEP 484:
        https://www.python.org/dev/peps/pep-0484/

    """


def function_with_pep484_type_annotations(param1: int, param2: str) -> bool:
    """Example function with PEP 484 type annotations.

    Args:
        param1: The first parameter.
        param2: The second parameter.

    Returns:
        The return value. True for success, False otherwise.

    """


def module_level_function(param1, param2=None, *args, **kwargs):
    """This is an example of a module level function.

    Function parameters should be documented in the ``Args`` section. The name
    of each parameter is required. The type and description of each parameter
    is optional, but should be included if not obvious.

    If *args or **kwargs are accepted,
    they should be listed as ``*args`` and ``**kwargs``.

    The format for a parameter is::

        name (type): description
            The description may span multiple lines. Following
            lines should be indented. The "(type)" is optional.

            Multiple paragraphs are supported in parameter
            descriptions.

    Args:
        param1 (int): The first parameter.
        param2 (:obj:`str`, optional): The second parameter. Defaults to None.
            Second line of description should be indented.
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.

    Returns:
        bool: True if successful, False otherwise.

        The return type is optional and may be specified at the beginning of
        the ``Returns`` section followed by a colon.

        The ``Returns`` section may span multiple lines and paragraphs.
        Following lines should be indented to match the first line.

        The ``Returns`` section supports any reStructuredText formatting,
        including literal blocks::

            {
                'param1': param1,
                'param2': param2
            }

    Raises:
        AttributeError: The ``Raises`` section is a list of all exceptions
            that are relevant to the interface.
        ValueError: If `param2` is equal to `param1`.

    """
    if param1 == param2:
        raise ValueError("param1 may not be equal to param2")
    return True


class Vehicles(object):
    """
    The Vehicle object contains a lot of vehicles

    Args:
        arg (str): The arg is used for...
        *args: The variable arguments are used for...
        **kwargs: The keyword arguments are used for...

    Attributes:
        arg (str): This is where we store arg,
    """

    def __init__(self, arg, *args, **kwargs):
        self.arg = arg

    def cars(self, distance, destination):
        """We can't travel distance in vehicles without fuels, so here is the fuels

        Args:
            distance (int): The amount of distance traveled
            destination (bool): Should the fuels refilled to cover the distance?

        Raises:
            RuntimeError: Out of fuel

        Returns:
            cars: A car mileage
        """
        pass


def fetch_smalltable_rows() -> None:
    """Fetches rows from a Smalltable.

    Retrieves rows pertaining to the given keys from the Table instance
    represented by table_handle.  String keys will be UTF-8 encoded.

    Args:
        table_handle: An open smalltable.Table instance.
        keys: A sequence of strings representing the key of each table
          row to fetch.  String keys will be UTF-8 encoded.
        require_all_keys: If True only rows with values set for all keys will be
          returned.

    Returns:
        A dict mapping keys to the corresponding table row data
        fetched. Each row is represented as a tuple of strings. For
        example:

        {b'Serak': ('Rigel VII', 'Preparer'),
         b'Zim': ('Irk', 'Invader'),
         b'Lrrr': ('Omicron Persei 8', 'Emperor')}

        Returned keys are always bytes.  If a key from the keys argument is
        missing from the dictionary, then that row was not found in the
        table (and require_all_keys must have been False).

    Raises:
        IOError: An error occurred accessing the smalltable.
    """


class reST(object):
    """
    The Vehicle object contains lots of vehicles
    :param arg: The arg is used for ...
    :type arg: str
    :param `*args`: The variable arguments are used for ...
    :param `**kwargs`: The keyword arguments are used for ...
    :ivar arg: This is where we store arg
    :vartype arg: str
    """

    def __init__(self, arg, *args, **kwargs):
        self.arg = arg

    def cars(self, distance, destination):
        """We can't travel a certain distance in vehicles without fuels, so
            here's the fuels

        :param distance: The amount of distance traveled
        :type amount: int
        :param bool destinationReached: Should the fuels be refilled to cover
            required distance?
        :raises: :class:`RuntimeError`: Out of fuel

        :returns: A Car mileage
        :rtype: Cars
        """
        pass


class Numpy(object):
    """
    The Vehicles object contains lots of vehicles

    Parameters
    ----------
    arg : str
        The arg is used for ...
    *args
        The variable arguments are used for ...
    **kwargs
        The keyword arguments are used for ...

    Attributes
    ----------
    arg : str
        This is where we store arg,
    """

    def __init__(self, arg, *args, **kwargs):
        self.arg = arg

    def cars(self, distance, destination):
        """We can't travel distance in vehicles without fuels, so here is the fuels

        Parameters
        ----------
        distance : int
            The amount of distance traveled
        destination : bool
            Should the fuels refilled to cover the distance?

        Raises
        ------
        RuntimeError
            Out of fuel

        Returns
        -------
        cars
            A car mileage

        Attributes
        -------
        h: int
            bla
        """
        pass
