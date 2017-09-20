#  APyI
from flask import Flask

class API:
    @staticmethod
    def run(module, **kwargs):
        app = Flask(__name__)

        #   variable setup
        ip = "localhost"
        port_num = 5000
        separator = "+"
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "ip":
                    ip = value
                elif key == "port":
                    port_num = value
                elif key == "separator":
                    separator = value
        api_path = "/{}/<string:args>".format(module.__name__)

        #  define the flask functions
        @app.route(api_path)
        def api(args):
            arguments = tuple(args.split(separator))
            return module(*arguments)

        print("API available from:\n{}:{}{}".format(ip, port_num, api_path))    #  some info on how to make requests to the api
        app.run(host=ip, port=port_num)    #  run the flask server


if __name__ == '__main__':
    API.run(port=8080)
