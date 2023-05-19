# d8118624-2006-4b6c-8f3f-fa7d204e5f9a
from office365.graph_client import GraphClient


def get_token_for_user():
    import adal

    authority_url = "https://login.microsoftonline.com/{0}".format(
        "DONGHWATelecom.onmicrosoft.com"
    )
    auth_ctx = adal.AuthenticationContext(authority_url)
    token = auth_ctx.acquire_token_with_username_password(
        "https://graph.microsoft.com",
        "DONGHWA17@DONGHWATelecom.onmicrosoft.com",
        "Vam1874Vam1874",
        "3886e22f-7576-43f6-9ab5-f2ab68e548fd",
    )
    return token


import adal
from office365.graph_client import GraphClient


def acquire_token_func():
    authority_url = "https://login.microsoftonline.com/DONGHWATelecom.onmicrosoft.com"
    auth_ctx = adal.AuthenticationContext(authority_url)
    token = auth_ctx.acquire_token_with_client_credentials(
        "https://graph.microsoft.com",
        "4169274b-92fc-4d11-8e35-8114f16d287d",
        "Y5F8Q~sobRSv~MwEXkIjZZ0bC4_mY5P6HVMXgc~7",
    )
    return token


print(acquire_token_func())
