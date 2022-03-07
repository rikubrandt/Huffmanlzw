# Implementation document

## Huffman coding
### Encoding
- Create dictionary of chars in the text and their number of occurrences
- Create the huffman tree
- Create the bit representation of the huffman tree. 
- Encode the text using the bit representation, encode the huffman tree and the length of the huffman tree to the bit representation.
- Turn the bits into binary and save the file.

### Decoding
- Turn the binary file to bits and take info about the length of the huffman tree and remove extra bits.
- Create the huffman tree from the tree bits. 
- Decode the text bits into text using the huffman tree.
- Save the newly created text file.

### Time Complexity
- O(n log n)


## Lempel-Ziv-Welch
### Encoding
- Create dictionary of characters and their unicode values.
- Run through the text char by char and if the current + next string is not in the dictionary add it there with value 256 and raise the dict_size value by one. 
- If the current + next string is in the dictionary then make it as the current string and continue the loop.
- Returns a list that is shorter than the original and we get compression.
- Create bit representation of the list and save it as binary.
### Decoding
- Remove bit length info and the extra bits. 
- Create list of the bits
- Create dictionary of the list items that have value below 256.
- Decode the text using the dictionary.

### Time Complexity
o(n)