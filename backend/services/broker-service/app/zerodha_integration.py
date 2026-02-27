"""Sample Zerodha Kite Connect integration."""
from kiteconnect import KiteConnect


def get_login_url(api_key: str) -> str:
    kite = KiteConnect(api_key=api_key)
    return kite.login_url()


def exchange_request_token(api_key: str, api_secret: str, request_token: str) -> dict:
    kite = KiteConnect(api_key=api_key)
    session = kite.generate_session(request_token, api_secret=api_secret)
    kite.set_access_token(session["access_token"])
    profile = kite.profile()
    return {"session": session, "profile": profile}
