"""
This file is only used for local development
and overrides some of the default values from the plugin.
"""

from jupyterhub.auth import DummyAuthenticator
from tljh.configurer import apply_config, load_config
# from tljh_pangeo import tljh_custom_jupyterhub_config
from . import tljh_pangeo
import sys

TLJH_R2D_ADMIN_SCOPE = "custom:tljh_pangeo:admin"

tljh_config = load_config()

apply_config(tljh_config, c)

# tljh_custom_jupyterhub_config(c)


c.JupyterHub.authenticator_class = DummyAuthenticator

c.JupyterHub.allow_named_servers = True
c.JupyterHub.ip = "0.0.0.0"

c.JupyterHub.services.extend(
    [
        {
            "name": "tljh_pangeo",
            "url": "http://127.0.0.1:6789",
            "command": [
                sys.executable,
                "-m",
                "tljh_pangeo",
                "--ip",
                "127.0.0.1",
                "--port",
                "6789",
                "--machine_profiles",
                '{"label": "Small", "cpu": 2, "memory": 2}',
                "--machine_profiles",
                '{"label": "Medium", "cpu": 4, "memory": 4}',
                "--machine_profiles",
                '{"label": "Large", "cpu": 8, "memory": 8}',
            ],
            "oauth_no_confirm": True,
            "oauth_client_allowed_scopes": [
                TLJH_R2D_ADMIN_SCOPE,
            ],
        }
    ]
)

c.JupyterHub.custom_scopes = {
    TLJH_R2D_ADMIN_SCOPE: {
        "description": "Admin access to myservice",
    },
}

c.JupyterHub.load_roles = [
    {
        "description": "Role for tljh_pangeo service",
        "name": "tljh-pangeo-service",
        "scopes": ["read:users", "read:roles:users", "admin:servers"],
        "services": ["tljh_pangeo"],
    },
    {
        "name": "tljh-repodocker-service-admin",
        "users": ["alice"],
        "scopes": [TLJH_R2D_ADMIN_SCOPE],
    },
    {
        "name": "user",
        "scopes": [
            "self",
            # access to the env page
            "access:services!service=tljh_pangeo",
        ],
    },
]
