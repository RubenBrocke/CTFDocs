---
id: crypto
title: Cryptography
sidebar_label: Cryptography
---

## Cryptography

### [ROT cipher](./crypto/rot.md)

A simple substitution cipher based on character shifting.
Every character of the plaintext gets shifted by the same ammount resulting in the ciphertext.

### [Vigenere cipher](./crypto/vigenere.md)

A substitution cipher using a key to indicate character shifting.
A character in the plaintext get shifted relative character in the key resulting in the ciphertext.

### [AES](./crypto/aes.md)

A symmetric encryption cipher. 
Uses byte substitution and shuffling to mask the plaintext and key.
Is widely used for symmetric encryption and can be used with multiple block modes.

### [RSA](./crypto/rsa.md)

An asymmetric encryption cipher.
Uses a public and private key for encryption and decyption respectively.
Starts with two primes 
$$p, q$$
public key = n, e
$$n = p * q$$
$$e = [3, 5, 17, 257, 65537]$$

private key = d, n
$$d = modinv((p-1)*(q-1), e)$$

Encryption / Decryption:
$$ciphertext = plaintext^e \bmod n$$
$$plaintext = 


### [MD5](./crypto/md5.md)

Message digest 5 hashing algorithm creating 128-bit hashes.

### [SHA1](./crypto/sha1.md)

Secure Hashing Algorithm V1 is a hashing algorithm creating 160-bit hashes.

### [SHA2](./crypto/sha2.md)

Secure Hashing Algorithm V2 is the successor to the SHA1 algorithm and has the ability to create 224, 256, 384 or 512 bit hashes.

### [DH](./crypto/dh.md)

Diffie-Hellman key exchange