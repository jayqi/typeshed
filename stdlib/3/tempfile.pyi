# Stubs for tempfile
# Ron Murawski <ron@horizonchess.com>

# based on http://docs.python.org/3.3/library/tempfile.html

import sys
from types import TracebackType
from typing import Any, AnyStr, Generic, IO, Optional, Tuple, Type

# global variables
TMP_MAX: int
tempdir = ...  # type: Optional[str]
template = ...  # type: str


if sys.version_info >= (3, 5):
    def TemporaryFile(
        mode: str = ..., buffering: int = ..., encoding: Optional[str] = ...,
        newline: Optional[str] = ..., suffix: Optional[AnyStr] = ..., prefix: Optional[AnyStr] = ...,
        dir: Optional[AnyStr] = ...
    ) -> IO[Any]:
        ...
    def NamedTemporaryFile(
        mode: str = ..., buffering: int = ..., encoding: Optional[str] = ...,
        newline: Optional[str] = ..., suffix: Optional[AnyStr] = ..., prefix: Optional[AnyStr] = ...,
        dir: Optional[AnyStr] = ..., delete: bool = ...
    ) -> IO[Any]:
        ...
    def SpooledTemporaryFile(
        max_size: int = ..., mode: str = ..., buffering: int = ...,
        encoding: str = ..., newline: str = ..., suffix: Optional[AnyStr] = ...,
        prefix: Optional[AnyStr] = ..., dir: Optional[AnyStr] = ...
    ) -> IO[Any]:
        ...

    class TemporaryDirectory(Generic[AnyStr]):
        name = ...  # type: str
        def __init__(self, suffix: Optional[AnyStr] = ..., prefix: Optional[AnyStr] = ...,
                     dir: Optional[AnyStr] = ...) -> None: ...
        def cleanup(self) -> None: ...
        def __enter__(self) -> AnyStr: ...
        def __exit__(self, exc_type: Optional[Type[BaseException]],
                     exc_val: Optional[BaseException],
                     exc_tb: Optional[TracebackType]) -> bool: ...

    def mkstemp(suffix: Optional[AnyStr] = ..., prefix: Optional[AnyStr] = ..., dir: Optional[AnyStr] = ...,
                text: bool = ...) -> Tuple[int, AnyStr]: ...
    def mkdtemp(suffix: Optional[AnyStr] = ..., prefix: Optional[AnyStr] = ...,
                dir: Optional[str] = ...) -> AnyStr: ...
    def mktemp(suffix: Optional[AnyStr] = ..., prefix: Optional[AnyStr] = ..., dir: Optional[AnyStr] = ...) -> AnyStr: ...

    def gettempdirb() -> bytes: ...
    def gettempprefixb() -> bytes: ...
else:
    def TemporaryFile(
        mode: str = ..., buffering: int = ..., encoding: Optional[str] = ...,
        newline: Optional[str] = ..., suffix: str = ..., prefix: str = ...,
        dir: Optional[str] = ...
    ) -> IO[Any]:
        ...
    def NamedTemporaryFile(
        mode: str = ..., buffering: int = ..., encoding: Optional[str] = ...,
        newline: Optional[str] = ..., suffix: str = ..., prefix: str = ...,
        dir: Optional[str] = ..., delete: bool = ...
    ) -> IO[Any]:
        ...
    def SpooledTemporaryFile(
        max_size: int = ..., mode: str = ..., buffering: int = ...,
        encoding: str = ..., newline: str = ..., suffix: str = ...,
        prefix: str = ..., dir: Optional[str] = ...
    ) -> IO[Any]:
        ...

    class TemporaryDirectory:
        name = ...  # type: str
        def __init__(self, suffix: str = ..., prefix: str = ...,
                     dir: Optional[str] = ...) -> None: ...
        def cleanup(self) -> None: ...
        def __enter__(self) -> str: ...
        def __exit__(self, exc_type: Optional[Type[BaseException]],
                     exc_val: Optional[BaseException],
                     exc_tb: Optional[TracebackType]) -> bool: ...

    def mkstemp(suffix: str = ..., prefix: str = ..., dir: Optional[str] = ...,
                text: bool = ...) -> Tuple[int, str]: ...
    def mkdtemp(suffix: str = ..., prefix: str = ...,
                dir: Optional[str] = ...) -> str: ...
    def mktemp(suffix: str = ..., prefix: str = ..., dir: Optional[str] = ...) -> str: ...

def gettempdir() -> str: ...
def gettempprefix() -> str: ...
