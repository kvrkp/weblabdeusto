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
package es.deusto.weblab.client.experiments.gpib1.ui;

import es.deusto.weblab.client.configuration.IConfigurationRetriever;
import es.deusto.weblab.client.experiments.gpib.ui.GpibExperiment;
import es.deusto.weblab.client.lab.experiments.IBoardBaseController;

public class WlDeustoGpib1Board extends GpibExperiment {
	
	public static final String DEFAULT_GPIB1_WEBCAM_IMAGE_URL       = "https://www.weblab.deusto.es/webcam/gpib1/image.jpg";
	
	public WlDeustoGpib1Board(IConfigurationRetriever configurationRetriever, IBoardBaseController commandSender) {
		super(configurationRetriever, commandSender);		
	}
		
	@Override
	protected String getDefaultWebcamImageUrl(){
		return WlDeustoGpib1Board.DEFAULT_GPIB1_WEBCAM_IMAGE_URL;
	}
}