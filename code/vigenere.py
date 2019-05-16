# This python script will decrypt vigenere using letter requency analysis

ciphertext = "Ahmcx pw kv nxty ulkjlsvt ou tpp xhwd"
plaintext = ""

# First we need to get the aproximate key length
def getKeyLength(input, ammount, begin, end):
    # get the letter frequencies
    input = input.lower()
    input = input.replace(" ", "")
    frequencies = []
    for c in range(0, 26):
        frequencies.append(input.count(chr(c + 97)))
    
    results = {}
    for keylength in range(begin, end):
        strings = [input[i:i+keylength] for i in range(0, len(input), keylength)]
        stringfreq = []
        for string in strings:
            freqsum = 0
            for c in string:
                freqsum += frequencies[ord(c) - 97] * (frequencies[ord(c) - 97] -1)
            stringfreq.append(freqsum / (len(input * (len(input) - 1))))
        results[keylength] = 0.0385  / ((sum(stringfreq) / len(stringfreq)) - 0.0385)

    print(results)
    return []
keylengths = getKeyLength(ciphertext, 3, 3, len(ciphertext))