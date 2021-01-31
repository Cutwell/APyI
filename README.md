# Easy-Python-Remote-Interfaces
---

1. Download the package and run setup.py to install the module.
```bash
$ python3 setup.py install
```
2. Then insert this statement to the end of your module to run it as an API.
```python
if __name__ == "__main__":
    from APyI import run
    run(function, args=())
```

### Function arguments
When calling the API.run method, you must pass the target function object as well as the arguments this function takes.
If you intend to call the API through JQuery Ajax, you must pass the name of each argument inside the args tuple, e.g.:
```python
run(function_name, args=("string", "integer"))
```
 - Note: if you only intend to call the API via the URL method, you can leave args blank.

### Server options
You can specify a variety of arguments when executing the run command. These arguments can be used for both the command line and scripted forms of APyI, as they are effectively the same code.

All arguments can be specified as key word arguments, e.g.:
```python
run(function, args=(), ip="127.0.0.1", port=5000)
```


#### Required arguments
| Action | Example Usage |
| :-: | :-: |
| Specify a function target for API | APyI.API.run(function_name) |
| Specify the arguments the function uses | APyI.API.run(args=("string", "integer")) |

#### Optional arguments
| Action | Example Argument | Default |
| :-: | :-: | :-: |
| Specify IP to host API from | ip="127.0.0.1" | ip="localhost" |
| Specify port to host API from | port=8080 | port=5000 |
| Change argument separator | separator="\_" | separator="+" |


### Making API requests
You can make a request to the server the same way you would make a request to a regular API. You can make requests in the following form:
```
localhost:5000/<function name>/<string input>
```
Where the <function name> is the name of the function you are running, and <string input> is a single string containing the necessary inputs for the function.
 - Note: When calling the API in this method, all outputs are returned as a single string.

You can also use JQuery and Ajax to make requests to the API. You should structure your requests like so:
```javascript
$.ajax({
	url: "localhost:5000/_<function name>_ajax",
	
	// optional arguments are passed in a dictionary
	data: {string:"this is an example", integer:42,},
	
	success: function(result){
		// handle the request
	}
});
```
 - Note: The default fall-back for an empty/non-existent argument is a None value.
 - Note: Unlike the URL method, output types are retained using this method.

If the module or target function should encounter an error during handling of a request, a server error 500 code is returned, either as a JSON or string, dependent on the method used to make the request originally.
