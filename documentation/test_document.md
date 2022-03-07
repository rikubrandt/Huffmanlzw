# Testing document
Used unittest framework for unit testing the program.

## Tests
Tests can be found from `test_huffman.py` and `test_lzw.py` files.
Used basic inputs to verify that the functions work as they should.

Tests can be run with command
> poetry run coverage run -m pytest
And test coverage report can be generated
> poetry run coverage html

## Test coverage
![Coverage report](/documentation/pictures/coverage.png)



## Performance testing
Generated lorem ipsum files from [Loremipsum.com](https://www.lipsum.com/) and compressed and decompressed the files.

### Huffman 
| Original Size (in bytes) | Compressed size | (%) | Compression time (ms) | Decompression time (ms) |
|---|---|---|---|---|
| 64 | 58 | 7.79 | 0.389 | 0.233 |
| 256 | 173 | 31.67 | 0.637 | 0.469 |
| 1 024 | 570 | 44.06 | 0.789 | 0.769 |
| 4 096 | 2 174 | 46.69 | 1.799 | 2.434 |
| 8 192 | 4 342 | 47.76 | 3.180 | 5.010 |
| 262 144 | 137 021 | 48.01 | 79.421 | 136.317 |
| 524 288 | 273 981 | 47.74 | 158.517 | 272.876 |
| 1 048 576 | 547 900 | 47.65 | 317.121 | 541.023 |


### Lempel-Ziv-Welch
| Original Size (in bytes) | Compressed size | (%) | Compression time (ms) | Decompression time (ms) |
|---|---|---|---|---|
| 64 | 67 | -3.17 | 0.279 | 0.247 |
| 256 | 209 | 19.41 | 0.410 | 0.438 |
| 1 024 | 688 | 32.7 | 1.17 | 0.968 |
| 4 096 | 2 230| 45.42 | 3.202 | 2.49 |
| 8 192 | 4 222 | 48.41 | 5.699 | 4.231 |
| 262 144 | 79 534 | 69.56 | 129.757 | 65.367 |
| 524 288 | 155 702 | 70.41 | 258.63 | 122.925 |
| 1 048 576 | 300 889 | 71.32 | 541.371 | 235.868 |

![Compression percentage](/documentation/pictures/compression.png)
