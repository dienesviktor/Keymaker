def shift_characters(word, shift):
    result = ""
    for char in word:
        character = chr((ord(char) + (shift % 26)))
        if ord(character) <= 122:
            result += character
        elif ord(character) > 122:
            result += chr(ord(character) - 26)
    return result


def pad_up_to(word, shift, n):
    result = word
    for char in range(n):
        result += shift_characters(word, shift)
        word = shift_characters(word, shift)
    return result[:n]


def abc_mirror(word):
    result = ""
    for char in word:
        if ord(char) - ord("a") > ord(char) - ord("z"):
            mirrored = chr(ord("z") - (ord(char) - ord("a")))
            result += mirrored
        else:
            mirrored = chr(ord("a") + (ord(char) - ord("z")))
            result += mirrored
    return result


def create_matrix(word1, word2):
    result = []
    for i in range(len(word2)):
        result.append(shift_characters(word1, ord(word2[i]) - ord("a")))
    return result


def zig_zag_concatenate(matrix):
    result = ""
    for char in range(len(matrix[0])):
        for item in range(len(matrix)):
            if char % 2 == 0:
                result += matrix[item][char]
            else:
                result += matrix[-1-item][char]
    return result


def rotate_right(word, n):
    result = word
    if n >= 0:
        for i in range(1, n+1):
            variation = result[-1] + result[:-1]
            result = variation
    else:
        for i in range(1, abs(n)+1):
            variation = result[1:] + result[0]
            result = variation
    return result


def get_square_index_chars(word):
    result = ""
    try:
        for index in range(len(word)):
            result += word[index**2]
        return result
    except IndexError:
        return result


def remove_odd_blocks(word, block_length):
    result = ""
    for i in range(len(word)+block_length):
        if block_length % 2 == 1:
            if i % 2 == 1:
                result += word[i*block_length-block_length:i*block_length]
        elif block_length % 2 == 0:
            if i % 2 == 0:
                result += word[i*block_length-block_length:i*block_length]
    return result


def reduce_to_fixed(word, n):
    new_word = word[:n]
    shift = n // 3
    result = rotate_right(new_word, shift*-1)
    return result[::-1]


def hash_it(word):
    padded = pad_up_to(word, 15, 19)
    elongated = zig_zag_concatenate(create_matrix(padded, abc_mirror(padded)))
    rotated = rotate_right(elongated, 3000003)
    cherry_picked = get_square_index_chars(rotated)
    halved = remove_odd_blocks(cherry_picked, 3)
    key = reduce_to_fixed(halved, 6)
    return key


if __name__ == '__main__':
    name = input("Enter your name! ").lower()
    print(f'Your key: {hash_it(name)}')
