"""
Provides the function `run_cmd` to execute shell commands from Python.

This module is mainly used interally for `ds.inspect`.

For more sophisticated subprocesses have a look at
[delegator](https://github.com/amitt001/delegator.py).

See
[here](http://www.leancrew.com/all-this/2012/04/python-doesnt-play-nicely-with-others/)
why Python's subprocess is not very user-friendly.
"""
from __future__ import annotations

import os
import re
import subprocess
from tempfile import NamedTemporaryFile


class RunCMDError(Exception):
    """
    Raises an exception from `subprocess.CalledProcessError` to provide
    information the error message of the stderr stream.

    Requires that the stderr stream is forwarded to `subprocess.CalledProcessError`.

    Note:
        This is used in `run_cmd`.

    Example:
        ```python
        import subprocess import CalledProcessError, STDOUT
        from ds.shell import RunCMDError

        # The error message of the stderr stream is not included in `CalledProcessError`
        try:
            # Set stderr=STDOUT to forward the stderr stream to `CalledProcessError`
            result = subprocess.check_output(
                ["ls", "nonexistent_file"], stderr=STDOUT
            )
        except CalledProcessError as e:
            print("Exception =", e)
            print("Error message from stderr:", e.returncode)
            print("Output:", e.output.decode("utf-8"))

        # The error message of the stderr stream is included in RunCMDError
        try:
            # Set stderr=STDOUT to forward the stderr stream to `CalledProcessError`
            result = subprocess.check_output(
                ["ls", "nonexistent_file"], stderr=STDOUT
            )
        except CalledProcessError as e:
            raise RunCMDError(e) from e
        ```
    """  # noqa

    def __init__(self, exception: subprocess.CalledProcessError):
        # This is empty if print_stderr of `run_cmd` is True
        stderr_stream = exception.output.decode("utf-8")
        super().__init__(stderr_stream)

    """ Dev note
    Unfortunately, something like
    ```python
    from ds.shell import run_cmd
    try:
        run_cmd(...)
    except subprocess.CalledProcessError as e:
        msg = e.output.decode("utf-8")
        raise subprocess.CalledProcessError(msg) from e
    ```
    cannot be used because `subprocess.CalledProcessError` must be initialized
    with 'returncode' and 'cmd', but it not error message. For instance,
    ````python
    raise subprocess.CalledProcessError(2, "ha")
    # Returns
    "CalledProcessError: Command 'ha' returned non-zero exit status 2."
    ```
    """


# TODO: Test on Windows OS
def _shell_split(cmd: str):
    """
    This is `shlex.split` on posix system, on Windows the Windows splitting
    syntax is used. On Windows, this is the inverse of `subprocess.list2cmdline`.

    Note:
        This is used in `ds.shell.run_shell_comamnd`.
        This has not been tested on Windows OS.
        Inspired by
        https://stackoverflow.com/a/54730743.

    Example:
        ```python
        from ds.shell import shell_split

        shell_split("echo $PATH")
        ```
    """
    import json  # json is an easy way to send arbitrary ascii-safe lists of strings out of python  # noqa
    import shlex
    import subprocess
    import sys

    if os.name == "posix":
        return shlex.split(cmd)
    else:
        if not cmd:
            return []
        full_cmd = "{} {}".format(
            subprocess.list2cmdline(
                [
                    sys.executable,
                    "-c",
                    "import sys, json; print(json.dumps(sys.argv[1:]))",
                ]
            ),
            cmd,
        )
        ret = subprocess.check_output(full_cmd).decode()
        return json.loads(ret)


