//
// Copyright (C) 2005-2009 University of Deusto
// All rights reserved.
//
// This software is licensed as described in the file COPYING, which
// you should have received as part of this distribution.
//
// This software consists of contributions made by many individuals,
// listed below:
//
// Author: Luis Rodr�guez <4lurodri@rigel.deusto.es>
//         Jaime Irurzun <jaime.irurzun@gmail.com>
//

#ifndef WEBLAB_LIB
#define WEBLAB_LIB

#define TRUE  1
#define FALSE 0

int default_is_up_and_running();

struct ExperimentServer{
    char * (* start_experiment)();
    char * (* send_file)(char * encoded_file, char * fileinfo);
    char * (* send_command)(char * command);
    char * (* dispose)();
    int    (* is_up_and_running)();
};

void launch(int port, struct ExperimentServer handlers);

#endif
