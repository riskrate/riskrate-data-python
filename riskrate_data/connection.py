from sgqlc.operation import Operation
from .graphql_schema import graphql_schema as schema
from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.endpoint.websocket import WebSocketEndpoint

DATA_HTTPS_URL = 'https://data.riskrate.io/v1/graphql'
DATA_WSS_URL = 'wss://data.riskrate.io/v1/graphql'


class DataClient:
    """
    Main class that handles all queries and connections.

    Uses singleton pattern.
    """

    class __DataClient:
        def __init__(
            self,
            data_admin_secret,
            data_https_url=DATA_HTTPS_URL,
            data_wss_url=DATA_WSS_URL,
        ):

            # Set up clients
            self.https_client = HTTPEndpoint(
                data_https_url, {'x-hasura-admin-secret': data_admin_secret},
            )
            self.wss_client = WebSocketEndpoint(
                data_wss_url, {'x-hasura-admin-secret': data_admin_secret}
            )

        def query(self, *args, **kwargs):
            """
            Returns a query object.
            """

            return Operation(schema.query_type, *args, **kwargs)

        def mutation(self, *args, **kwargs):
            """
            Returns mutation object.
            """

            return Operation(schema.mutation_type, *args, **kwargs)

        def subscription(self, *args, **kwargs):
            """
            Returns subscription object.
            """

            return Operation(schema.subscription_type, *args, **kwargs)

        def make_query(self, query):
            """
            Sets up a query (string or object).
            """

            self.__query = query
            return self

        def execute(self, variables=None, operation_name=None):
            """
            Sends https request to the server.
            """

            return self.dispatch_request(
                self.https_client, variables, operation_name
            )

        def subscribe(self, variables=None, operation_name=None):
            """
            Sends wss request to the server.

            Currently doesn't work because of `sgqlc` error!
            """

            return self.dispatch_request(
                self.wss_client, variables, operation_name
            )

        def dispatch_request(self, client, *args, **kwargs):
            """
            Sends request to the server through a given client

            Don't use this method explicitly, use execute() or subscribe()!
            """

            response = client(self.__query, *args, **kwargs)
            return self.process_response(response)

        def process_response(self, response):
            """
            Returns response data or raises an error.
            """

            if 'errors' in response:
                # Raise only first error message
                raise Exception(response['errors'][0]['message'])

            return response

    __instance = None

    def __init__(self, *args, **kwargs):
        if not DataClient.__instance:
            DataClient.__instance = DataClient.__DataClient(*args, **kwargs)

    def __getattr__(self, name):
        return getattr(self.__instance, name)
