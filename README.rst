CGMiner HTTP Interface
======================

A basic HTTP endpoint to any API conforming to the CGMiner RPC interface.

Installation
============

From pip::

    $ pip install cgminerhttpinterface


Usage
=====

Most people will just want to run the server, which means a simple command in
your shell / command prompt:

::

  $ chi-server

This will start an http server reachable on all interfaces on port 80, which
will re-issue incoming requests to localhost:4028 (the default host:port for
the CGMiner RPC API.)


Options
=======

::

  usage: chi-server [-h] [-w HTTP_PORT] [-p API_PORT] [-a API_HOST]

  Start HTTP interface to the monitoring API

  optional arguments:
    -h, --help            show this help message and exit
    -w HTTP_PORT, --http_port HTTP_PORT
                          Port to use for http server
    -p API_PORT, --api_port API_PORT
                          Port used by API server
    -a API_HOST, --api_host API_HOST
                          Host name/address used by API server
