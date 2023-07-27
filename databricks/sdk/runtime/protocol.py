from __future__ import annotations

import typing
from collections.abc import Callable

if typing.TYPE_CHECKING:
    from pyspark.sql.types import DataType
    from pyspark.sql import DataFrame


class SparkFunctionUDF(typing.Protocol):
    def __call__(
        self,
        f: Callable,
        returnType: typing.Union[DataType, str],
    ) -> Callable:
        ...


class SparkSessionTable(typing.Protocol):
    def __call__(self, tableName: str) -> DataFrame:
        ...


class SparkSessionSQL(typing.Protocol):
    def __call__(self, sqlQuery: str, **kwargs: typing.Any) -> DataFrame:
        ...


class FileInfo(typing.NamedTuple):
    path: typing.Any
    name: typing.Any
    size: typing.Any
    modificationTime: typing.Any


class MountInfo(typing.NamedTuple):
    mountPoint: typing.Any
    source: typing.Any
    encryptionType: typing.Any


class SecretScope(typing.NamedTuple):
    name: str

    def getName(self) -> str:
        return self.name


class SecretMetadata(typing.NamedTuple):
    key: str


class Credentials(typing.Protocol):
    """
    Utilities for interacting with credentials within notebooks
    """

    @staticmethod
    def assumeRole(role: str) -> bool:
        """
        Sets the role ARN to assume when looking for credentials to authenticate with S3
        """
        ...

    @staticmethod
    def showCurrentRole() -> typing.List[str]:
        """
        Shows the currently set role
        """
        ...

    @staticmethod
    def showRoles() -> typing.List[str]:
        """
        Shows the set of possibly assumed roles
        """
        ...

    @staticmethod
    def getCurrentCredentials() -> typing.Mapping[str, str]:
        ...


class Data(typing.Protocol):
    """
    Utilities for understanding and interacting with datasets (EXPERIMENTAL)
    """

    @staticmethod
    def summarize(df: typing.Any, precise: bool = False) -> None:
        """Summarize a Spark/pandas/Koalas DataFrame and visualize the statistics to get quick insights.

        Example: dbutils.data.summarize(df)

        :param df: A pyspark.sql.DataFrame, pyspark.pandas.DataFrame, databricks.koalas.DataFrame
        or pandas.DataFrame object to summarize. Streaming dataframes are not supported.
        :param precise: If false, percentiles, distinct item counts, and frequent item counts
        will be computed approximately to reduce the run time.
        If true, distinct item counts and frequent item counts will be computed exactly,
        and percentiles will be computed with high precision.

        :return: visualization of the computed summmary statistics.
        """
        ...


class FS(typing.Protocol):
    """
    Manipulates the Databricks filesystem (DBFS) from the console
    """

    @staticmethod
    def cp(source: str, dest: str, recurse: bool = False) -> bool:
        """
        Copies a file or directory, possibly across FileSystems
        """
        ...

    @staticmethod
    def head(file: str, max_bytes: int = 65536) -> str:
        """
        Returns up to the first 'maxBytes' bytes of the given file as a String encoded in UTF-8
        """
        ...

    @staticmethod
    def ls(path: str) -> typing.List[FileInfo]:
        """
        Lists the contents of a directory
        """
        ...

    @staticmethod
    def mkdirs(dir: str) -> bool:
        """
        Creates the given directory if it does not exist, also creating any necessary parent directories
        """
        ...

    @staticmethod
    def mv(source: str, dest: str, recurse: bool = False) -> bool:
        """
        Moves a file or directory, possibly across FileSystems
        """
        ...

    @staticmethod
    def put(file: str, contents: str, overwrite: bool = False) -> bool:
        """
        Writes the given String out to a file, encoded in UTF-8
        """
        ...

    @staticmethod
    def rm(dir: str, recurse: bool = False) -> bool:
        """
        Removes a file or directory
        """
        ...

    @staticmethod
    def cacheFiles(*files):
        ...

    @staticmethod
    def cacheTable(name: str):
        ...

    @staticmethod
    def uncacheFiles(*files):
        ...

    @staticmethod
    def uncacheTable(name: str):
        ...

    @staticmethod
    def mount(
        source: str,
        mount_point: str,
        encryption_type: str = "",
        owner: typing.Optional[str] = None,
        extra_configs: typing.Mapping[str, str] = {},
    ) -> bool:
        """
        Mounts the given source directory into DBFS at the given mount point
        """
        ...

    @staticmethod
    def updateMount(
        source: str,
        mount_point: str,
        encryption_type: str = "",
        owner: typing.Optional[str] = None,
        extra_configs: typing.Mapping[str, str] = {},
    ) -> bool:
        """
        Similar to mount(), but updates an existing mount point (if present) instead of creating a new one
        """
        ...

    @staticmethod
    def mounts() -> typing.List[MountInfo]:
        """
        Displays information about what is mounted within DBFS
        """
        ...

    @staticmethod
    def refreshMounts() -> bool:
        """
        Forces all machines in this cluster to refresh their mount cache, ensuring they receive the most recent information
        """
        ...

    @staticmethod
    def unmount(mount_point: str) -> bool:
        """
        Deletes a DBFS mount point
        """
        ...


class TaskValues(typing.Protocol):
    """
    Provides utilities for leveraging job task values
    """

    @staticmethod
    def get(taskKey: str, key: str, default: typing.Any = None, debugValue: typing.Any = None) -> None:
        """
        Returns the latest task value that belongs to the current job run
        """
        ...

    @staticmethod
    def set(key: str, value: typing.Any) -> None:
        """
        Sets a task value on the current task run
        """
        ...


