import hashlib

HASHED_CRON_CHAR = "H"

HASH_CONFIGS = {
    0: {"value": 60, "increment": 0},
    1: {"value": 24, "increment": 0},
    2: {"value": 32, "increment": 0},
    3: {"value": 12, "increment": 1},
    4: {"value": 7, "increment": 0},
    5: {"value": 2030, "increment": 0},
}


def convert(cron, identifier):
    """ Converts cron """
    if cron and len(cron.split(" ")) in [5, 6]:
        if HASHED_CRON_CHAR in cron:
            return convert_hashed_cron(cron, identifier)

        else:
            return cron

    return None


def convert_hashed_cron(cron, dag_id):
    """ Converts hashed cron """
    converted_cron = str()
    cron_expression_array = cron.split(" ")

    for index, item in enumerate(cron_expression_array):
        if HASHED_CRON_CHAR in item and index in HASH_CONFIGS:
            converted_cron += " " + generate_dynamic_cron_value(dag_id, index, item)

        else:
            converted_cron += " " + item

    return converted_cron.strip()


def generate_dynamic_cron_value(dag_id, index, item):
    """ Generates a dynamic cron value, based on its index """
    separator_char = "/"
    dag_id_hash = generate_text_hash(dag_id)
    hash_mod = HASH_CONFIGS[index]["value"]
    hash_increment = HASH_CONFIGS[index]["increment"]

    if separator_char in item:
        hash_mod = int(item.split(separator_char, 1)[1])
        hash_value = str((dag_id_hash % hash_mod) + hash_increment)
        return hash_value + separator_char + str(hash_mod)

    else:
        return str((dag_id_hash % hash_mod) + hash_increment)


def generate_text_hash(text):
    """ Generates hash value of a text """
    encoded_text = text.encode("utf-8")
    return int(hashlib.sha1(encoded_text).hexdigest(), 16)
