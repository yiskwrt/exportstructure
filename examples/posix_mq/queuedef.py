import ctypes

class MemberHoge(ctypes.Structure):
    _fields_ = [
        ("xpos", ctypes.c_uint32),
        ("ypos", ctypes.c_uint32),
        ("score", ctypes.c_uint32),
        ("descr", ctypes.c_uint32),
    ]

class MsgBody(ctypes.Structure):
    _fields_ = [
        ("foo", ctypes.c_uint32),
        ("bar", ctypes.c_uint32),
        ("hoge", MemberHoge * 4),
    ]

MQUEUE_NAME="/mqpy_test1"
