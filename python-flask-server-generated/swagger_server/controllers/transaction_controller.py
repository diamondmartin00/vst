import connexion
import six
import json

from swagger_server.models.inline_response400 import InlineResponse400  # noqa: E501
from swagger_server.models.inline_response401 import InlineResponse401  # noqa: E501
from swagger_server.models.inline_response404 import InlineResponse404  # noqa: E501
from swagger_server.models.inline_response405 import InlineResponse405  # noqa: E501
from swagger_server.models.inline_response429 import InlineResponse429  # noqa: E501
from swagger_server.models.inline_response500 import InlineResponse500  # noqa: E501
from swagger_server.models.transaction_search_request import TransactionSearchRequest  # noqa: E501
from swagger_server.models.transaction_search_response import TransactionSearchResponse  # noqa: E501
from swagger_server import util

def get_transactions_history(body=None):  # noqa: E501
    """transaction history is returned

     # noqa: E501

    :param organization_id: Indicates the firm or organization identifier which is issuing the request.
    :type organization_id: str
    :param uuid: Unique request identifier
    :type uuid: str
    :param body: 
    :type body: dict | bytes

    :rtype: TransactionSearchResponse
    """
    if connexion.request.is_json:
        body = TransactionSearchRequest.from_dict(connexion.request.get_json())  # noqa: E501
    jsonFile = open(r"C:\Users\e5657937\OneDrive - FIS\Documents\visual_transactions\python-flask-server-generated\swagger_server\transaction_history.json") #open JSON file containing transaction history
    bankTransactions = json.load(jsonFile) #convert banking transaction to JSON
    return bankTransactions
