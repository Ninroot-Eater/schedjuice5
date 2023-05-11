import urllib

import decouple
import msal
import requests

AUTHORITY = decouple.config("MS_AUTHORITY")
CLIENT_ID = decouple.config("APP_ID")
KEY = decouple.config("KEY")
THUMBPRINT = decouple.config("THUMBPRINT")
CLIENT_SECRET = decouple.config("CLIENT_SECRET")
STAFFY_ID = "f4f28526-7323-4ef3-8b68-978c3851bc4e"

SCOPES = [
    "User.ReadWrite.All",
    "Directory.ReadWrite.All",
    "Group.ReadWrite.All",
    "Mail.ReadWrite",
    "Mail.Send",
    "MailboxSettings.ReadWrite",
    "TeamMember.ReadWrite.All",
    "TeamMember.ReadWriteNonOwnerRole.All",
]


def get_token():
    app = msal.ConfidentialClientApplication(
        CLIENT_ID,
        authority=AUTHORITY,
        client_credential={"thumbprint": THUMBPRINT, "private_key": open(KEY).read()},
    )
    x = app.acquire_token_silent(SCOPES, account=None)
    if not x:
        res = app.acquire_token_for_client(
            scopes=["https://graph.microsoft.com/.default"]
        )

        return res
    return x


def get_msal_app(cache=None):
    app = msal.ConfidentialClientApplication(
        CLIENT_ID,
        authority=AUTHORITY,
        client_credential={"thumbprint": THUMBPRINT, "private_key": open(KEY).read()},
    )
    return app


class BaseMSRequest:
    """
    The base class for preparing requests to be made to the MS graph API.
    Subclasses tailored for Users and Groups will be inherited from this class.
    Basically, I am building my own wrapper.
    """

    URL = "https://graph.microsoft.com/v1.0/"
    BETA_URL = "https://graph.microsoft.com/beta/"

    headers = {}

    @staticmethod
    def get_token():
        x = get_msal_app()
        res = x.acquire_token_silent(SCOPES, account=None)
        if not res:
            res = x.acquire_token_for_client(
                scopes=["https://graph.microsoft.com/.default"]
            )

        BaseMSRequest.token = res["access_token"]
        BaseMSRequest.headers = {
            "Authorization": "Bearer " + BaseMSRequest.token,
            "Content-Type": "application/json",
        }

    def __init__(self):
        self.get_token()

    def get(self, *args, **kwargs):
        return requests.get(*args, **kwargs, headers=self.headers)

    def post(self, *args, **kwargs):
        return requests.post(*args, **kwargs, headers=self.headers)

    def patch(self, *args, **kwargs):
        return requests.patch(*args, **kwargs, headers=self.headers)

    def delete(self, *args, **kwargs):
        return requests.delete(*args, **kwargs, headers=self.headers)