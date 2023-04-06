# This is an automatically generated file.
# DO NOT EDIT or your changes may be overwritten
import base64
from xdrlib import Packer, Unpacker

from .base import Opaque
from .constants import *

__all__ = ["SCBytes"]


class SCBytes:
    """
    XDR Source Code::

        typedef opaque SCBytes<SCVAL_LIMIT>;
    """

    def __init__(self, sc_bytes: bytes) -> None:
        self.sc_bytes = sc_bytes

    def pack(self, packer: Packer) -> None:
        Opaque(self.sc_bytes, SCVAL_LIMIT, False).pack(packer)

    @classmethod
    def unpack(cls, unpacker: Unpacker) -> "SCBytes":
        sc_bytes = Opaque.unpack(unpacker, SCVAL_LIMIT, False)
        return cls(sc_bytes)

    def to_xdr_bytes(self) -> bytes:
        packer = Packer()
        self.pack(packer)
        return packer.get_buffer()

    @classmethod
    def from_xdr_bytes(cls, xdr: bytes) -> "SCBytes":
        unpacker = Unpacker(xdr)
        return cls.unpack(unpacker)

    def to_xdr(self) -> str:
        xdr_bytes = self.to_xdr_bytes()
        return base64.b64encode(xdr_bytes).decode()

    @classmethod
    def from_xdr(cls, xdr: str) -> "SCBytes":
        xdr_bytes = base64.b64decode(xdr.encode())
        return cls.from_xdr_bytes(xdr_bytes)

    def __eq__(self, other: object):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.sc_bytes == other.sc_bytes

    def __str__(self):
        return f"<SCBytes [sc_bytes={self.sc_bytes}]>"
