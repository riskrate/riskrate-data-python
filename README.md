# Riskrate Data client for Python

Python wrapper around Riskrate Data GraphQL interface. Internally, makes use of `https://data.riskrate.io/v1/graphql` and `wss://data.riskrate.io/v1/graphql` endpoints.

## Installation

To install the package, use `pip`:

```shell
pip install riskrate-data
```

## Getting started

First, you need to initialize the client:

```python
import riskrate_data

# Set your admin secret key
DATA_ADMIN_SECRET = 'YOUR_ADMIN_SECRET'

# Construct a client
data_client = riskrate_data.DataClient(DATA_ADMIN_SECRET)
```

Client uses singleton pattern, so if you don't want to pass `data_client` to all functions that use it, you can call an empty constructor and get the reference to the client:

```python
data_client = riskrate_data.DataClient()
```

However, to use this, proper instance (with `data_admin_secret`) should be created first.

## Usage

Next, you need to create a query object. You need to choose if you want to use `query`, `mutation` or `subscription`:

```python
my_query = data_client.query()
my_mutation = data_client.mutation()
my_subscription = data_client.subscription()
```

For simplicity, we will construct a query. Here's how we can construct a query object to get all companies from the database:

```python
my_query = data_client.query()

my_query_company = my_query.company()

# Explicitly ask for fields
my_query_company.id()
my_query_company.vat()
my_query_company.name()

# Make query and immediately execute
raw_result = data_client.make_query(my_query).execute()
```

`execute()` returns a dictionary. Don't forget that this is a GraphQL response, so you have to select the data yourself:

```python
companies = raw_result['data']['company']

# companies is a list of dicts
for company in companies:
  print(company)
```

That is useful in combination with `pandas`. Before constructing DataFrame, we should flatten nested dicts (don't forget to `import pandas as pd`):

```python
companies_df = pd.json_normalize(companies, sep='_')
print(companies_df.head())
```

You can also parse the result into native Python objects:

```python
result = my_query + raw_result

# result.company is a list of company objects
for company in result.company:
    print(company)
```

## "Simple" functions

This package also provides an easy way to create unnamed queries with no variables called **simple functions**. You can import them from `riskrate_data`:

```python
from riskrate_data import simple_query, simple_query_dict, simple_mutation, insert_chunked
```

`simple_query` and `simple_query_dict` are supposed to be used like decorators: each time you are given new `query` object, that you can use to make your query. In the end, you have to return the modified query object:

```python
@simple_query
def get_all_companies(query):
    """
    Returns all companies from the database.
    """

    query.company.__fields__(
        id=True, vat=True, name=True
    )
    return query

companies = get_all_companies().company
```

The difference between `simple_query` and `simple_query_dict` is that the former returns native Python objects, but the latter returns dictionary. `simple_query_dict` works much faster and integrates nicely with `pandas`, so if you're analysing lots of data, use this:

```python
@simple_query_dict
def get_all_companies_dict(query):
    """
    Returns all companies from the database.
    """

    query.company.__fields__(
        id=True, vat=True, name=True
    )
    return query

companies = get_all_companies_dict()['company']
# Flatten if there are nested relations
companies_df = pd.json_normalize(companies, sep='_')
```

For mutations you have to use `insert_chunked`, it will split your data into pieces before mutating so you don't timeout:

```python
@simple_mutation
def insert_companies(mutation, data):
    """
    Inserts companies into DB
    """

    mutation.insert_company(objects=data).affected_rows()
    return mutation

res = insert_chunked(companies, insert_companies)
print('Affected rows: {}'.format(res.insert_company.affected_rows))
```

Be careful, `insert_chunked` assumes that your function accepts `data` as the second parameter (right after `mutation`).

## Advanced use cases

If you feel like you need more control over your queries, you can use `sgqlc` to get this functionality. Alternatively, you can run the GraphQL queries directly.

### Custom query example

Let's see how you can customize the queries:

```python
from sgqlc.types import Variable, non_null

# Optionally, you can set the name and variables
my_query = data_client.query(name='my_query', limit=non_null(int))

# Query specific fields
my_query.invoice(limit=Variable('limit')).__fields__(id=True, buyer_id=True, seller_id=True)

# Or use a shortcut
my_query.company(limit=Variable('limit')).__fields__('id', 'name', 'vat')

# You can print out your query
print(my_query)
```

This will result in the following query:

```graphql
query my_query($limit: Int!) {
  invoice(limit: $limit) {
    id
    buyer_id
    seller_id
  }
  company(limit: $limit) {
    id
    name
    vat
  }
}
```

Now, execute the query and pass your variables as a dictionary:

```python
# Set limit, so we don't query the whole database.
# Specific order of entries is not guaranteed!
LIMIT = 10

raw_result = data_client.make_query(my_query).execute({'limit': LIMIT})
```

You can also find more use cases from [sgqlc page](https://github.com/profusion/sgqlc). Not everything is documented there, so you might have to look through their source code.

### Using GraphQL queries directly

This library is made to abstract away from using direct queries. However, some use cases are not supported by `sgqlc`, so if you ever need to execute GraphQL queries directly, you can do it:

```python
LIMIT = 10

raw_result = data_client.make_query(
    """
    query test($limit: Int!) {
        invoice(limit: $limit) {
            id
            buyer_id
            seller_id
        }
        company(limit: $limit) {
            id
            name
            vat
        }
    }
"""
).execute({'limit': LIMIT})
```

## Limitations

Currently, GraphQL subscriptions via WebSockets are **not supported**. However, you can still use other GraphQL packages to get this functionality, namely [gql](https://github.com/graphql-python/gql).

## Developing

If GraphQL schema of Riskrate Data changes, you have to regenerate all the Python classes. To regenerate classes using `sgqlc`, use:

```shell
DATA_ADMIN_SECRET=YOUR_SECRET_KEY python3 riskrate_data/generate_schema.py
```
