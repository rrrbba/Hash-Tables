import random

def how_many_before_colliosion(buckets, loops =1):
    """
    Roll random hashes indexes into buckets and print
    how many rolls before a collision

    Run loops times
    """

    for i in range(loops):
        tries = 0
        tried = set()

        tried_list = []

        while True:
            random_key = str(random.random())
            #find index from random key string
            hash_index = hash(random_key) % buckets

            if hash_index not in tried_list:
                tried_list.append(hash_index)

                tries += 1

            else:
                #collision is found
                break

        print(f"{buckets} buckets, {tries} hashes before colliosion. ({tries/buckets * 100:.1f}%)")

print(how_many_before_colliosion(100,10))