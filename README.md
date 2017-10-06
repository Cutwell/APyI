# APyI
Python RESTful API's made stupidly simple.
---

### How to play:
 - Download the package and run setup.py to install the module.
```bash
$ python3 setup.py install
```
 - Then insert this statement to the end of your module to run it as an API.
```python
if __name__ == "__main__":
    import APyI
    APyI.API.run(function_name)
```

### Options
Using APyI, you can specify a variety of arguments when executing the run command. These arguments can be used for both the command line and scripted forms of APyI, as they are effectively the same code.

All arguments can be specified as key word arguments, e.g.:
```python
APyI.API.run(function, ip="127.0.0.1", port=5000)
```
Although they can also be passed as unlabeled arguments in this order:
```python
APyI.API.run(function, ip, port, separator)
```

#### Required arguments
| Action | Example Usage |
| :-: | :-: |
| Specify a function target for API | APyI.API.run(function_name) |

#### Optional arguments
| Action | Example Argument | Default |
| :-: | :-: | :-: |
| Specify IP to host API from | ip="127.0.0.1" | ip="localhost" |
| Specify port to host API from | port=8080 | port=5000 |
| Change argument separator | separator="\_" | separator="+" |


### Making API requests
You can make a request to a APyI server the same way you would make a request to a regular API. Currently you can make requests in the following form:
```
localhost:5000/<module name>/<string input>
```
Where the <module name> is the actual file name of the module you are running, and <string input> is a single string containing the necessary inputs for the function.
The API then returns a string of the functions output.

### Uploading Files
You can use a form to upload files to your API. Use a POST request to submit a file to the module. Currently you can only upload a single file, without any other arguments, through this method.

#### Argument syntax
 - To specify multiple arguments, use a unique character to separate each argument (This can be changed when you run APyI (default "+")) e.g.:
 ```
localhost:5000/function/arg1+arg2+arg3
 ```
