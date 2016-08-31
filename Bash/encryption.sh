#!/usr/bin/env bash

# WARNING: You can't directly encrypt a large file using rsautl.  Public/private key pairs tend to
# be used to protect symmetric keys (like AES) that are then used to enc/dec large files.

#==============================================================================
# Public/Private Keys
# Asymmetric Keys
# PSKs
#==============================================================================

echo 'Hello, encryption!' > plain.txt

# Export public key in a form usable by openssh.
# PEM => privacy enhanced e-mail; a container formt for keys/certs from RFC 1421..1424.
if [ ! -f ~/.ssh/id_rsa.pub.pem ]; then
	openssl rsa -in ~/.ssh/id_rsa -pubout > ~/.ssh/id_rsa.pub.pem
fi

# Encrypt with public key using RSA utility.
cat plain.txt | openssl rsautl -encrypt -pubin -inkey ~/.ssh/id_rsa.pub.pem > plain.txt.enc

# Decrypt using private key.
cat plain.txt.enc | openssl rsautl -decrypt -inkey ~/.ssh/id_rsa > plain2.txt

od -c plain.txt.enc
echo
diff plain.txt plain2.txt && cat plain2.txt  


#==============================================================================
# Session Keys
# Data Keys
# Symmetric Keys
#==============================================================================


# Here's how you encrypt large data files.
# Assume that your public/private keys are preshared.
# Assume you use those PSKs to enc/dec your symmetric data enc key.

# Create a random 256-bit symmetric data key for use with AES.
openssl rand 32 -out datakey.key

# Create a large blob of random data.
dd if=/dev/random of=data.bin bs=1M count=10

# Encrypt.
openssl enc -in data.bin -out data.bin.enc -e -aes256 -k datakey.key

# Decrypt.
openssl enc -in data.bin.enc -out data.bin.enc.dec -d -aes256 -k datakey.key

diff data.bin data.bin.enc
diff data.bin data.bin.enc.dec && echo "Enc/dec succeeded!"


# Clean up.
rm -f plain.txt
rm -f plain2.txt
rm -f plain.txt.enc

rm -f datakey.key
rm -f data.bin
rm -f data.bin.enc
rm -f data.bin.enc.dec

exit 0