class Jobs(typing.Protocol):
    """
    Utilities for leveraging jobs features
    """
    taskValues: TaskValues


class Notebook(typing.Protocol):
    """
    Utilities for the control flow of a notebook (EXPERIMENTAL)
    """

    @staticmethod
    def exit(value: str) -> None:
        """
        This method lets you exit a notebook with a value
        """
        ...

    @staticmethod
    def run(path: str, timeout_seconds: int, arguments: typing.Mapping[str, str]) -> str:
        """
        This method runs a notebook and returns its exit value
        """
        ...


class Library(typing.Protocol):
    """
    Utilities for session isolated libraries
    """
    notebook: Notebook

    @staticmethod
    def restartPython() -> None:
        """
        Restart python process for the current notebook session
        """
        ...


class Secrets(typing.Protocol):
    """
    Provides utilities for leveraging secrets within notebooks
    """

    @staticmethod
    def get(scope: str, key: str) -> str:
        """
        Gets the string representation of a secret value with scope and key
        """
        ...

    @staticmethod
    def getBytes(self, scope: str, key: str) -> bytes:
        """Gets the bytes representation of a secret value for the specified scope and key."""

    @staticmethod
    def list(scope: str) -> typing.List[SecretMetadata]:
        """
        Lists secret metadata for secrets within a scope
        """
        ...

    @staticmethod
    def listScopes() -> typing.List[SecretScope]:
        """
        Lists secret scopes
        """
        ...


class GetArgument(typing.Protocol):
    def __call__(self, name: str, defaultValue: typing.Optional[str] = None) -> str:
        ...


class Widgets(typing.Protocol):
    """
    provides utilities for working with notebook widgets. You can create different types of widgets and get their bound value
    """
    getArgument: GetArgument

    @staticmethod
    def get(name: str) -> str:
        """Returns the current value of a widget with give name.
        :param name: Name of the argument to be accessed
        :return: Current value of the widget or default value
        """
        ...

    @staticmethod
    def text(name: str, defaultValue: str, label: str = None) -> None:
        """Creates a text input widget with given name, default value and optional label for
        display
        :param name: Name of argument associated with the new input widget
        :param defaultValue: Default value of the input widget
        :param label: Optional label string for display in notebook and dashboard
        """
        ...

    @staticmethod
    def dropdown(name: str, defaultValue: str, choices: typing.List[str], label: str = None) -> None:
        """Creates a dropdown input widget with given specification.
        :param name: Name of argument associated with the new input widget
        :param defaultValue: Default value of the input widget (must be one of choices)
        :param choices: List of choices for the dropdown input widget
        :param label: Optional label string for display in notebook and dashboard
        """
        ...

    @staticmethod
    def combobox(
        name: str,
        defaultValue: str,
        choices: typing.List[str],
        label: typing.Optional[str] = None,
    ) -> None:
        """Creates a combobox input widget with given specification.
        :param name: Name of argument associated with the new input widget
        :param defaultValue: Default value of the input widget
        :param choices: List of choices for the dropdown input widget
        :param label: Optional label string for display in notebook and dashboard
        """
        ...

    @staticmethod
    def multiselect(
        name: str,
        defaultValue: str,
        choices: typing.List[str],
        label: typing.Optional[str] = None,
    ) -> None:
        """Creates a multiselect input widget with given specification.
        :param name: Name of argument associated with the new input widget
        :param defaultValue: Default value of the input widget (must be one of choices)
        :param choices: List of choices for the dropdown input widget
        :param label: Optional label string for display in notebook and dashboard
        """
        ...

    @staticmethod
    def remove(name: str) -> None:
        """Removes given input widget. If widget does not exist it will throw an error.
        :param name: Name of argument associated with input widget to be removed
        """
        ...

    @staticmethod
    def removeAll() -> None:
        """Removes all input widgets in the notebook."""
        ...


class dbutils(typing.Protocol):
    credentials: Credentials
    data: Data
    fs: FS
    jobs: Jobs
    library: Library
    secrets: Secrets
    widgets: Widgets


class Display(typing.Protocol):
    """
    Display plots or data.
    Display plot:
                    - display() # no-op
                    - display(matplotlib.figure.Figure)
    Display dataset:
                    - display(spark.DataFrame)
                    - display(list) # if list can be converted to DataFrame, e.g., list of named tuples
                    - display(pandas.DataFrame)
                    - display(koalas.DataFrame)
                    - display(pyspark.pandas.DataFrame)
    Display any other value that has a _repr_html_() method
    For Spark 2.0 and 2.1:
                    - display(DataFrame, streamName='optional', trigger=optional pyspark.sql.streaming.Trigger,
                                                    checkpointLocation='optional')
    For Spark 2.2+:
                    - display(DataFrame, streamName='optional', trigger=optional interval like '1 second',
                                                    checkpointLocation='optional')
    """
    def __call__(self, input: typing.Any, *args: typing.Any, **kwargs: typing.Any) -> None:
        ...


class DisplayHTML(typing.Protocol):
    """
    Display HTML data.
    Parameters
    ----------
    data : URL or HTML string
                    If data is a URL, display the resource at that URL, the resource is loaded dynamically by the browser.
                    Otherwise data should be the HTML to be displayed.
    See also:
    IPython.display.HTML
    IPython.display.display_html
    """
    def __call__(self, html: str) -> None:
        ...
