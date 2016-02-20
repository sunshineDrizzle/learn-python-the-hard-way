def new(num_buckets=256):
    """
    Initializes a Map with the given number of buckets.
    :param num_buckets:
    :return:
    """
    aMap = []
    for i in range(0, num_buckets):
        aMap.append([])
    return aMap


def hash_key(aMap, key):
    """
    Given a key this will create a number and then convert it to
    an index for the aMap's buckets.
    :param aMap:
    :param key:
    :return:
    """
    return hash(key) % len(aMap)  # 利用内置函数hash()得到key的哈希值，和aMap的长度进行取模运算以控制数值大小来用作buckets在aMap中的索引


def get_bucket(aMap, key):
    """
    Given a key, find the bucket where it would go.
    :param aMap:
    :param key:
    :return:
    """
    bucket_id = hash_key(aMap, key)
    return aMap[bucket_id]


def get_slot(aMap, key, default=None):
    """
    Returns the index, key, and value of a slot found in a bucket.
    Returns -1, key, and default (None if not set) when not found.
    :param aMap:
    :param key:
    :param default:
    :return:
    """
    bucket = get_bucket(aMap, key)

    for i, kv in enumerate(bucket):  # enumerate函数是给bucket中的元素按顺序带上索引值
        k, v = kv
        if key == k:
            return i, k, v

    return -1, key, default


def get(aMap, key, default=None):
    """
    Gets the value in a bucket for the given key, or the default.
    :param aMap:
    :param key:
    :param default:
    :return:
    """
    i, k, v = get_slot(aMap, key, default=default)
    return v


def set(aMap, key, value):
    """
    Sets the key to the value, replacing any existing value.
    :param aMap:
    :param key:
    :param value:
    :return:
    """
    bucket = get_bucket(aMap, key)
    i, k, v = get_slot(aMap, key)

    if i >= 0:
        # the key exists, replace it
        bucket[i] = (key, value)
    else:
        # the key does not, append to create it
        bucket.append((key, value))


def delete(aMap, key):
    """
    Deletes the given key from the Map.
    :param aMap:
    :param key:
    :return:
    """
    bucket = get_bucket(aMap, key)

    for i in range(len(bucket)):
        k, v = bucket[i]
        if key == k:
            del bucket[i]
            break


def list(aMap):
    """
    Prints out what's in the Map.
    :param aMap:
    :return:
    """
    for bucket in aMap:
        if bucket:
            for k, v in bucket:
                print(k, v)
