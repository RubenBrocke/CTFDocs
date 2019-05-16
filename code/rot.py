# This python script will brute force all possible ROTn plaintexts

ciphertext = "Gurer vf na nezl znepuvat va gur rnfg"
plaintext = ""

# for every possible n (0 and 26 don't change anything)
for i in range(1, 26):
    # for every character in the ciphertext
    for c in ciphertext:
        # if the character is a lower case character
        if (c.islower()):
            plaintext += chr((((ord(c) - 97) + i) % 26) + 97)
        # if the character is an upper case character
        elif(c.isupper()):
            plaintext += chr((((ord(c) - 65) + i) % 26) + 65)
        # if the character is neither it's an invalid character
        else:
            plaintext += c
    print(plaintext)
    plaintext = ""