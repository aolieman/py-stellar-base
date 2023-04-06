# This is an automatically generated file.
# DO NOT EDIT or your changes may be overwritten
import base64
from xdrlib import Packer, Unpacker

from .sc_spec_type import SCSpecType
from .sc_spec_type_bytes_n import SCSpecTypeBytesN
from .sc_spec_type_map import SCSpecTypeMap
from .sc_spec_type_option import SCSpecTypeOption
from .sc_spec_type_result import SCSpecTypeResult
from .sc_spec_type_set import SCSpecTypeSet
from .sc_spec_type_tuple import SCSpecTypeTuple
from .sc_spec_type_udt import SCSpecTypeUDT
from .sc_spec_type_vec import SCSpecTypeVec

__all__ = ["SCSpecTypeDef"]


class SCSpecTypeDef:
    """
    XDR Source Code::

        union SCSpecTypeDef switch (SCSpecType type)
        {
        case SC_SPEC_TYPE_VAL:
        case SC_SPEC_TYPE_BOOL:
        case SC_SPEC_TYPE_VOID:
        case SC_SPEC_TYPE_STATUS:
        case SC_SPEC_TYPE_U32:
        case SC_SPEC_TYPE_I32:
        case SC_SPEC_TYPE_U64:
        case SC_SPEC_TYPE_I64:
        case SC_SPEC_TYPE_TIMEPOINT:
        case SC_SPEC_TYPE_DURATION:
        case SC_SPEC_TYPE_U128:
        case SC_SPEC_TYPE_I128:
        case SC_SPEC_TYPE_U256:
        case SC_SPEC_TYPE_I256:
        case SC_SPEC_TYPE_BYTES:
        case SC_SPEC_TYPE_STRING:
        case SC_SPEC_TYPE_SYMBOL:
        case SC_SPEC_TYPE_ADDRESS:
            void;
        case SC_SPEC_TYPE_OPTION:
            SCSpecTypeOption option;
        case SC_SPEC_TYPE_RESULT:
            SCSpecTypeResult result;
        case SC_SPEC_TYPE_VEC:
            SCSpecTypeVec vec;
        case SC_SPEC_TYPE_MAP:
            SCSpecTypeMap map;
        case SC_SPEC_TYPE_SET:
            SCSpecTypeSet set;
        case SC_SPEC_TYPE_TUPLE:
            SCSpecTypeTuple tuple;
        case SC_SPEC_TYPE_BYTES_N:
            SCSpecTypeBytesN bytesN;
        case SC_SPEC_TYPE_UDT:
            SCSpecTypeUDT udt;
        };
    """

    def __init__(
        self,
        type: SCSpecType,
        option: SCSpecTypeOption = None,
        result: SCSpecTypeResult = None,
        vec: SCSpecTypeVec = None,
        map: SCSpecTypeMap = None,
        set: SCSpecTypeSet = None,
        tuple: SCSpecTypeTuple = None,
        bytes_n: SCSpecTypeBytesN = None,
        udt: SCSpecTypeUDT = None,
    ) -> None:
        self.type = type
        self.option = option
        self.result = result
        self.vec = vec
        self.map = map
        self.set = set
        self.tuple = tuple
        self.bytes_n = bytes_n
        self.udt = udt

    @classmethod
    def from_sc_spec_type_val(cls) -> "SCSpecTypeDef":
        return cls(SCSpecType.SC_SPEC_TYPE_VAL)

    @classmethod
    def from_sc_spec_type_bool(cls) -> "SCSpecTypeDef":
        return cls(SCSpecType.SC_SPEC_TYPE_BOOL)

    @classmethod
    def from_sc_spec_type_void(cls) -> "SCSpecTypeDef":
        return cls(SCSpecType.SC_SPEC_TYPE_VOID)

    @classmethod
    def from_sc_spec_type_status(cls) -> "SCSpecTypeDef":
        return cls(SCSpecType.SC_SPEC_TYPE_STATUS)

    @classmethod
    def from_sc_spec_type_u32(cls) -> "SCSpecTypeDef":
        return cls(SCSpecType.SC_SPEC_TYPE_U32)

    @classmethod
    def from_sc_spec_type_i32(cls) -> "SCSpecTypeDef":
        return cls(SCSpecType.SC_SPEC_TYPE_I32)

    @classmethod
    def from_sc_spec_type_u64(cls) -> "SCSpecTypeDef":
        return cls(SCSpecType.SC_SPEC_TYPE_U64)

    @classmethod
    def from_sc_spec_type_i64(cls) -> "SCSpecTypeDef":
        return cls(SCSpecType.SC_SPEC_TYPE_I64)

    @classmethod
    def from_sc_spec_type_timepoint(cls) -> "SCSpecTypeDef":
        return cls(SCSpecType.SC_SPEC_TYPE_TIMEPOINT)

    @classmethod
    def from_sc_spec_type_duration(cls) -> "SCSpecTypeDef":
        return cls(SCSpecType.SC_SPEC_TYPE_DURATION)

    @classmethod
    def from_sc_spec_type_u128(cls) -> "SCSpecTypeDef":
        return cls(SCSpecType.SC_SPEC_TYPE_U128)

    @classmethod
    def from_sc_spec_type_i128(cls) -> "SCSpecTypeDef":
        return cls(SCSpecType.SC_SPEC_TYPE_I128)

    @classmethod
    def from_sc_spec_type_u256(cls) -> "SCSpecTypeDef":
        return cls(SCSpecType.SC_SPEC_TYPE_U256)

    @classmethod
    def from_sc_spec_type_i256(cls) -> "SCSpecTypeDef":
        return cls(SCSpecType.SC_SPEC_TYPE_I256)

    @classmethod
    def from_sc_spec_type_bytes(cls) -> "SCSpecTypeDef":
        return cls(SCSpecType.SC_SPEC_TYPE_BYTES)

    @classmethod
    def from_sc_spec_type_string(cls) -> "SCSpecTypeDef":
        return cls(SCSpecType.SC_SPEC_TYPE_STRING)

    @classmethod
    def from_sc_spec_type_symbol(cls) -> "SCSpecTypeDef":
        return cls(SCSpecType.SC_SPEC_TYPE_SYMBOL)

    @classmethod
    def from_sc_spec_type_address(cls) -> "SCSpecTypeDef":
        return cls(SCSpecType.SC_SPEC_TYPE_ADDRESS)

    @classmethod
    def from_sc_spec_type_option(cls, option: SCSpecTypeOption) -> "SCSpecTypeDef":
        return cls(SCSpecType.SC_SPEC_TYPE_OPTION, option=option)

    @classmethod
    def from_sc_spec_type_result(cls, result: SCSpecTypeResult) -> "SCSpecTypeDef":
        return cls(SCSpecType.SC_SPEC_TYPE_RESULT, result=result)

    @classmethod
    def from_sc_spec_type_vec(cls, vec: SCSpecTypeVec) -> "SCSpecTypeDef":
        return cls(SCSpecType.SC_SPEC_TYPE_VEC, vec=vec)

    @classmethod
    def from_sc_spec_type_map(cls, map: SCSpecTypeMap) -> "SCSpecTypeDef":
        return cls(SCSpecType.SC_SPEC_TYPE_MAP, map=map)

    @classmethod
    def from_sc_spec_type_set(cls, set: SCSpecTypeSet) -> "SCSpecTypeDef":
        return cls(SCSpecType.SC_SPEC_TYPE_SET, set=set)

    @classmethod
    def from_sc_spec_type_tuple(cls, tuple: SCSpecTypeTuple) -> "SCSpecTypeDef":
        return cls(SCSpecType.SC_SPEC_TYPE_TUPLE, tuple=tuple)

    @classmethod
    def from_sc_spec_type_bytes_n(cls, bytes_n: SCSpecTypeBytesN) -> "SCSpecTypeDef":
        return cls(SCSpecType.SC_SPEC_TYPE_BYTES_N, bytes_n=bytes_n)

    @classmethod
    def from_sc_spec_type_udt(cls, udt: SCSpecTypeUDT) -> "SCSpecTypeDef":
        return cls(SCSpecType.SC_SPEC_TYPE_UDT, udt=udt)

    def pack(self, packer: Packer) -> None:
        self.type.pack(packer)
        if self.type == SCSpecType.SC_SPEC_TYPE_VAL:
            return
        if self.type == SCSpecType.SC_SPEC_TYPE_BOOL:
            return
        if self.type == SCSpecType.SC_SPEC_TYPE_VOID:
            return
        if self.type == SCSpecType.SC_SPEC_TYPE_STATUS:
            return
        if self.type == SCSpecType.SC_SPEC_TYPE_U32:
            return
        if self.type == SCSpecType.SC_SPEC_TYPE_I32:
            return
        if self.type == SCSpecType.SC_SPEC_TYPE_U64:
            return
        if self.type == SCSpecType.SC_SPEC_TYPE_I64:
            return
        if self.type == SCSpecType.SC_SPEC_TYPE_TIMEPOINT:
            return
        if self.type == SCSpecType.SC_SPEC_TYPE_DURATION:
            return
        if self.type == SCSpecType.SC_SPEC_TYPE_U128:
            return
        if self.type == SCSpecType.SC_SPEC_TYPE_I128:
            return
        if self.type == SCSpecType.SC_SPEC_TYPE_U256:
            return
        if self.type == SCSpecType.SC_SPEC_TYPE_I256:
            return
        if self.type == SCSpecType.SC_SPEC_TYPE_BYTES:
            return
        if self.type == SCSpecType.SC_SPEC_TYPE_STRING:
            return
        if self.type == SCSpecType.SC_SPEC_TYPE_SYMBOL:
            return
        if self.type == SCSpecType.SC_SPEC_TYPE_ADDRESS:
            return
        if self.type == SCSpecType.SC_SPEC_TYPE_OPTION:
            if self.option is None:
                raise ValueError("option should not be None.")
            self.option.pack(packer)
            return
        if self.type == SCSpecType.SC_SPEC_TYPE_RESULT:
            if self.result is None:
                raise ValueError("result should not be None.")
            self.result.pack(packer)
            return
        if self.type == SCSpecType.SC_SPEC_TYPE_VEC:
            if self.vec is None:
                raise ValueError("vec should not be None.")
            self.vec.pack(packer)
            return
        if self.type == SCSpecType.SC_SPEC_TYPE_MAP:
            if self.map is None:
                raise ValueError("map should not be None.")
            self.map.pack(packer)
            return
        if self.type == SCSpecType.SC_SPEC_TYPE_SET:
            if self.set is None:
                raise ValueError("set should not be None.")
            self.set.pack(packer)
            return
        if self.type == SCSpecType.SC_SPEC_TYPE_TUPLE:
            if self.tuple is None:
                raise ValueError("tuple should not be None.")
            self.tuple.pack(packer)
            return
        if self.type == SCSpecType.SC_SPEC_TYPE_BYTES_N:
            if self.bytes_n is None:
                raise ValueError("bytes_n should not be None.")
            self.bytes_n.pack(packer)
            return
        if self.type == SCSpecType.SC_SPEC_TYPE_UDT:
            if self.udt is None:
                raise ValueError("udt should not be None.")
            self.udt.pack(packer)
            return

    @classmethod
    def unpack(cls, unpacker: Unpacker) -> "SCSpecTypeDef":
        type = SCSpecType.unpack(unpacker)
        if type == SCSpecType.SC_SPEC_TYPE_VAL:
            return cls(type=type)
        if type == SCSpecType.SC_SPEC_TYPE_BOOL:
            return cls(type=type)
        if type == SCSpecType.SC_SPEC_TYPE_VOID:
            return cls(type=type)
        if type == SCSpecType.SC_SPEC_TYPE_STATUS:
            return cls(type=type)
        if type == SCSpecType.SC_SPEC_TYPE_U32:
            return cls(type=type)
        if type == SCSpecType.SC_SPEC_TYPE_I32:
            return cls(type=type)
        if type == SCSpecType.SC_SPEC_TYPE_U64:
            return cls(type=type)
        if type == SCSpecType.SC_SPEC_TYPE_I64:
            return cls(type=type)
        if type == SCSpecType.SC_SPEC_TYPE_TIMEPOINT:
            return cls(type=type)
        if type == SCSpecType.SC_SPEC_TYPE_DURATION:
            return cls(type=type)
        if type == SCSpecType.SC_SPEC_TYPE_U128:
            return cls(type=type)
        if type == SCSpecType.SC_SPEC_TYPE_I128:
            return cls(type=type)
        if type == SCSpecType.SC_SPEC_TYPE_U256:
            return cls(type=type)
        if type == SCSpecType.SC_SPEC_TYPE_I256:
            return cls(type=type)
        if type == SCSpecType.SC_SPEC_TYPE_BYTES:
            return cls(type=type)
        if type == SCSpecType.SC_SPEC_TYPE_STRING:
            return cls(type=type)
        if type == SCSpecType.SC_SPEC_TYPE_SYMBOL:
            return cls(type=type)
        if type == SCSpecType.SC_SPEC_TYPE_ADDRESS:
            return cls(type=type)
        if type == SCSpecType.SC_SPEC_TYPE_OPTION:
            option = SCSpecTypeOption.unpack(unpacker)
            return cls(type=type, option=option)
        if type == SCSpecType.SC_SPEC_TYPE_RESULT:
            result = SCSpecTypeResult.unpack(unpacker)
            return cls(type=type, result=result)
        if type == SCSpecType.SC_SPEC_TYPE_VEC:
            vec = SCSpecTypeVec.unpack(unpacker)
            return cls(type=type, vec=vec)
        if type == SCSpecType.SC_SPEC_TYPE_MAP:
            map = SCSpecTypeMap.unpack(unpacker)
            return cls(type=type, map=map)
        if type == SCSpecType.SC_SPEC_TYPE_SET:
            set = SCSpecTypeSet.unpack(unpacker)
            return cls(type=type, set=set)
        if type == SCSpecType.SC_SPEC_TYPE_TUPLE:
            tuple = SCSpecTypeTuple.unpack(unpacker)
            return cls(type=type, tuple=tuple)
        if type == SCSpecType.SC_SPEC_TYPE_BYTES_N:
            bytes_n = SCSpecTypeBytesN.unpack(unpacker)
            return cls(type=type, bytes_n=bytes_n)
        if type == SCSpecType.SC_SPEC_TYPE_UDT:
            udt = SCSpecTypeUDT.unpack(unpacker)
            return cls(type=type, udt=udt)
        return cls(type=type)

    def to_xdr_bytes(self) -> bytes:
        packer = Packer()
        self.pack(packer)
        return packer.get_buffer()

    @classmethod
    def from_xdr_bytes(cls, xdr: bytes) -> "SCSpecTypeDef":
        unpacker = Unpacker(xdr)
        return cls.unpack(unpacker)

    def to_xdr(self) -> str:
        xdr_bytes = self.to_xdr_bytes()
        return base64.b64encode(xdr_bytes).decode()

    @classmethod
    def from_xdr(cls, xdr: str) -> "SCSpecTypeDef":
        xdr_bytes = base64.b64decode(xdr.encode())
        return cls.from_xdr_bytes(xdr_bytes)

    def __eq__(self, other: object):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return (
            self.type == other.type
            and self.option == other.option
            and self.result == other.result
            and self.vec == other.vec
            and self.map == other.map
            and self.set == other.set
            and self.tuple == other.tuple
            and self.bytes_n == other.bytes_n
            and self.udt == other.udt
        )

    def __str__(self):
        out = []
        out.append(f"type={self.type}")
        out.append(f"option={self.option}") if self.option is not None else None
        out.append(f"result={self.result}") if self.result is not None else None
        out.append(f"vec={self.vec}") if self.vec is not None else None
        out.append(f"map={self.map}") if self.map is not None else None
        out.append(f"set={self.set}") if self.set is not None else None
        out.append(f"tuple={self.tuple}") if self.tuple is not None else None
        out.append(f"bytes_n={self.bytes_n}") if self.bytes_n is not None else None
        out.append(f"udt={self.udt}") if self.udt is not None else None
        return f"<SCSpecTypeDef [{', '.join(out)}]>"
