Technical description
=====================

This section describes the internals of a single WebLab-Deusto deployment.
However, the architecture is enriched supporting federation. Go to the
:ref:`federation <federation>` section for further information.

Architecture
------------

Locally, WebLab-Deusto is based on the distributed architecture shown in following diagram:

.. image:: /_static/local_architecture.png
   :width: 600 px
   :align: center

The WebLab-Deusto servers are also based on a distributed design, as can be shown in the following more detailed figure:

.. image:: /_static/local_architecture_protocols.png
   :width: 600 px
   :align: center

In this architecture, clients connect to the core and login servers, using commonly HTTP with JSON (although XML-RPC and SOAP are also supported). These servers manage the authentication, authorization, user tracking, federation (sharing) and scheduling. From there, the system forwards requests to the laboratory servers, which forward them to the final experiments. One exception are the unmanaged laboratories (such as Remote Panels, Virtual Machines or so), where students directly connect to the final host directly (and therefore user tracking is lost).

As detailed later, the communications however enable that all these servers are spread in different machines in a network, or they can all be running on the same machine or even in the same process. For instance, the login server and the core server are usually always in the same process, while the laboratory server may be in other computer and the experiment server could be in the same process as the laboratory server. It just depends on the deployment desired and the required latency.

Technologies
------------

The client is developed `Google Web Toolkit <https://developers.google.com/web-toolkit/>`_, but we support developing a client in Java and in Adobe Flash. The servers provided by WebLab-Deusto (Core Server, Login Server, Laboratory Server) are developed in Python, but we provide `multiple APIs <https://github.com/weblabdeusto/weblabdeusto/tree/master/experiments/managed/libs/server>`_ for developing laboratories in different languages.

The server uses an `ORM <http://en.wikipedia.org/wiki/Object-relational_mapping>`_ called `SQLAlchemy <http://www.sqlalchemy.org/>`_. In theory, WebLab-Deusto should be independent of the database provider, but it has only been tested with `MySQL <http://www.mysql.com>`_ and `SQLite <http://www.sqlite.org/>`_. For scheduling, WebLab-Deusto supports two types of back-ends: database and `Redis <http://redis.io/>`_, which is much faster.

Communications
--------------

WebLab-Deusto communications have been built on top of a pluggable system of protocols. Currently, five protocols have been written, and new protocols could be added. These protocols are Python-dependent SOAP messages, TCP sockets, UNIX sockets, XML-RPC and "Direct", which calls the method name of the server in the same program instance. The decision of choosing between the different communications systems is handled through a communications broker, parameterized by the system administrator. If a server tries to connect to other server, it provides the WebLab-Deusto address of this server, and the communications broker will check what possible protocols can be used and it will automatically choose the fastest one.

Because of this protocol-agnostic system, the Remote Laboratory can be configured in a very flexible way, supporting the avoidance of communications between different tiers if they are not necessary. The advantages and disadvantages of each protocol are summed up in the following image:

.. image:: /_static/protocols.png
   :width: 600 px
   :align: center

The system administrator is responsible for deploying in a secure way. If the system is deployed with a single process running the whole system using "direct", then if the Experiment Server code fails at process level, it may shut the whole server down. Or, if an attacker manages to exploit a vulnerability in a layer of the system and the Login Server is running with the same privileges, the attacker could access sensitive information such as the stored password hashes (or even more, the passwords sent by the users when they log in).

