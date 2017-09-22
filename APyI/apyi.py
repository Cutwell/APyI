#  APyI
from flask import Flask

class API:
    @staticmethod
    def run(module, *args, **kwargs):
        app = Flask(__name__)

        #  if args are passed
        if args is not None:
            file_name, function_name, ip, port_num, separator = list(args) + [0]*(5 - len(args))

        #   variable setup
        ip = "localhost" if ip == 0 else ip
        port_num = 5000 if port_num == 0 else port_num
        separator = "+" if separator == 0 else separator

        #  if kwargs are passed
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "ip":
                    ip = value
                elif key == "port":
                    port_num = value
                elif key == "separator":
                    separator = value
                elif key == "module":
                    module = value
        api_path = "/{}/<string:args>".format(module.__name__)

        #  define the flask functions
        @app.route(api_path)
        def api(args):
            try:
                arguments = tuple(args.split(separator))
                return str(module(*arguments))
            except:
                return "404"

        print(" * API available from http://{}:{}/{}/[arguments]".format(ip, port_num, module.__name__))    #  some info on how to make requests to the api
        app.run(host=ip, port=port_num)    #  run the flask server
