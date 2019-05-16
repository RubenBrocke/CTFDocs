---
id: rot
title: ROT substitution cipher
sidebar_label: ROT cipher
---

## Explaination

One of the easiest substitution ciphers is the ROT cipher. This cipher is also called the Caesar cipher (based on Julius Caesar).

I works by shifting the alphabet n places. for example:

`ROT2: CDEFGHIJKLMNOPQRSTUVWXYZAB`

`ROT13: NOPQRSTUVWXYZABCDEFGHIJKLM`

## Example

Plaintext: `There is an army marching in the east`

After putting this through ROT13 we get:

Ciphertext: `Gurer vf na nezl znepuvat va gur rnfg`

## Detecting

This cipher can at first be tricky to detect.
This is because the text is not scrambled in any way and could be using any other substitution cipher like: (link).

The best way to detect ROT ciphers is by looking at repeated characters (at least in english). For example a word like `roof` will become `ebbs`.
This still contains the double letter it's just a different letter.

A second thing to look at is the word length. If it looks like it could be a sentence (mix of longer and shorter words) then it might be worth checking for ROT ciphers.

## Solving

An ROT cipher is trivially solveable. This is because it's easy to try all 25 different values for n. 

To decrypt any ciphertext which is suspected to be encrypted with ROTn
we can do the following calculation:

`plaintext[i] = ciphertext[i] + n % 26`

Some more calculation needs to be done to work with the ASCII standard but the idea stays the same.

## Code (brute force)

```python
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
```
