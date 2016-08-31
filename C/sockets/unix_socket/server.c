// Standard C library.
#include <sys/types.h>
#include <sys/socket.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/un.h>
#include <stdio.h>


// Function prototype.
void error(const char*);


// Implements a Unix socket server.
// First arg is the name of the socket.
int main(int argc, char* argv[]) {
	if (argc != 2) {
		// If you let this code without an arg, it will core dump.
		printf("Usage: server.exe <socket name>\n");
		printf("Example: ./server.exe unixsocket\n");
		exit(1);
	}

	// If file already exists, socket binding will crash later.
	unlink(argv[1]);

	int server_socket_fd = 0; // Server socket file descriptor. 
	int connection_socket_fd = 0; // New connection socket file descriptor.
	int server_address_length = 0; // ?
	int n = 0; // Number of bytes read (or to write).

	// sun => socket Unix	
	socklen_t sockaddr_un_size = 0;
	struct sockaddr_un client_address;
	struct sockaddr_un server_address;

	// This is what a struct sockaddr_un looks like:
	/*
	struct sockaddr_un {
		shortsun_family; // AF_UNIX
		charsun_path[108]; // path
	};
	*/

	char buffer[80];

	// Get a handle (file descriptor) for the server socket.
	if ((server_socket_fd = socket(AF_UNIX, SOCK_STREAM, 0)) < 0) {
		error("creating socket");
	}

	// These really are file descriptors.  Small numeric indexes into the file descriptor table for a process.
	// For example, 1 is stdout.  Modern Linux allows 1024 per process.  Cygwin allows 256.

	// A socket has an address domain (address family) and socket type.
	// AF_UNIX => Unix domain socket.
	// The other domain is the Internet domain (IP protocol).
	// Unix domain sockets only have one type: file (named pipe).
	// Internet domain sockets come in two flavors: UDP (datagram) and TCP.
	// Thus, we can create Unix, TCP/IP, and UDP/IP sockets for bidirectional IPC. 
	// Possibly globally networked IPC.

	// Set up args for binding socket to its address.
	bzero( (char*)&server_address, sizeof(server_address) ); // Sets n values in given buffer to 0.
	server_address.sun_family = AF_UNIX;
	strcpy(server_address.sun_path, argv[1]);
	server_address_length = strlen(server_address.sun_path) + sizeof(server_address.sun_family);

	// Bind the file descriptor (socket) to an address.
	// In the case of a Unix socket, the address is just a local file.
	// The socket and its address are two different "files".
	// You have to do the cast here because struct sockaddr* is the type bind() expects.
	if( bind(server_socket_fd, (struct sockaddr*)&server_address, server_address_length) < 0 ) {
		// If the local file you are binding two already exists, you will get an error.
		// I'm surprised that closing the socket does not remove this file.
		error("binding socket"); 
	}

	// Loop forever responding to client requests.
	while (1) {
		// Start listening for client connections.
		// Second arg is the maximum pending connection queue length before connections are refused.
		listen(server_socket_fd, 5);

		// When a connection is requested by a client socket, a new socket is created to handle that connection.
		// That is, you "accept" the connection.  Kind of like an old telephone switchboard operator.
		// The server socket just continues to listen for connection requests.
		
		// The size of a sockaddr_un struct.  Why exactly we need to pass this value, I know not.
		sockaddr_un_size = sizeof(client_address); 

		// accept() blocks until a client makes a connection.
		connection_socket_fd = accept(server_socket_fd, (struct sockaddr*)&client_address, &sockaddr_un_size);
		if (connection_socket_fd < 0) {
			error("accepting");
		}
		printf("A connection has been established!\n");
		
		bzero(&buffer, 80); // Zero out buffer so it acts like a C string.
		// This assumes that the request will have at most 79 characters in it.
		n = read(connection_socket_fd, buffer, 80); // Read at most 80 characters.
		printf("n = %d\n", n);
		printf("strlen(buffer) = %d\n", strlen(buffer));

		write(1, buffer, n); // Writes to file descriptor 1: stdout.

		// Server response.  Just echo back what we received.
		write(connection_socket_fd, buffer, n); // Write n bytes from given buffer (char*).
	
	} // next request
	
	close(connection_socket_fd); // Close the connection socket.
	close(server_socket_fd); // Close the server socket.

	return 0;
} // main(...)


// Exits on error.
void error(const char* msg) {
	// perror => print error
	// Turn global errno into a string and appends optional string arg.
	perror(msg);
	exit(2);
}


