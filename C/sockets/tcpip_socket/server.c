#include <sys/socket.h> // socket()
#include <arpa/inet.h>
#include <string.h> // strlen()
#include <stdio.h> // puts()

// This is my Nice Things C library.
// It currently is deployed to $HOME/lib/.
#include <nt_error.h> // nt_error()

// Make e() alias for nt_error().
void (*e)(int, char*) = nt_error; 

int main(int argc, char** argv) {
	// e(-1, "Fail test using alias"); // Works!

	// BLAB: bind listen accept begin

	// PF_INET => protocol family Internet (aka, IP-based).
	// SOCK_STREAM => TCP (a coherent stream of data unlike UDP)
	int listener_d = socket(PF_INET, SOCK_STREAM, 0); // Listener socket descriptor.
	e(listener_d, "Can't open socket");

	// Create a socket address.  Bind a socket to it.
	struct sockaddr_in address;
	address.sin_family = PF_INET;
	address.sin_port = (in_port_t)htons(30000); // The TCP port we listen on.
	address.sin_addr.s_addr = htonl(INADDR_ANY);
	int r = bind(listener_d, (struct sockaddr *) &address, sizeof(address));
	e(r, "Can't bind to socket");

	puts("Listening for new connection");
	r = listen(listener_d, 10); // 10 is waiting queue length.  Others will be dropped.
	e(r, "Can't listen");

	// Accept the connection.  When a connection is accepted, a new socket is created.
	// Communication with client happens on the new socket.
	// The server continues listening on the main sockets.
	// It's like how when you call a business the secretary connects you to the actual number.
	// Since this server is single threaded, it's like the secretary connects the call to the other
	// line but then walks across the room and picks it up herself!  All other incoming calls will
	// have to wait.
	struct sockaddr_storage client_addr;
	unsigned int address_size = sizeof(client_addr);
	int connect_d = accept(listener_d, (struct sockaddr*) &client_addr, &address_size);
	e(connect_d, "Can't open secondary socket");

	// Tell the client what service you provide and what version of its protocol you speak.
	char* msg = "Internet Knock-Knock Protocol Server\r\nVersion 1.0\r\nKnock! Knock!\r\n> ";
	r = send(connect_d, msg, strlen(msg), 0);
	e(r, "send");


} // main(...)


