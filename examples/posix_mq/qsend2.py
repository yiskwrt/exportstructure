import sys
import yaml
import posix_ipc as ipc
import queuedef
from exportstructure import exportstructure as es
import ctypes
from ctypes import sizeof

msgbody = queuedef.MsgBody()

mq = ipc.MessageQueue(queuedef.MQUEUE_NAME, ipc.O_CREAT, 0o666, 10, sizeof(msgbody), False, True)

obj = yaml.safe_load(sys.stdin)
es.import_item(msgbody, obj)
mq.send(bytes(msgbody))
