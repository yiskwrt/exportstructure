import posix_ipc as ipc
import queuedef

ipc.unlink_message_queue(queuedef.MQUEUE_NAME)
