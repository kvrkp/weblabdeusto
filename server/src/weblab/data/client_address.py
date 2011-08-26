#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2005-2009 University of Deusto
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.
#
# This software consists of contributions made by many individuals, 
# listed below:
#
# Author: Pablo Orduña <pablo@ordunya.com>

class ClientAddress(object):
    def __init__(self, address):
        self.client_address = address
    def __repr__(self):
        return "<ClientAddress address='%s' />" % self.client_address