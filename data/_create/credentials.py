import os
from collections import namedtuple


def dict2namedtuple(
    typename: str, data: dict
):  # https://stackoverflow.com/questions/43921240/pythonic-way-to-convert-a-dictionary-into-namedtuple-or-another-hashable-dict-li  # noqa
    """converts a (nested) dictionary to a namedtuple"""
    return namedtuple(typename, data.keys())(
        *(
            dict2namedtuple(typename + "_" + k, v) if isinstance(v, dict) else v
            for k, v in data.items()
        )
    )


class Credentials:
    """
    Provides credentials for different apps. Credentials for an
    app called X are assigned as attribute X and stored as a namedtumple.
    Alternatively, credentials for all apps are stored in the attribute .apps
    as a dictionary.

    Usage:
    - The path to the credentials file can be provided during initialization
      via the argument path. A basic credentials file can be found on
      https://confluence.p7s1-tech.com/display/DF/Accounts.
    - By default, the file .hasselhoff in the home directory is used as
      credentials file. The home directory is stored in the class
      attribute Credentials.home_directory
    - Available credentials can be seen by printing an instance.
    - Credentials of a particular app can be accessed as
        1: 'nested attributes', i.e., Credentials().exasol.write.user
           (Implementation: Credentials().exasol is a named tuple)
        2: value of the dictionary attribute .apps, e.g.,
           Credentials().apps['exasol']['write']['user]

    Example:
      # -- import
      from Credentials import Credentials

      # -- show home directory (this is the default location of the credentials file)
      Credentials.home_directory

      # -- init
      credentials = Credentials()

      # -- show info about apps credentials
      credentials
      # alternative: credentials.apps

      # -- show dsn for exasol
      credentials.exasol.dsn
      # alternative: credentials.apps['exasol']['dsn']

    Note:
      If a user should not access a particular app with a particular role
      the credentials file should be adjusted.

    Possible extensions:
      - Verify the connection to the app.
      - Maybe it would be better to provide the credentials via environment
        variables, especially when working on a server?
      - Encryt/Decrypt credentials file

    """

    # -- class attribute
    home_directory = os.path.expanduser("~")

    # -- instance attributes
    def __init__(self, path: str = os.path.join(home_directory, ".hasselhoff")) -> None:
        """
        Input:
          path = path to the python file which contains the credentials
          as a dict that has the name apps, defaults to the file
          .hasselhoff located in Credentials.home_directory.

        Initialized Attributes:
          apps: Dict[str, Any] = contains the apps with corresponding
            credentials, this is the dict named apps in the file .hasselhoff
          For each key in apps, a attribute with this name is assigned to an
          instance and its value is given by the corresponding value of apps.
        """
        self.apps = self._get_credentials(path)
        for app in self.apps:
            setattr(self, app, dict2namedtuple(app, self.apps[app]))

    def _get_credentials(
        self, path: str = os.path.join(home_directory, ".hasselhoff")
    ) -> dict:
        # -- path to credentials file of the apps
        assert os.path.exists(path), f"{path} does not exists"

        # -- import credentials (I could also write the credentails as a json file and load this file but loading it directly as a dict is simpler at the moment)  # noqa
        from importlib.machinery import SourceFileLoader

        module_apps = SourceFileLoader("apps", path).load_module()
        apps = module_apps.apps  # variable apps of the module apps
        return apps

    def __repr__(self) -> str:
        return str(dict2namedtuple("credentials", self.apps))
