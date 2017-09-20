# APyI
Python RESTful API's made stupidly simple.
---

### 2 ways to play:

#### 1
 - Download the package and run setup.py to install the module.
```bash
$ python3 setup.py
```
 - Then insert this statement to the end of your module to run it as an API.
```python
if __name__ == "__main__":
    import apyi
    apyi.API.run(function_name())
```

#### 2
 - Download this package and run mac_install.py to create a command line alias.
```bash
$ python3 mac_install.py
```

 - Then run a module as an API using the following command.
```bash
$ apyi run module.py
```

### Options
Using APyI, you can specify a variety of arguments when executing the run command. These arguments can be used for both the command line and scripted forms of APyI, as they are effectively the same code.

All arguments should be specified as key word arguments, e.g.:
```bash
$ apyi run module.py ip="127.0.0.1" port=5000
```
#### Required arguments
| Action | Example Usage |
| :-: | :-: |
| Specify a function target for API | apyi.API.run(function_name()) |

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

#### Argument syntax
 - To specify multiple arguments, use a unique character to separate each argument. This can be changed when you run APyI (default "+")
