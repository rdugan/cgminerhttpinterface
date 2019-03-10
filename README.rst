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

This will start an HTTP server reachable on all interfaces on port 8080, which
will re-issue incoming requests to localhost:4028 (the default host:port for
the CGMiner RPC API.)  This server can be started at any time, but will of
course only be useful once the CGMiner API has been started.


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


Using the HTTP Interface
========================

URL structure is *\http://<host>[:port]/<command>[+command...]/[parameter]*. For
example:

- *\http://localhost/summary+pools/* : combined summary and pools report on the
  default port
- *\http://localhost:8081/gpu/0* : single gpu status on port 8081 (as defined in
  the command line)  

Visiting the server root (e.g. *\http://localhost/*) will issue the compound
'summary+devs' command.

At this point in time, the HTTP endpoint will simply serve the response of the
API as is - meaning a JSON formatted data structure containing sections for each
command issued. All commands available via the `CGMiner API`_ are also available
via the HTTP endpoint - in fact the HTTP endpoint performs no command validation
at all, relying on the API to validate requests and respond appropriately.


.. _CGMiner API: https://github.com/ckolivas/cgminer/blob/master/API-README
