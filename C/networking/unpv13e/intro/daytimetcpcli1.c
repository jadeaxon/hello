// The book's library header.
#include "unp.h"

int main(int argc, char** argv) {
	int	sockfd; // Socket file descriptor.
	int n = 0; // Number of bytes read.
	int counter = 0; // Number of reads from socket to get full response.
	char recvline[MAXLINE + 1]; // The receive buffer.
	struct sockaddr_in servaddr; // Internet socket address structure.

	if (argc != 2)
		err_quit("usage: a.out <IPaddress>");

	// Associate the file descriptor with an Internet socket.
	// So, now we have the client end of the socket.  
	// A socket connection (like a guitar cable) has two endpoints.
	// First you connect to the guitar (client) then to the server (amp).
	if ( (sockfd = socket(AF_INET, SOCK_STREAM, 0)) < 0)
		err_sys("socket error");

	bzero(&servaddr, sizeof(servaddr)); // Zero out the struct instance.  Safer than memset().
	servaddr.sin_family = AF_INET; // Internet socket (TCP socket).
	
	// Port 13 is well-known port of time-of-day service.
	// htons => host (way of storing numbers) to network short
	// So, maybe a 64-bit little endian integer becomes a 16-bit big endian short int (?).
	servaddr.sin_port = htons(13);	

	// Client port is not same as server port.  A randomish available port will be given to the
	// client socket endpoint on connection.  Server port generally stays fixed.
	// Server is typically multithreaded to handle multiple simultaneous client requests.
	// The worker threads just respond.  Stateless protocol.

	// Presentation to network.  An IPv6 function that replaces inet_addr().  Also works with IPv4.
	if (inet_pton(AF_INET, argv[1], &servaddr.sin_addr) <= 0)
		err_quit("inet_pton error for %s", argv[1]);

	// Connect to the remote server socket.
	if (connect(sockfd, (SA*) &servaddr, sizeof(servaddr)) < 0)
		err_sys("connect error");

	// Read from the socket (as if it were a local file).
	// TCP doesn't have end-of-record markers, so you just have to keep reading until zero bytes are
	// sent.  Append each chunk to a receive buffer.
	while ( (n = read(sockfd, recvline, MAXLINE)) > 0) {
		counter++;
		recvline[n] = 0;	/* null terminate */
		if (fputs(recvline, stdout) == EOF)
			err_sys("fputs error");
	}
	if (n < 0)
		err_sys("read error");

	// How many reads did it take from the socket to get the full response?
	printf("counter = %d\n", counter);
	exit(0);
} // main(...)