def run_cmd(
    cmd: str, cwd: str = ".", print_stderr: bool = False, shell: bool = False
) -> list[str]:
    """
    Returns the stdout of the shell command `cmd` executed in the directory
    `cwd`.

    Moreover, it captures the stderr stream of a possible
    `subprocess.CalledProcessError` by rasing `RunCMDError`.

    Limitations:
        `run_cmd("git checkout branch -- file")` raises the error that
        'file' did not match any file(s) known to git. Setting `shell` to True
        makes no difference and `os.system` throws the same error.

    Args:
        cmd: Shell command that should be run.
        cwd: Working directory of the shell. By default, the current working
            directory of the Python interpreter is used.
        print_stderr: If False, the stderr stream is not printed to the console
            and the captured error message of the stderr stream is forwarded to
            `RunCMDError` if a `subprocess.CalledProcessError` occurs.
            If True, the stderr stream is printed to the console and
            not captured by `RunCMDError`.
        shell: If True, the shell is invoked explicitly, see the
            [subprocess docs](https://docs.python.org/3/library/subprocess.html#frequently-used-arguments).
            If False, the shell is not used to run the shell command. Note that
            variable interpolation is a shell feature. See
            [here](https://stackoverflow.com/a/5659249).

    Raises:
        `RunCMDError`: Caused by a `subprocess.CalledProcessError` with the
            error message being the caputed error message of the stderr stream
            if `print_stderr` is False.

    Returns:
        list: The stdout of the shell command splitted into a list w.r.t. the
            delimiter "\\n".

    Example:
        ```python
        import traceback
        from ds.shell import run_cmd, RunCMDError

        # -- Display the files and folders of the current working directory
        run_cmd("ls")

        # -- Display the files and folders of the parent working directory
        run_cmd("ls", path="..")

        # -- Invoke the shell or not
        # Note that variable interpolation is a shell feature.
        run_cmd("echo $PATH", shell=True)

        # Without shell=True, the string that is echoed is simply literally $PATH
        run_cmd("echo $PATH")

        # -- Capturing the error message of the stderr stream
        # The error message of the stderr stream is included in RunCMDErrorr
        try:
            run_cmd("ls _nonexistent_folder")
        except RunCMDError:
             traceback.print_exc()

        # Here the error message of the stderr stream is printed to the console
        # before the exception traceback is printed
        try:
            run_cmd("ls _nonexistent_folder", print_stderr=True)
        except RunCMDError:
            traceback.print_exc()
        ```
    """  # noqa
    """ Explanation of the parameter print_stderr
    ChatGPT: "What is the meaning of stderr in subprocess.check_output in Python?"

    In Python's subprocess module, the subprocess.check_output() function is
    used to run a command as a subprocess and capture its standard output
    (stdout). The stderr (standard error) is a separate stream where error
    messages and diagnostics are typically printed.

    When you use subprocess.check_output(), you capture the standard output of
    the command you're running, which is usually the regular program output.
    By default, the standard error stream is not captured and will still be
    printed to the console.

    If you want to capture both standard output and standard error, you can set
    the stderr argument to subprocess.STDOUT. This will merge the standard error
    stream into the standard output stream, allowing you to capture both in a
    single output.

    Here's an example:

    ```python
    import subprocess

    # Run a command and capture its stdout and stderr
    try:
        result = subprocess.check_output(
            ["ls", "-l", "nonexistent_file"], stderr=subprocess.STDOUT
        )
        print("Output:", result.decode("utf-8"))
    except subprocess.CalledProcessError as e:
        print("Error:", e.returncode)
        print("Output:", e.output.decode("utf-8"))
        print(e)
    ```

    In this example, the ls -l nonexistent_file command is run. Since the file
    doesn't exist, an error message is printed to the standard error stream.
    By using stderr=subprocess.STDOUT, we capture both the standard output and
    the standard error output into the output attribute of the CalledProcessError
    exception.

    By default, if you don't specify stderr=subprocess.STDOUT, only the standard
    output will be captured using check_output(), and the standard error will
    still be printed to the console.

    Note that in the above example,
        - print(e.returncode) yields "ls: cannot access 'nonexistent_file': No
            such file or directory"
        - print(e.output.decode("utf-8")) yields "2"
        - print(e) only yields
            "CalledProcessError: Command '['ls', '-l', 'nonexistent_file']'
            returned non-zero exit status 2."

    If stderr is not specified then print(e) yields an empty string.
    """
    # Command must be given as string if shell is True, e.g., https://stackoverflow.com/a/54765780  # noqa
    if shell is True:
        parsed_cmd = cmd
    else:
        parsed_cmd = _shell_split(cmd)
    if not print_stderr:
        stderr = subprocess.STDOUT
    else:
        stderr = None

    try:
        res = subprocess.check_output(
            parsed_cmd, cwd=cwd, stderr=stderr, shell=shell
        ).splitlines()
        res_parsed = [file.decode("utf-8") for file in res]
        return res_parsed
    except subprocess.CalledProcessError as e:
        raise RunCMDError(e) from e


