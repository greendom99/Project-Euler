file = open("project_files\\problem_59.txt", "r")
for contents in file:
    input_encoded_message = contents.split(",")
    input_encoded_message = list(map(int, input_encoded_message))

# key = 'exp'

def decode(encoded_message_list, key):
    decoded_message = ''
    for index, element in enumerate(encoded_message_list):
        decoded_message += chr(element ^ ord(key[index % 3]))
        # print(element, key[index % 3],chr(element ^ ord(key[index % 3])) )
    return decoded_message


def key_finder(input_list):
    # Use letter frequency to determine the key.
    # Uses the fact that space character i.e ' ' is likely to be most frequent
    key = ''
    for n in [0, 1, 2]:
        freq_dict = {}
        for index, element in enumerate(input_list):
            if index % 3 == n:
                if element in freq_dict:
                    freq_dict[element] += 1
                else:
                    freq_dict[element] = 1
        max_freq_char = max(freq_dict, key=freq_dict.get)
        for i in range(97, 123):
            if chr(max_freq_char^i) == ' ':

                key += chr(i)
    return key


found_key = key_finder(input_encoded_message)
output_decoded_message = decode(input_encoded_message, found_key)
print(output_decoded_message)
