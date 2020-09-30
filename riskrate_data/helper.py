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


def simple_mutation(func):
    """
    Decorator to execute unnamed mutations without variables.
    Returns native python objects.
    """

    def wrapper(*args, **kwargs):
        data_client = DataClient()
        mutation = data_client.mutation()
        result = func(mutation, *args, **kwargs)
        return mutation + data_client.make_query(result).execute()

    return wrapper


def insert_chunked(data, insert_func, *args, split_size=5000, **kwargs):
    """
    Inserts data into DB, splitting by chunks
    """

    res = None

    # Special case for empty data
    if not data:
        res = insert_func(data, *args, *kwargs)
    else:
        for i in range(0, len(data), split_size):
            chunk = data[i : i + split_size]
            r = insert_func(chunk, *args, *kwargs)
            res = r if res is None else res + r

    return res
