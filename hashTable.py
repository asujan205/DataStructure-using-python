def get_hash_key(key):
    h=0 
    for char in key:
        h+=ord(char)
    return h %10
    