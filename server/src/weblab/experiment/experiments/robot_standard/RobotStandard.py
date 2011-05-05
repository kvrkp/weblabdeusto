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
# Author: Luis Rodríguez <luis.rodriguez@opendeusto.es>
# 

import weblab.experiment.Experiment as Experiment

from voodoo.override import Override
from voodoo.log import logged


import voodoo.log as log
import time
from voodoo.threaded import threaded

DEBUG = False


class RobotStandard(Experiment.Experiment):
    
    def __init__(self, coord_address, locator, cfg_manager, *args, **kwargs):
        super(RobotStandard, self).__init__(*args, **kwargs)
        self._cfg_manager = cfg_manager
        self.read_base_config()

        
    def read_base_config(self):
        """
        Reads the base config parameters from the config file. More parameters will be read through
        the same manager from the actual Virtual Machine Manager, and some may be implementation-specific.
        """
        pass

    @Override(Experiment.Experiment)
    @logged("info")
    def do_start_experiment(self):
        """
        Callback run when the experiment is started.
        """
        if(DEBUG):
            print "[Robot*] do_start_experiment called"
        return "Ok"

    @Override(Experiment.Experiment)
    @logged("info")
    def do_send_command_to_device(self, command):
        """
        Callback run when the client sends a command to the experiment
        @param command Command sent by the client, as a string.
        """
        if(DEBUG):
            print "[Robot*] do_send_command_to_device called"
        return "Ok"


    @Override(Experiment.Experiment)
    @logged("info")
    def do_send_file_to_device(self, content, file_info):
        """ 
        Callback for when the client sends a file to the experiment
        server.
        """
        if(DEBUG):
            print "[Robot*] do_send_file_to_device called"
        return "Ok"


    @Override(Experiment.Experiment)
    @logged("info")
    def do_dispose(self):
        """
        Callback to perform cleaning after the experiment ends.
        """
        if(DEBUG):
            print "[Robot*] do_dispose called"
        return "Ok"
    
