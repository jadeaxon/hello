// C
#include <sys/socket.h> // socket()
#include <arpa/inet.h> // htons()
#include <netdb.h> // getaddrinfo() -- DNS lookup
#include <string.h> // strlen()
#include <stdio.h> // puts()
#include <stdlib.h> // exit()
#include <unistd.h> // fork()
#include <signal.h> // SIGINT

// Nice Things
// It currently is deployed to $HOME/lib/.
#include <nt_error.h> // nt_error()
#include <nt_signal.h> // nt_register_signal_handler()

// Make e() alias for nt_error().
void (*e)(int, char*) = nt_error; 


int open_socket(char* host, char* port);
int say(int socket, char* s);


// Requests a hard-coded web page via HTTP.  Prints response to stdout.
int main(int argc, char** argv) {
	// Connect via IP address.
	/*
	int s = socket(PF_INET, SOCK_STREAM, 0);
	e(s, "Failed to create socket");
	
	struct sockaddr_in si;
	memset(&si, 0, sizeof(si));
	si.sin_family = PF_INET;
	si.sin_addr.s_addr = inet_addr("208.201.239.100");
	si.sin_port = htons(80);
	connect(s, (struct sockaddr *) &si, sizeof(si));
	*/

	// Connect using DNS.
	// It appears Wikipedia requires HTTPS connections, so our HTTP request gets us nothing back.
	// So, I'm just going to request a simple web page from another site.
	// int socket = open_socket("en.wikipedia.org", "80");
	// https://nethackwiki.com/wiki/NetHack	
	int socket = open_socket("nethackwiki.com", "80");
	char buf[256];
	
	// Send HTTP GET request.
	char* GET = "GET /wiki/NetHack http/1.1\r\n";
	// sprintf(buf, GET, argv[1]);
	say(socket, GET);
	say(socket, "Host: nethackwiki.com\r\n\r\n");
	
	// Read the response.
	int bytes = recv(socket, buf, 255, 0);
	while (bytes) {
		e(bytes, "Can't read from server");
		buf[bytes] = '\0';
		printf("%s", buf);
		// It seems if server does not close connection after all data sent, this call will hang forever.
		bytes = recv(socket, buf, 255, 0);
	} // next subseq of bytes

	puts("HERE!");
	close(socket);

} // main(void)


// Opens a TCP/IP socket to given host on given port.
// Returns the socket descriptor.
int open_socket(char* host, char* port) {
	// We use a string for port because it could be a service name.
	struct addrinfo* res; // Naming resource.  Basically a DNS response.
	struct addrinfo hints;
	memset(&hints, 0, sizeof(hints));
	hints.ai_family = PF_UNSPEC; // ???
	hints.ai_socktype = SOCK_STREAM;
	// Q. Why are we using &res when we're already passing a pointer?
	int r = getaddrinfo(host, port, &hints, &res);
	if (r != 0) {
		puts("ERROR: DNS lookup failed.");
		exit(1);
	}

	int s = socket(res->ai_family, res->ai_socktype, res->ai_protocol);
	e(s, "Failed to create socket");

	int c = connect(s, res->ai_addr, res->ai_addrlen);
	e(c, "Can't connect to socket");	

	freeaddrinfo(res); // Free naming resource mem on heap.
	return s;

} // open_socket(...)


// Writes a string out to a socket.
int say(int socket, char* s) {
	int r = send(socket, s, strlen(s), 0);
	e(r, "Error talking to the client");
	return r;
}



