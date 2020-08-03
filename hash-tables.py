# b = "beej".encode()
# for letter in b:
#     print(letter)

HASH_DATA_SIZE = 8

hash_data = [None] * HASH_DATA_SIZE


def hash_function(str):
    # Naive hashing function -- do not use in production
    bytes_list = str.encode()

    total = 0

    for b in bytes_list:  # O(n) over the length of the key
        total += b

    return total


def get_index(str):
    hash_value = hash_function(str)
    return hash_value % HASH_DATA_SIZE


def put(k, v):
    # 'for a given key, store a value in the hash table'
    index = get_index(k)
    hash_data[index] = v


def get(k):
    index = get_index(k)
    return hash_data[index]


print(hash_data)
put("Beej!", "hello world!")
put("Goats", 3490)
# print(hash_data)
# put("Beej!", "hello, again")
print(hash_data)

print(get("Beej!"))
print(get("Goats"))

