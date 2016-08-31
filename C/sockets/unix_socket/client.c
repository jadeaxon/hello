// Standard C library
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <sys/un.h>
#include <stdio.h>


// Function prototype.
void error(const char*);


// Implements a Unix socket client.
int main(int argc, char* argv[]) {
	if (argc != 2) {
		printf("Usage: client.exe <socket name>\n");
		printf("Example: ./client.exe unixsocket\n");
		exit(1);
	}

	int sockfd = 0; // Socket file descriptor. 
	int server_address_length = 0; // Length of server address. 
	int n = 0; // Number of bytes read or to write.

	struct sockaddr_un server_address; // Unix socket address of server socket.
	char buffer[82]; // Buffer to hold message sent/received.

	// I'm guessing this initializes all the bytes to 0.  Yes, it does.
	bzero( (char*)&server_address, sizeof(server_address) );
	
	// First commandline arg is the name of the Unix socket.
	// I believe the file ends up just being /tmp/<arg>.
	server_address.sun_family = AF_UNIX; // Unix domain socket.
	strcpy(server_address.sun_path, argv[1]); // 1st commandline arg is socket name (address).

	// The server will have already connected to this address and be listening.
	// In a Unix socket, the address is really just the path of a local file.
	// For an Internet socket, the address would be an IP address and a port.
	
	server_address_length = strlen(server_address.sun_path) + sizeof(server_address.sun_family);

	// Send requests forever.
	int request = 0; // Used to special case first request.
	while (1) {
		// TO DO: Program hung when I tried to send multiple messages on the same connection.
		// So, I now make a new client connection for each request.

		// We create a socket and get a handle to it (a file descriptor).
		if ((sockfd = socket(AF_UNIX, SOCK_STREAM, 0)) < 0) {
			error("Creating socket");
		}

		// Now, we connect this our end of the socket to the server.
		// That is, we request a connection.
		if (connect(sockfd, (struct sockaddr*) &server_address, server_address_length) < 0) {
			error("Connecting");
		}
		if (request == 0) {
			printf("Connected to %s.\n", argv[1]);
			printf("Press <Ctrl + C> to exit.\n");
		}

		// Now we send a message to the server.
		printf("Please enter your message: ");
		bzero(buffer, 82); // Zero out our string buffer.
		fgets(buffer, 80, stdin); // Read a string from stdin.  At *most* 80 characters.

		// Request response from server.
		int result = write(sockfd, buffer, strlen(buffer));
		if (result == -1) {
			error("Writing to socket");
		}

		n = read(sockfd, buffer, 80);
		printf("Response: ");
		fflush(stdout); // Flush stdout else response appears before this prefix!

		// Is this an ACK?  No, we are writing to file descriptor 1: stdout.
		// I think this is because buffer is not a null-terminate string.
		write(1, buffer, n);
	
		close(sockfd); // Close our connection.
		request++;
	} // next request
	

	return 0;
} // main(...)


// Exits on error.
void error(const char* msg) {
    perror(msg);
    exit(2);
}



