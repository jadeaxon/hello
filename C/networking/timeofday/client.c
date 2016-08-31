
#include "unp.h"

int main(int argc, char** argv) {
	int sockfd; // Socket file descriptor.  Everything is a file.
	int n; // Number of bytes read from socket.
	char recvline[MAXLINE + 1];  // Buffer for received line.
	
	// Internet socket (TCP socket) address structure.
	struct sockaddr_in servaddr;
	
	if (argc != 2) {
		err_quit("usage: a.out <IPaddress>");
	}

	// Open a file descriptor for a TCP socket.
	if ( (sockfd = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
		err_sys("socket error");
	}
	
	bzero(&servaddr, sizeof(servaddr)); // Zero out the variable.
	servaddr.sin_family = AF_INET; // An Internet socket (vs. a Unix socket).
	
	// htons is some kind of network byte order converter: host to network short.
	// Port 13.  Well-know address of daytime server on Linux machines.
	servaddr.sin_port = htons(13); /* daytime server */
	
	// Presentation to numeric.  Convert ASCII IP addy into proper form for sockets API consumption.
	// Converts in place to serveradder.sin_addr.
	// Older code uses inet_addr().  This inet_pton() is new for IPv6.  Works better with IPv4 too.
	if (inet_pton(AF_INET, argv[1], &servaddr.sin_addr) <= 0) {
		// Unable to convert IP addy to proper form.
		err_quit("inet_pton error for %s", argv[1]);
	}
	
	// Connect local client socket to server address.
	if (connect(sockfd, (SA*) &servaddr, sizeof(servaddr)) < 0) {
		// Could not connect to socket.
		err_sys("connect error");
	}
	
	// Read from the socket.
	// This is basically the same read function used to read from normal local files.
	while ( (n = read(sockfd, recvline, MAXLINE)) > 0) {
		recvline[n] = 0; /* null terminate */
		if (fputs(recvline, stdout) == EOF) {
			err_sys("fputs error");
		}
	}
	
	if (n < 0) {
		err_sys("read error");
	}

	exit(0);

} // main(...)

