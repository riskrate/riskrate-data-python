import subprocess
import os
import json

from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.introspection import query, variables


def generate_schema(data_url, data_admin_secret, schema_name):
    JSON_PATH = './riskrate_data/{}.json'.format(schema_name)
    SCHEMA_PATH = './riskrate_data/{}.py'.format(schema_name)

    endpoint = HTTPEndpoint(
        data_url, {'x-hasura-admin-secret': data_admin_secret}, None
    )
    data = endpoint(
        query, variables(include_description=False, include_deprecated=False,),
    )
    with open(JSON_PATH, 'w') as file:
        json.dump(
            data, file, sort_keys=True, indent=2, default=str,
        )

    subprocess.run(['sgqlc-codegen', JSON_PATH, SCHEMA_PATH])

    os.remove(JSON_PATH)


if __name__ == '__main__':
    DATA_ADMIN_SECRET = os.getenv('DATA_ADMIN_SECRET')
    DATA_URL = 'https://data.riskrate.io/v1/graphql'
    DATA_URL_DEV = 'https://data2.riskrate.io/v1/graphql'
    generate_schema(
        data_url=DATA_URL,
        data_admin_secret=DATA_ADMIN_SECRET,
        schema_name='schema',
    )
    generate_schema(
        data_url=DATA_URL_DEV,
        data_admin_secret=DATA_ADMIN_SECRET,
        schema_name='schema_dev',
    )
