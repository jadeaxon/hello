#include <sys/socket.h> // socket()

// This is my Nice Things C library.
// It currently is deployed to $HOME/lib/.
#include <nt_error.h> // nt_error()

int main(int argc, char** argv) {

	// PF_INET => protocol family Internet (aka, IP-based).
	// SOCK_STREAM => TCP (a coherent stream of data unlike UDP)
	int listener_d = socket(PF_INET, SOCK_STREAM, 0);
	nt_error(listener_d, "Can't open socket");

}


