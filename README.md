# Riskrate Data client for Python

Python wrapper around Riskrate Data GraphQL interface. Internally, makes use of `https://data.riskrate.io/v1/graphql` and `wss://data.riskrate.io/v1/graphql` endpoints.

## Installation

To install the package, use `pip`:

```shell
pip install riskrate-data
```

## Usage

Code example of how to make use of the package:

```python
import riskrate_data
from sgqlc.types import Variable, non_null

# Set your admin secret key
DATA_ADMIN_SECRET = 'YOUR_ADMIN_SECRET'

# Set limit, so we don't query the whole database.
# Specific order of entries is not guaranteed!
LIMIT = 3

# Construct a client
data_client = riskrate_data.DataClient(DATA_ADMIN_SECRET)

# Get the query object (Optionally, you can set the name and variables)
my_query = data_client.query(name='my_query', limit=non_null(int))
# For mutations, use data_client.mutation()

# Query specific fields
my_query.invoice(limit=Variable('limit')).id()
my_query.invoice.buyer_id()
my_query.invoice.seller_id()

# Or use a shortcut
my_query.company(limit=Variable('limit')).__fields__('id', 'name', 'vat')

print(my_query)
```

You can check your constructed query:

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

You can find more use cases from [sgqlc page](https://github.com/profusion/sgqlc).

Make query and immediately execute:

```python
raw_result = data_client.make_query(my_query).execute({'limit': LIMIT})

print(raw_result)
```

Alternatively, you can use GraphQL queries directly:

```python
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

print(raw_result)
```

You can also parse the result into native Python objects:

```python
result = my_query + raw_result

# Iterate over invoices
for invoice in result.invoice:
    print(invoice)

# Iterate over companies
for company in result.company:
    print(company)
```

GraphQL subscriptions via WebSockets are currently **not supported**. However, you can still use other GraphQL packages to get this functionality, namely [gql](https://github.com/graphql-python/gql).

## Developing

If GraphQL schema of Riskrate Data changes, you have to regenerate all the Python classes. To regenerate classes using `sgqlc`, use:

```shell
DATA_ADMIN_SECRET=YOUR_SECRET_KEY python riskrate_data/generate_schema.py
```
