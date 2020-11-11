import sys
from typing import TypeVar, overload, List, Sequence

from numpy import ndarray
from numpy.typing import ArrayLike

if sys.version_info >= (3, 8):
    from typing import SupportsIndex
else:
    from typing_extensions import Protocol
    class SupportsIndex(Protocol):
        def __index__(self) -> int: ...

_ArrayType = TypeVar("_ArrayType", bound=ndarray)

@overload
def atleast_1d(__arys: ArrayLike) -> ndarray: ...
@overload
def atleast_1d(*arys: ArrayLike) -> List[ndarray]: ...

@overload
def atleast_2d(__arys: ArrayLike) -> ndarray: ...
@overload
def atleast_2d(*arys: ArrayLike) -> List[ndarray]: ...

@overload
def atleast_3d(__arys: ArrayLike) -> ndarray: ...
@overload
def atleast_3d(*arys: ArrayLike) -> List[ndarray]: ...

def vstack(tup: Sequence[ArrayLike]) -> ndarray: ...
def hstack(tup: Sequence[ArrayLike]) -> ndarray: ...
@overload
def stack(
    arrays: Sequence[ArrayLike], axis: SupportsIndex = ..., out: None = ...
) -> ndarray: ...
@overload
def stack(
    arrays: Sequence[ArrayLike], axis: SupportsIndex = ..., out: _ArrayType = ...
) -> _ArrayType: ...
def block(arrays: ArrayLike) -> ndarray: ...
