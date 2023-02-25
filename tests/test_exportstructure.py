import ctypes
from exportstructure import exportstructure as es

class MemberHoge(ctypes.Structure):
    _fields_ = [
        ("asd", ctypes.c_uint32),
        ("qwe", ctypes.c_uint32),
    ]

class MsgBody(ctypes.Structure):
    _fields_ = [
        ("foo", ctypes.c_uint32),
        ("bar", ctypes.c_uint32),
        ("piyo", ctypes.c_uint32 * 4),
        ("piyopiyo", (ctypes.c_int32 * 2) * 2),
        ("hoge", MemberHoge),
        ("hogehoge", MemberHoge * 4),
    ]

def test_export_import():
    print(MemberHoge)
    print(MsgBody)

    msgbody1 = MsgBody()
    msgbody1.foo=1
    msgbody1.bar=2
    msgbody1.piyo[0] = 3
    msgbody1.piyo[1] = 4
    msgbody1.piyo[2] = 5
    msgbody1.piyo[3] = 6
    msgbody1.piyopiyo[0][0] = 7
    msgbody1.piyopiyo[0][1] = 8
    msgbody1.piyopiyo[1][0] = 9
    msgbody1.piyopiyo[1][1] = 10
    msgbody1.hoge.asd = 11
    msgbody1.hoge.qwe = 12
    msgbody1.hogehoge[0].asd = 13
    msgbody1.hogehoge[0].qwe = 14
    msgbody1.hogehoge[1].asd = 13
    msgbody1.hogehoge[1].qwe = 14
    msgbody1.hogehoge[2].asd = 13
    msgbody1.hogehoge[2].qwe = 14
    msgbody1.hogehoge[3].asd = 13
    msgbody1.hogehoge[3].qwe = 14
    es.print_item(msgbody1, "**")
    obj1 = es.export_item(msgbody1)
    print(obj1)

    msgbody2 = MsgBody()
    es.import_item(msgbody2, obj1)
    obj2 = es.export_item(msgbody2)
    print(obj2)

    seq1=bytes(msgbody1)
    seq2=bytes(msgbody2)

    assert obj1==obj2
    assert seq1==seq2
