from p2pool.bitcoin import networks

PARENT = networks.nets['flappycoin']
SHARE_PERIOD = 15 # seconds
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 30 # blocks
IDENTIFIER = 'b1c1c2c3b2f68Cd9'.decode('hex')
PREFIX = 'd2c3c4c541c11dd9'.decode('hex')
P2P_PORT = 65150
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 65050
BOOTSTRAP_ADDRS = '24.9.245.200 88.89.11.212 96.52.216.191 54.186.211.206 104.244.216.187'
VERSION_CHECK = lambda v: None if 35 <= v else 'Flappycoin version too old. Upgrade to 0.10.4 or newer!'
VERSION_WARNING = lambda v: None
