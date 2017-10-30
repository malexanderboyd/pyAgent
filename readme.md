##  pyAgent

An attempt at a sample python agent to monitor a rest request and display record interesting events about it. Current logging is within console after running `__main__.py`


## How to Install
 (Requires Python 2.7)
```
git clone https://github.com/malexanderboyd/pyAgent.git
cd pyAgent
python setup.py install
python __main__.py

browse to http://127.0.0.1:5000 on your favorite browser.
```


## Configure Agent

Open `agentconfig.json` and find `agentEnabled`. Set this to either `True` or `False` to enable monitoring.


## Resources
[Flask](http://flask.pocoo.org/)
[Requests](http://docs.python-requests.org/en/master/)
[Pympler](https://pythonhosted.org/Pympler/)
[ObjGraph](https://mg.pov.lt/objgraph/)
