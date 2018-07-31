# In routing.py
from channels.routing import route
channel_routing = [
    route("http.request", "awsdeploytest_app.consumers.http_consumer"),
]