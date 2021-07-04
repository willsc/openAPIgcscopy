import connexion
import six

import os, sys
import stat


from swagger_server import util


def get_delete_path(query=None):  # noqa: E501
    """Delete

     # noqa: E501

    :param query: 
    :type query: str

    :rtype: None
    """
    print(query)
    print("deltree", query)
    for d in os.listdir(query):
        try:
            deltree(query + '/' + d)
        except OSError:
            os.remove(query + '/' + d)

    os.rmdir(query)
    return True 
