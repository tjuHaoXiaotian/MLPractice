import time

ISOTIMEFORMAT="%Y-%m-%d %X"
print time.strftime( ISOTIMEFORMAT, time.localtime( time.time() ) )