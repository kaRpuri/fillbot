import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/kabirpuri/fuelbot_ws/install/my_doosan_pkg'
