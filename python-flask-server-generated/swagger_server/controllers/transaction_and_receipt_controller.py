import connexion
import six

from swagger_server.models.inline_response400 import InlineResponse400  # noqa: E501
from swagger_server.models.inline_response401 import InlineResponse401  # noqa: E501
from swagger_server.models.inline_response404 import InlineResponse404  # noqa: E501
from swagger_server.models.inline_response405 import InlineResponse405  # noqa: E501
from swagger_server.models.inline_response429 import InlineResponse429  # noqa: E501
from swagger_server.models.inline_response500 import InlineResponse500  # noqa: E501
from swagger_server.models.transaction_and_receipt import TransactionAndReceipt  # noqa: E501
from swagger_server.models.transaction_and_receipt_search_response import TransactionAndReceiptSearchResponse  # noqa: E501
from swagger_server.models.transaction_search_request import TransactionSearchRequest  # noqa: E501
from swagger_server import util
from swagger_server import visual_transactions_demo_modified
from swagger_server.controllers import transaction_controller

def get_transaction_and_receipt_by_primary_key(primary_key, body=None):  # noqa: E501
    """A transaction and its receipt is returned based on the given primary key

     # noqa: E501

    :param organization_id: Indicates the firm or organization identifier which is issuing the request.
    :type organization_id: str
    :param uuid: Unique request identifier
    :type uuid: str
    :param primary_key: 
    :type primary_key: str
    :param body: 
    :type body: dict | bytes

    :rtype: TransactionAndReceipt
    """
    if connexion.request.is_json:
        body = TransactionSearchRequest.from_dict(connexion.request.get_json())  # noqa: E501
    cardNumber = '1234'
    visualTransactions = visual_transactions_demo_modified.VisualTransactions(cardNumber)
    transactionHistory = transaction_controller.get_transactions_history()
    visualTransactions.getTransactions(transactionHistory)
    transactionAndReceipt = visualTransactions.getTransactionAndReceiptByPrimaryKey(primary_key)
    return transactionAndReceipt


def get_transactions_and_receipts(body=None):  # noqa: E501
    """A list of transactions and receipts are returned

     # noqa: E501

    :param organization_id: Indicates the firm or organization identifier which is issuing the request.
    :type organization_id: str
    :param uuid: Unique request identifier
    :type uuid: str
    :param body: 
    :type body: dict | bytes

    :rtype: TransactionAndReceiptSearchResponse
    """
    if connexion.request.is_json:
        body = TransactionSearchRequest.from_dict(connexion.request.get_json())  # noqa: E501
    cardNumber = '1234'
    visualTransactions = visual_transactions_demo_modified.VisualTransactions(cardNumber)
    transactionHistory = transaction_controller.get_transactions_history()
    visualTransactions.getTransactions(transactionHistory)
    transactionsAndReceipts = visualTransactions.getTransactionsAndReceiptsDict()
    return transactionsAndReceipts
