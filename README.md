# Keymaker

Simple, custom hashing algorithm.

Hashing functions are created to convert data of various sizes to a fixed "address" that can be identified with a key.

Key features include this algorithm must be done quickly, minimal collisions with existing keys, and repeatable.

### Algorithm

1. Function `shift_characters(word, shift)` returns the characters of the word, all shifted by `shift`.
_Shifting a character_ means adding a number to the original character value.
If the resulting character steps out of the `a-z` region, the count is continued from the other end.
The function returns these shifted characters concatenated.
Example: `shift_characters('abby', 5)` returns `'fggd'`.

2. Function `pad_up_to(word, shift, n)` returns a string of `n` characters, starting with the lowercase version of `word`, continued by its shifted variants, as described above.
A variant is the shifted version of the one before.
Example: `pad_up_to('abb', 5, 11)` returns `'abbfggkllpq'`.

3. Function `abc_mirror(word)` returns a string where each character (all lowercase) is "mirrored" to the other side of 'abc'.
A character is the mirror of another when its value distance from 'z' is the same as the value distance of the other character from 'a'.
Example: `abc_mirror('abcd')` returns `'zyxw'`.

4. Function `create_matrix(word1, word2)` returns a list of strings where the nth row is `word1` shifted by the value of the nth character of `word2`.
Example: `create_matrix('mamas', 'papas')` returns `['bpbph', 'mamas', 'bpbph', 'mamas', 'esesk']`.

5. Function `zig_zag_concatenate(list_of_words)` returns a single string containing all the characters of the "matrix".
Example: `zig_zag_concatenate(['aaa', 'bbb', 'ccc', 'ddd'])` returns `abcddcbaabcd`.

```
   0  1  2
0  V  /--\
1  |  |  |
2  |  |  |
3  \--/  V
```

6. Function `rotate_right(word, n)` returns a string of the same length as `word`, only the characters are rotated by `n` positions rightwards.
The character "falling out" on the right side come back from the left side.
Example: `rotate_right('abcdefgh', 1)` returns `'habcdefg'`.

7. Function `get_square_index_chars(word)` returns all characters of `word` laying at square number indices.
Example: `get_square_index_chars('abcdefghijklm')` returns `'abej'`.

8. Function `remove_odd_blocks(word, block_length)` breaks the input into blocks of the given length, removes every second block, and returns the remaining blocks concatenated.
Example: `remove_odd_blocks('abcdefghijklm', 3)` returns `'abcghim'`.

9. Function `reduce_to_fixed(word, n)` cuts the first `n` characters of the input, and performs a left rotation of `n//3` and returns the result read backwards.
Example: `reduce_to_fixed('abcdefghijklm', 6)` returns `'bafedc'`.

### Instruction:

To start:
```
python Keymaker.py
```
