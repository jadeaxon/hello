include ../Make.defines

PROGS =	client client1 client2 client3 \
		server server1 server2 server3 \
		clientv6 serverv6 \
		byteorder

all:	${PROGS}

client:	daytimetcpcli.o
		${CC} ${CFLAGS} -o $@ daytimetcpcli.o ${LIBS}

client1:	daytimetcpcli1.o
		${CC} ${CFLAGS} -o $@ daytimetcpcli1.o ${LIBS}

client2:	daytimetcpcli2.o
		${CC} ${CFLAGS} -o $@ daytimetcpcli2.o ${LIBS}

client3:	daytimetcpcli3.o
		${CC} ${CFLAGS} -o $@ daytimetcpcli3.o ${LIBS}

server:	daytimetcpsrv.o
		${CC} ${CFLAGS} -o $@ daytimetcpsrv.o ${LIBS}

server1:	daytimetcpsrv1.o
		${CC} ${CFLAGS} -o $@ daytimetcpsrv1.o ${LIBS}

server2:	daytimetcpsrv2.o
		${CC} ${CFLAGS} -o $@ daytimetcpsrv2.o ${LIBS}

server3:	daytimetcpsrv3.o
		${CC} ${CFLAGS} -o $@ daytimetcpsrv3.o ${LIBS}

clientv6:	daytimetcpcliv6.o
		${CC} ${CFLAGS} -o $@ daytimetcpcliv6.o ${LIBS}

serverv6:	daytimetcpsrvv6.o
		${CC} ${CFLAGS} -o $@ daytimetcpsrvv6.o ${LIBS}

byteorder:	byteorder.o
		${CC} ${CFLAGS} -o $@ byteorder.o ${LIBS}

clean:
		rm -f ${PROGS} ${CLEANFILES}
