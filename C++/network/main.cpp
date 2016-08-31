#include <iostream>

#include <cstdio>

// Network crap.
#include <unistd.h>
#include <string.h> /* for strncpy */
#include <sys/types.h>
#include <sys/socket.h>
#include <sys/ioctl.h>
#include <netinet/in.h>
#include <net/if.h>
#include <arpa/inet.h>

using namespace std;


// Perhaps this works in Linux, but it does not work in Windows.
// There is no /dev/eth0 or /dev/wlan0 in Windows (even in Cygwin).
int main(int argc, char* argv[]) {

	int fd;
	struct ifreq ifr;

	// Open a UDP socket.
	fd = socket(AF_INET, SOCK_DGRAM, 0);

	/* I want to get an IPv4 IP address.*/
	ifr.ifr_addr.sa_family = AF_INET;

	/* I want IP address attached to "eth0". */
	strncpy(ifr.ifr_name, "eth0", IFNAMSIZ - 1);
	ioctl(fd, SIOCGIFADDR, &ifr);

	close(fd);

	// Display the result.
	printf("%s\n", inet_ntoa(((struct sockaddr_in*) &ifr.ifr_addr)->sin_addr));

} // main(...)


