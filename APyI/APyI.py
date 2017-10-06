#  APyI
from flask import Flask, jsonify

def run(module, args, **kwargs):
    app = Flask(__name__)

    #  default var setup
    ip, port_num, seperator = "localhost", 5000, "+" 

    #  if kwargs are passed
    if kwargs is not None:
        #  overwrite specified vars
        for key, value in kwargs.items():
            if key == "ip":
                ip = value
            elif key == "port":
                port_num = value
            elif key == "separator":
                separator = value

    #  define the flask functions
    @app.route("/{}/<string:arg_string>".format(module.__name__))
    def api(arg_string):
        try:
            arguments = tuple(arg_string.split(separator))
            return str(module(*arguments))
        except:
            return "500"

    @app.route("/_{}_ajax".format(module.__name__))
    def ajax():
        arguments = []
        try:
            for var in args:
                arguments.append(request.args.get(var, None))            
            return jsonify(module(tuple(*arguments)))
        except:
            return jsonify("500")
        
    
    print(" * API available from:\nhttp://{0}:{1}/{2}/[arguments]\nhttp://{0}:{1}/_{2}_ajax".format(ip, port_num, module.__name__))    #  some info on how to make requests to the api
    app.run(host=ip, port=port_num)    #  run the flask server
