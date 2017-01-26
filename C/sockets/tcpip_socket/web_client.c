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
// It currently is deployed to $HOME/lib/ and /usr/local/lib.
#include <nt_error.h> // nt_error()
#include <nt_signal.h> // nt_register_signal_handler()

// Make e() alias for nt_error().
void (*e)(int, char*) = nt_error; 


int open_socket(char* host, char* port);
int say(int socket, char* s);


// Requests a hard-coded web page via HTTP.  Prints response to stdout.
int main(int argc, char** argv) {
	const int D = 0; // Print debug output?	
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
	int total_bytes = 0;
	int bytes = recv(socket, buf, 255, 0);
	int expected_bytes = -1;
	char line[1024]; // Buffer for HTTP header lines.	
	char* li = line; // Line buffer index.	
	int beyond_headers = 0; // Are we done processing HTTP headers?
	
	while (bytes) {
		e(bytes, "Can't read from server");
		buf[bytes] = '\0';
		printf("%s", buf);
		D && printf("___\n"); // Show receive buffer boundaries.
	
		// We have to turn the raw response chunks into individual lines so we can parse out the
		// response length so that we don't hang forever on the last recv().  A line may be broken
		// between two buffer loads of response and a buffer load may contain multiple lines.
		// Also, the content length is *after* all headers have been processed.  It does not count
		// the header bytes.	
		char* i = buf;
		int buffer_index = 0;
		int lines = 0;
		while (1) {
			int line_complete = 0;
			while (*i != '\0') {
				D && printf("buf[%d] = %c\n", buffer_index, *i);
				if (*i == '\n') {
					line_complete = 1;
					li--; // Headers use \r\n, so we'll chop that off.
					i++; buffer_index++;
					break;
				}
				*li = *i; // Fill the line buffer.
				li++;
				i++; buffer_index++;
			} // next char in response buffer
			if (line_complete) {
				*li = '\0';	
				D && printf("LINE: %s\n", line);
				
				// A single empty line designates the end of HTTP headers.		
				if (!beyond_headers && strlen(line) == 0) {
					D && printf("\n");
					D && printf("Finished processing HTTP headers.\n");	
					D && printf(" expected_bytes = %d\n", expected_bytes);
					beyond_headers = 1;
					// Part of this buffer load is response data.
					D && printf(" bytes = %d\n", bytes);
					D && printf(" buffer_index = %d\n", buffer_index);
					total_bytes += (bytes - buffer_index); // ??? Feels like this is off by one, but total comes out right.
					D && printf(" total_bytes = %d\n", total_bytes);
				}

				// Check 'Content Length:' HTTP header so we don't hang forever on recv().
				if ( strstr(line, "Content-Length: ") == line ) {
					nt_keep_chars(line, "0123456789");
					expected_bytes = atoi(line);
					D && printf("expected_bytes = %d\n", expected_bytes);
				}
				li = line; // Point back to beginning of line.
				lines++;
			}
			else { // Line was not complete.
				break; // Need to read more response from server.
			}
			/*
			if (lines >= 2) {
				exit(1);
			}
			*/
		} // next potential line in response buffer

		// Don't read anymore bytes if we've already read the expected amount.
		if ((expected_bytes != -1) && (total_bytes >= expected_bytes)) {
			break; // We've read all the bytes in the response.
		}
		
		// It seems if server does not close connection after all data sent, this call will hang forever.
		bytes = recv(socket, buf, 255, 0);
		if (beyond_headers) total_bytes += bytes;
		D && printf("total_bytes = %d\n", total_bytes);
	} // next subseq of bytes

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



