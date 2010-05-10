/*
* Copyright (C) 2005-2009 University of Deusto
* All rights reserved.
*
* This software is licensed as described in the file COPYING, which
* you should have received as part of this distribution.
*
* This software consists of contributions made by many individuals, 
* listed below:
*
* Author: Pablo Orduña <pablo@ordunya.com>
*
*/ 
package es.deusto.weblab.client.lab.experiments.plugins.es.deusto.weblab.gpib2.ui;

import es.deusto.weblab.client.configuration.IConfigurationManager;
import es.deusto.weblab.client.lab.experiments.plugins.es.deusto.weblab.gpib.ui.WlDeustoGpibBoard;

public class WlDeustoGpib2Board extends WlDeustoGpibBoard {
	
	public static final String DEFAULT_GPIB2_WEBCAM_IMAGE_URL       = "http://gpib2.weblab.deusto.es/cliente/camview.jpg";
	
	public WlDeustoGpib2Board(IConfigurationManager configurationManager, IBoardBaseController commandSender) {
		super(configurationManager, commandSender);		
	}
		
	@Override
	protected String getDefaultWebcamImageUrl(){
		return WlDeustoGpib2Board.DEFAULT_GPIB2_WEBCAM_IMAGE_URL;
	}
}