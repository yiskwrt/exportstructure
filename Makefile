

sample_mqsend:
	python -m examples.posix_mq.qsend

sample_mqsend2:
	python -m examples.posix_mq.qsend2 < examples/posix_mq/bodysample.yaml

sample_mqrecv:
	python -m examples.posix_mq.qrecv

sample_mqremove:
	python -m examples.posix_mq.qremove
