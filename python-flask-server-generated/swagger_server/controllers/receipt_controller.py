import connexion
import six

from swagger_server.models.inline_response400 import InlineResponse400  # noqa: E501
from swagger_server.models.inline_response401 import InlineResponse401  # noqa: E501
from swagger_server.models.inline_response403 import InlineResponse403  # noqa: E501
from swagger_server.models.inline_response404 import InlineResponse404  # noqa: E501
from swagger_server.models.inline_response405 import InlineResponse405  # noqa: E501
from swagger_server.models.inline_response429 import InlineResponse429  # noqa: E501
from swagger_server.models.inline_response500 import InlineResponse500  # noqa: E501
from swagger_server.models.receipt import Receipt  # noqa: E501
from swagger_server.models.transaction_search_request import TransactionSearchRequest  # noqa: E501
from swagger_server import util
from swagger_server import visual_transactions_demo_modified
from swagger_server.controllers import transaction_controller

def find_receipt(transaction_primary_key, transaction_date, transaction_total, body=None):  # noqa: E501
    """A receipt is searched for in a customer&#x27;s email using the transaction&#x27;s total and date. If a receipt is found, the receipt is given the transaction&#x27;s primary key as its own.

     # noqa: E501

    :param organization_id: Indicates the firm or organization identifier which is issuing the request.
    :type organization_id: str
    :param uuid: Unique request identifier
    :type uuid: str
    :param transaction_primary_key: 
    :type transaction_primary_key: str
    :param transaction_date: 
    :type transaction_date: str
    :param transaction_total: 
    :type transaction_total: str
    :param body: 
    :type body: dict | bytes

    :rtype: Receipt
    """
    if connexion.request.is_json:
        body = TransactionSearchRequest.from_dict(connexion.request.get_json())  # noqa: E501
    cardNumber = '1234'
    visualTransactions = visual_transactions_demo_modified.VisualTransactions(cardNumber)
    visualTransactions.getTransactions()
    receipt = visualTransactions.findReceipt(transaction_primary_key, transaction_date, transaction_total)
    if receipt != {}:
        response = receipt, 200
    else:
        response = receipt, 404
    return response

def get_receipt_by_primary_key(receipt_primary_key, body=None):  # noqa: E501
    """A receipt is returned based on the given primary key

     # noqa: E501

    :param organization_id: Indicates the firm or organization identifier which is issuing the request.
    :type organization_id: str
    :param uuid: Unique request identifier
    :type uuid: str
    :param receipt_primary_key: 
    :type receipt_primary_key: str
    :param body: 
    :type body: dict | bytes

    :rtype: Receipt
    """
    if connexion.request.is_json:
        body = TransactionSearchRequest.from_dict(connexion.request.get_json())  # noqa: E501
    cardNumber = '1234'
    visualTransactions = visual_transactions_demo_modified.VisualTransactions(cardNumber)
    transactionHistory = transaction_controller.get_transactions_history()
    visualTransactions.getTransactions(transactionHistory)
    receipt = visualTransactions.getReceiptByPrimaryKey(receipt_primary_key)
    if receipt != {}:
        response = receipt, 200
    else:
        response = receipt, 404
    return response


def get_receipts(body=None):  # noqa: E501
    """A list of the uploaded pyhsical receipts and eReceipts that were collected are returned

     # noqa: E501

    :param organization_id: Indicates the firm or organization identifier which is issuing the request.
    :type organization_id: str
    :param uuid: Unique request identifier
    :type uuid: str
    :param body: 
    :type body: dict | bytes

    :rtype: List[Receipt]
    """
    if connexion.request.is_json:
        body = TransactionSearchRequest.from_dict(connexion.request.get_json())  # noqa: E501
    #cardNumber = body['pan']['plainText']
    visualTransactions = visual_transactions_demo_modified.VisualTransactions('123')
    transactionHistory = transaction_controller.get_transactions_history()
    visualTransactions.getTransactions(transactionHistory)
    receipts = visualTransactions.getReceipts()
    InlineResponse404("The object(s) does not exist.", "404")
    if receipts != {}:
        response = receipts, 200
    else:
        response = , 404
    return response
