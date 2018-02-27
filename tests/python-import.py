def function(var):
    return "var: {}".format(var)

if __name__ == "__main__":
    
    from APyI import run
    run(function, args=("string"))
