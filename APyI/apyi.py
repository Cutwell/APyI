#  APyI
from flask import Flask

class API(object):
    def __init__(self):
        pass

    @classmethod
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

        #  define the flask functions
        @app.route("/{}/<string:args>".format(module.__name__))
        def api(args):
            try:
                arguments = tuple(args.split(separator))
                return str(module(*arguments))
            except:
                return "404"

        @app.route("/{}/file_upload.html".format(module.__name__), methods=['GET', 'POST'])
        def form():
            if request.method == 'POST':
                try:
                    file = request.files['file']
                    return str(module(file))
                except Exception as error:
                    print("Form without file. Error: {}".format(error))


        print(" * API available from http://{}:{}/{}/[arguments]".format(ip, port_num, module.__name__))    #  some info on how to make requests to the api
        app.run(host=ip, port=port_num)    #  run the flask server
