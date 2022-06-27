import os
graph_auth = {
    "tenant": os.environ["SENTINEL_TENANT"],
    "client_id": os.environ["SENTINEL_CLIENT_ID"],
    "client_secret": os.environ["SENTINEL_SECRET"],
}
targetProduct = os.environ.get("TARGET_PRODUCT", "<targetProduct>")
misp_event_filters = {
    #"org": os.environ.get("MISP_EVENT_FILTER_ORG", ""),
    #"category": os.environ.get("MISP_EVENT_FILTER_CATEGORY", ""), 
    #"last": "30m",
    #"limit": "10",
}
action = os.environ.get("ACTION", "<action>")
passiveOnly = False
days_to_expire = int(os.environ.get("DAYS_TO_EXPIRE", "5"))
misp_key = os.environ["MISP_KEY"]
misp_domain = os.environ["MISP_DOMAIN"]
misp_verifycert = os.environ.get("MISP_VERIFYCERT", "False").lower() == "true"


targetProduct = os.environ.get("TARGET_PRODUCT", "<targetProduct>")
action = os.environ.get("ACTION", "<action>")