class TemporaryScript:
    """
    Creates a `tempfile.NamedTemporaryFile` with `code` that can be `run` with
    Python.

    Useful for testing the behavior of functions if they are called when a Python
    script is executed. The name of the temporay file starts with
    'ds_temporary_script_' and ends with '.py'.

    Example:
        ```python
        from ds.shell import TemporaryScript

        code = 'print("Hello World!")'
        with TemporaryScript(code) as ts:
            print("The path of the temporay file is", ts.file.name)
            print(
                f"The stdout of running 'python3 {ts.file.name}' is",
                f"'{ts.run()[0]}'"
            )
        ```
    """

    def __init__(self, code: str, prefix: str = "tmp_ds_script", suffix: str = ".py"):
        # TODO: update doc
        """
        Assigns a writable instance of `tempfile.NamedTemporaryFile` to the
        attribute `file` an inserts `code` into it.
        """
        self.code = code
        """Python code."""

        self.file = NamedTemporaryFile(mode="w", prefix=prefix, suffix=suffix)
        """A writable instance of `tempfile.NamedTemporaryFile` with prefix =
        "ds_temporary_script_" and suffix = ".py" into which `code` is
        written.
        """

        self.file.write(code)
        self.file.flush()

    def __enter__(self) -> TemporaryScript:
        return self

    def __exit__(self, exc_type, exc_value, exc_tb) -> None:
        self.file.close()

    def run(self, cwd: str = ".", args: None | str = None) -> list[str]:
        """
        Execute the `code` in `file` with Python in the working directory = `cwd`
        and command line arguments `args`.
        """
        if args is None:
            return run_cmd(f"python3 {self.file.name}", cwd=cwd)
        else:
            return run_cmd(f"python3 {self.file.name} {args}", cwd=cwd)


def list_files(
    folder: str = ".",  # do not use absolute paths here
    exclude_pattern: None | list[str] = None,
    exclude_files_unknown_to_git: bool = False,
) -> list[str]:
    """
    Folder in exclude must start with "./"
    """
    if exclude_pattern is None:
        exclude_pattern = []

    if exclude_files_unknown_to_git:
        files_known_to_git = run_cmd("git ls-files")
    else:
        files_known_to_git = []

    def _exclude(folder, exclude_pattern):
        # TODO: Instead of a loop could use | to combine exclude patterns
        for pattern in exclude_pattern:
            if re.search(pattern, folder):
                return True
            else:
                continue
        return False

    result = []

    for root, _, files in os.walk(folder):
        root = root[2:]
        # print(root)
        # print(files)
        # Not necessary, but if this is True then we don't have to iterate over files
        if _exclude(root, exclude_pattern):
            continue
        else:
            for file in files:
                # if file == "data.py":
                #     import pdb; pdb.set_trace()
                file_path = os.path.join(root, file)
                # if file_path == 'src/dsc/notebook.py':
                #   import pdb; pdb.set_trace()
                if _exclude(file_path, exclude_pattern):
                    continue
                if exclude_files_unknown_to_git:
                    if file_path not in files_known_to_git:
                        continue
                print(file_path)
                result.append(file_path)
    return result
