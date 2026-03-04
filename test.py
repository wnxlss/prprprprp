from yoomoney import Authorize

Authorize(
    client_id="F9FF6E03A35616D5B59653C9836907AB81E44F5D4C0619B6EAFEBD7D1CE117DB",
    redirect_uri="https://yoomoney.ru/",
    client_secret="0A260AE54D5BABE534C74FC958721633C7DE6C864C8BC72F35D23C08FF466BD482401AF9215F20BBE7C74933F500498EB0859992C9460046D51D35CC7B7C1CD5", # Может не требоваться для некоторых типов приложений
    scope=[
        "account-info",
        "operation-history",
        "operation-details",
        "incoming-transfers",
        "payment-p2p",
        "payment-shop",
    ]
)