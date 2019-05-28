import socket

if socket.gethostname()=='AT.local':
    from .dev import *
else:
    from .prod import *