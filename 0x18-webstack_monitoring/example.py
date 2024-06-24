"""
Get all hosts for your organization returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.hosts_api import HostsApi

configuration = Configuration()
DD_SITE = "datadoghq.com"
DD_API_KEY = "50f973be09e0bb5444786c370f7ac479"
DD_APP_KEY = "f83cc296378c245cd2025de4588bbdeb14865401"

with ApiClient(configuration) as api_client:
    api_instance = HostsApi(api_client)
    response = api_instance.list_hosts(
        filter="env:ci",
    )

    print(response)
