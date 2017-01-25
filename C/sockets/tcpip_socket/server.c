#include <sys/socket.h> // socket()
#include <arpa/inet.h>
#include <string.h> // strlen()
#include <stdio.h> // puts()
#include <stdlib.h> // exit()
#include <unistd.h> // ???
#include <signal.h> // SIGINT


// This is my Nice Things C library.
// It currently is deployed to $HOME/lib/.
#include <nt_error.h> // nt_error()
#include <nt_signal.h> // nt_register_signal_handler()

int recv_line(int socket, char* buf, int len);
void handle_shutdown(int sig);
void bind_to_port(int socket, int port);


// Make e() alias for nt_error().
void (*e)(int, char*) = nt_error; 

int listener_d; // The listener socket descriptor.


int main(int argc, char** argv) {
	// e(-1, "Fail test using alias"); // Works!
	int r = 0; // Return value from future system calls.
	
	r = nt_register_signal_handler(SIGINT, handle_shutdown);
	e(r, "Failed to register signal handler");

	// BLAB: bind listen accept begin
	listener_d = open_listener_socket();
	bind_to_port(listener_d, 30000);
	
	puts("Listening for new connection");
	char buf[255];
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
	
	while (1) {
		int connect_d = accept(listener_d, (struct sockaddr*) &client_addr, &address_size);
		e(connect_d, "Can't open secondary socket");

		// Tell the client what service you provide and what version of its protocol you speak.
		char* msg = "Internet Knock-Knock Protocol Server\r\nVersion 1.0\r\nKnock! Knock!\r\n> ";
		say(connect_d, msg);
		recv_line(connect_d, buf, sizeof(buf));
		if (strncasecmp("Who's there?", buf, 12)) {
			say(connect_d, "You should say \"Who's there?\".");
		}
		else { // Client asked "Who's there?".
			say(connect_d, "Oscar\r\n> ");
			recv_line(connect_d, buf, sizeof(buf));
			if (strncasecmp("Oscar who?", buf, 10)) {
				say(connect_d, "You should say \"Oscar who?\".\r\n");
			}
			else {
				say(connect_d, "Oscar silly question, get a silly answer!\r\n");
			}
		} // else

		// This knock-knock session is over.  Listen for a new connection.
		close(connect_d);
	} // next connection
	
	return 0;
} // main(...)


// Receives/reads a line of text from a socket.  Stores it in given buffer as a C string.
// POST: The newline is stripped from the string.  Assumes \r\n line terminators.
int recv_line(int socket, char* buf, int len) {
	char* s = buf; // Location in buffer to read data into.
	int slen = len; // Remaining length of buffer.
	
	int c = recv(socket, s, slen, 0);
	while ((c > 0) && (s[c-1] != '\n')) {
		s += c; slen -= c;
		c = recv(socket, s, slen, 0);
	}
	
	// Return error code or null terminate string.
	if (c < 0)
		return c;
	else if (c == 0)
		buf[0] = '\0';
	else
		s[c-1]='\0';

	return len - slen; // Number of chars read into buffer.
} // recv_line(...)


// Opens a listener socket.
int open_listener_socket() {
	// PF_INET => protocol family Internet (aka, IP-based).
	// SOCK_STREAM => TCP (a coherent stream of data unlike UDP)
	int s = socket(PF_INET, SOCK_STREAM, 0);
	e(s, "Can't open socket");
	return s;
}


// Binds a socket to a port.
void bind_to_port(int socket, int port) {
	// Create a socket address.  Bind a socket to it.
	struct sockaddr_in address;
	address.sin_family = PF_INET;
	address.sin_port = (in_port_t)htons(30000); // The TCP port we listen on.
	address.sin_addr.s_addr = htonl(INADDR_ANY);
	
	// Allow previously bound port to be reused quickly.  Like if the server stops and then starts
	// again quickly.
	int reuse = 1;
	int r = setsockopt(socket, SOL_SOCKET, SO_REUSEADDR, (char*)&reuse, sizeof(int));
	e(r, "Can't set the reuse option on the socket");

	r = bind (socket, (struct sockaddr*) &address, sizeof(address));
	e(r, "Can't bind to socket");
}


// Writes a string out to a socket.
int say(int socket, char* s) {
	int r = send(socket, s, strlen(s), 0);
	e(r, "Error talking to the client");
	return r;
}


// Handles SIGINT signal.
void handle_shutdown(int sig) {
	if (listener_d)
		close(listener_d);
	fprintf(stderr, "Bye!\n");
	exit(0);
}


