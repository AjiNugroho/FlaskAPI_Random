# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os

class Config(object):

    DEBUG = True

    #log
    LOG_LEVEL = 'INFO'

    # # DATABASE SECTION
    MYSQL_HOST = os.getenv('DB_HOST', '127.0.0.1')
    MYSQL_USER = os.getenv('DB_USER', 'root')
    MYSQL_PASSWORD = os.getenv('DB_PASS', '')
    MYSQL_DB = os.getenv('DB_NAME', 'discount')
    MYSQL_PORT = 3306
