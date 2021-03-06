#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2005 onwards University of Deusto
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.
#
# This software consists of contributions made by many individuals,
# listed below:
#
# Author: Pablo Orduña <pablo@ordunya.com>
#
import voodoo.gen.generators.ClientSkel as ClientSkel
import voodoo.gen.exceptions.protocols.ProtocolErrors as ProtocolErrors

import xmlrpclib

import voodoo.gen.protocols.XMLRPC.Errors as Exceptions

# Stubs of client methods to dynamically generate
# All of them must have the same name format:
#
# _prefix_stub
#
# Where prefix can be:
#    "":                        The method does what it must do (its action)
#    "call_begin"               Designed for asynchronous communication (not used for the moment)
#    "call_is_running"      Designed for asynchronous communication (not used for the moment)
#    "call_get_result"      Designed for asynchronous communication (not used for the moment)

def _generate_stub(METHOD_NAME):
    def _stub(self,*parameters,**kparameters):
        """ Dynamically generated method. Protocol: XMLRPC.
             Method name: METHOD_NAME. Documentation: DOCUMENTATION """
        try:
            return getattr(self._server,'Util.%s' % METHOD_NAME)(*parameters,**kparameters)
        except xmlrpclib.Fault as ft:
            raise Exceptions.UnknownFaultType(
                    "Unknown fault type: " + str(ft.faultCode) + ": " + str(ft.faultString),
                    ft
                )
        except Exception as e:
            raise ProtocolErrors.UnknownRemoteError(
                    "Unknown exception: " + str(e.__class__) + "; " + str(e),
                    e
                )
    return _stub

def _generate_call_begin_stub(METHOD_NAME):
    # Not used for the moment but requierd by ClientSkel
    def _call_begin_stub(self,*parameters,**kparameters):
        """ Dynamically generated method. Protocol: XMLRPC.
             Method name: METHOD_NAME. Documentation: DOCUMENTATION """
        return getattr(self._server,'begin_'+METHOD_NAME)(*parameters,**kparameters)
    return _call_begin_stub

def _generate_call_is_running_stub(METHOD_NAME):
    # Not used for the moment but requierd by ClientSkel
    def _call_is_running_stub(self,server_key,block):
        """ Dynamically generated method. Protocol: XMLRPC.
             Method name: METHOD_NAME. Documentation: DOCUMENTATION """
        return getattr(self._server,'is_running_'+METHOD_NAME)(server_key,block)
    return _call_is_running_stub

def _generate_call_get_result_stub(METHOD_NAME):
    # Not used for the moment but requierd by ClientSkel
    def _call_get_result_stub(self,server_key):
        """ Dynamically generated method. Protocol: XMLRPC.
             Method name: METHOD_NAME. Documentation: DOCUMENTATION """
        return getattr(self._server,'get_result_'+METHOD_NAME)(server_key)
    return _call_get_result_stub

# Tuple with the stub pointers of the stubs to generate
stubs = (
    _generate_stub,
    _generate_call_begin_stub,
    _generate_call_is_running_stub,
    _generate_call_get_result_stub
)

def generate(methods):
    clientSkel = ClientSkel.generate(methods)

    class ClientXMLRPC(clientSkel):

        def __init__(self, url, port=80, uri='/'):
            clientSkel.__init__(self,xmlrpclib.Server('http://'+url+':'+str(port)+uri, allow_none = True))

    # Adding properly the testing method to check availability
    if isinstance(methods,dict):
        all_methods = methods.keys()
    else:
        all_methods = list(methods[:])
    all_methods.append('test_me')

    # Generating stubs dinamically
    for method_name in all_methods:
        # Each method can have many stubs (with different prefixes)
        for stub in stubs:
            func = stub(method_name)
            # Setting docstring
            func.__doc__ = (func.__doc__ if func.__doc__ is not None else '').replace('METHOD_NAME', method_name)
            if isinstance(all_methods, dict):
                func.__doc__ = (func.__doc__ if func.__doc__ is not None else '').replace('DOCUMENTATION', all_methods[method_name])
            # Taking "prefix_" from "_prefix_stub"
            stub_prefix = stub.func_name[len('_generate_'):]
            stub_prefix = stub_prefix[:stub_prefix.rfind('stub')]
            func_name = stub_prefix + method_name
            func.func_name = func_name
            setattr(ClientXMLRPC, func_name, func)

    return ClientXMLRPC
