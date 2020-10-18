# This is an automatically generated file.
# DO NOT EDIT or your changes may be overwritten
import base64
from xdrlib import Packer, Unpacker

from .revoke_sponsorship_result_code import RevokeSponsorshipResultCode

__all__ = ["RevokeSponsorshipResult"]


class RevokeSponsorshipResult:
    """
    XDR Source Code
    ----------------------------------------------------------------
    union RevokeSponsorshipResult switch (RevokeSponsorshipResultCode code)
    {
    case REVOKE_SPONSORSHIP_SUCCESS:
        void;
    default:
        void;
    };
    ----------------------------------------------------------------
    """

    def __init__(self, code: RevokeSponsorshipResultCode,) -> None:
        self.code = code

    def pack(self, packer: Packer) -> None:
        self.code.pack(packer)
        if self.code == RevokeSponsorshipResultCode.REVOKE_SPONSORSHIP_SUCCESS:
            return

    @classmethod
    def unpack(cls, unpacker: Unpacker) -> "RevokeSponsorshipResult":
        code = RevokeSponsorshipResultCode.unpack(unpacker)
        if code == RevokeSponsorshipResultCode.REVOKE_SPONSORSHIP_SUCCESS:
            return cls(code)

    def to_xdr_bytes(self) -> bytes:
        packer = Packer()
        self.pack(packer)
        return packer.get_buffer()

    @classmethod
    def from_xdr_bytes(cls, xdr: bytes) -> "RevokeSponsorshipResult":
        unpacker = Unpacker(xdr)
        return cls.unpack(unpacker)

    def to_xdr(self) -> str:
        xdr_bytes = self.to_xdr_bytes()
        return base64.b64encode(xdr_bytes).decode()

    @classmethod
    def from_xdr(cls, xdr: str) -> "RevokeSponsorshipResult":
        xdr = base64.b64decode(xdr.encode())
        return cls.from_xdr_bytes(xdr)

    def __eq__(self, other: object):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.code == other.code

    def __str__(self):
        out = []
        out.append(f"code={self.code}")
        return f"<RevokeSponsorshipResult {[', '.join(out)]}>"
