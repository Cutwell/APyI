#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
'''APyI.

Handles URL and Ajax API requests with a target Python function.

'''

#  used to host a RESTful server and return valid JSON objects.
from flask import Flask, jsonify

def run(module, **kwargs):
    '''Controls setup of API with flask.

    Args:
        module: A function object from the target program.
        **kwargs: A series of named arguments, e.g.: ip, port, seperator.
    
    Kwargs:
        ip: The ip address to host the API from, defaults to 'localhost'.
        port: The port number of the target host machine, defaults to '5000'.
        seperator: The character seperator for URL requests, defaults to '+'.

    Returns:
        None: Runs perpetually until interrupted.

    '''

    #  create an instance of the Flask server.
    app = Flask(__name__)

    #  default var setup
    ip, port_num, seperator = "localhost", 5000, "+"

    #  if kwargs are passed
    if kwargs is not None:
        #  overwrite specified vars with passed arguments
        for key, value in kwargs.items():
            if key == "ip":
                ip = value
            elif key == "port":
                port_num = value
            elif key == "separator":
                separator = value

    #  create a server route from /[module_name]/[arguments] for URL requests
    @app.route("/{}/<string:arg_string>".format(module.__name__))
    def api(arg_string):
        '''Handles API requests from URL strings.

        Args:
            arg_string: An unparsed string of arguments from the URL.

        Returns:
            str(module(*arguments)): A string containing the output of the target program.
            "500": A 'Server Error' HTML code.

        '''

        try:
            #  convert the string into a list by splitting at the separator character and converting to a tuple.
            arguments = tuple(arg_string.split(separator))
            #  attempt to get an output using the passed arguments.
            return str(module(*arguments))
        except:
            #  if this fails, return a '500' error code.
            return "500"

    #  create a server route from /_[module name]_ajax for ajax requests
    @app.route("/_{}_ajax".format(module.__name__))
    def ajax():
        '''Handles API requests from ajax.

        Args:
            None: Arguments are loaded from a JSON object in the URL.

        Returns:
            jsonify(module(tuple(*arguments))): A JSON object of the output of the target program.
            jsonify("500"): A 'Server Error' HTML code.

        '''

        arguments = []
        try:
            #  create a list of arguments from the JSON object.
            for var in args:
                arguments.append(request.args.get(var, None))
            #  convert the list to a tuple and attempt to get an output using the passed arguments.
            return jsonify(module(tuple(*arguments)))
        except:
            #  if this fails, return a '500' error code.
            return jsonify("500")

    #  print out info text on server settings.
    print(" * API available from:\nhttp://{0}:{1}/{2}/[arguments]\nand\nhttp://{0}:{1}/_{2}_ajax".format(ip, port_num, module.__name__))    #  some info on how to make requests to the api
    #  host the flask server from the specified ip and port.
    app.run(host=ip, port=port_num)
