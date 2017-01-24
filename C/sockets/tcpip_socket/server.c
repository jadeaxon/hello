#include <sys/socket.h> // socket()
#include <arpa/inet.h>

// This is my Nice Things C library.
// It currently is deployed to $HOME/lib/.
#include <nt_error.h> // nt_error()

// Make e() alias for nt_error().
void (*e)(int, char*) = nt_error; 

int main(int argc, char** argv) {
	// e(-1, "Fail test using alias"); // Works!

	// PF_INET => protocol family Internet (aka, IP-based).
	// SOCK_STREAM => TCP (a coherent stream of data unlike UDP)
	int listener_d = socket(PF_INET, SOCK_STREAM, 0); // Listener socket descriptor.
	e(listener_d, "Can't open socket");

	// Create a socket address.  Bind a socket to it.
	struct sockaddr_in address;
	address.sin_family = PF_INET;
	address.sin_port = (in_port_t)htons(30000);
	address.sin_addr.s_addr = htonl(INADDR_ANY);
	int result = bind(listener_d, (struct sockaddr *) &address, sizeof(address));
	e(result, "Can't bind to socket");

} // main(...)


