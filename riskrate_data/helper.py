from .connection import DataClient


def simple_query(func):
    """
    Decorator to execute unnamed queries without variables.
    Returns native python objects.

    If you want it to return `dict`, use `simple_query_dict`.
    """

    def wrapper(*args, **kwargs):
        data_client = DataClient()
        query = data_client.query()
        result = func(query, *args, **kwargs)
        return query + data_client.make_query(result).execute()

    return wrapper


def simple_query_dict(func):
    """
    Same as `simple_query`, but returns `dict`
    """

    def wrapper(*args, **kwargs):
        data_client = DataClient()
        query = data_client.query()
        result = func(query, *args, **kwargs)
        return data_client.make_query(result).execute()['data']

    return wrapper


def simple_insert(func):
    """
    Decorator to execute unnamed mutations without variables.
    Returns native python objects.
    """

    def wrapper(*args, **kwargs):
        data_client = DataClient()
        query = data_client.mutation()
        result = func(query, *args, **kwargs)
        return query + data_client.make_query(result).execute()

    return wrapper


def insert_chunked(data, insert_func, split_size=5000):
    """
    Inserts data into DB, splitting by chunks
    """
    print("Inserting {} entries to the database...".format(len(data)))

    res = None
    for i in range(0, len(data), split_size):
        chunk = data[i : i + split_size]
        r = insert_func(chunk)
        res = r if res is None else res + r

    return res
