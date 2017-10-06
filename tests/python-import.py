def function(var):
    return "var: {}".format(var)

if __name__ == "__main__":
    from APyI.API import run
    run(function, args=("string"))
