#!/usr/bin/env python3

# pylint: disable=invalid-name

"""Gunicorn configuration"""

accesslog = "-"
bind = "0.0.0.0:8080"
disable_redirect_access_to_syslog = True
forwarded_allow_ips = "*"
workers = 1