import posix_ipc as ipc
import queuedef
from exportstructure import exportstructure as es
import ctypes
from ctypes import memmove, pointer, sizeof

msgbody = queuedef.MsgBody()

mq = ipc.MessageQueue(queuedef.MQUEUE_NAME, ipc.O_CREAT, 0o666, 10, sizeof(msgbody), True, False)

(qmsg, prio) = mq.receive()
memmove(pointer(msgbody), qmsg, sizeof(msgbody))

es.print_item(msgbody, "##")
