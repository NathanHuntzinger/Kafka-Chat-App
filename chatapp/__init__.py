# -*- coding: utf-8 -*-
from datatypes import logging


logging.quick_config(
    levels={
        "chatapp": logging.WARNING,
        "datatypes": logging.WARNING,
        "controllers": logging.INFO,
        "producer": logging.INFO,
        "elastic": logging.INFO,
    }
)
