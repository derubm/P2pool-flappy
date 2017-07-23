import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'c1c1c1c1'.decode('hex')
P2P_PORT = 11556
ADDRESS_VERSION = 35
RPC_PORT = 11555
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'flappycoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 50
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data))
BLOCK_PERIOD = 60 # s
SYMBOL = 'FLAP'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Flappycoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Flappycoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.flappycoin'), 'flappycoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://blockcrawler.rf.gd/index.php?block_hash='
ADDRESS_EXPLORER_URL_PREFIX = 'http://blockcrawler.rf.gd/index.php?address='
TX_EXPLORER_URL_PREFIX = 'http://blockcrawler.rf.gd/index.php?transaction='
SANE_TARGET_RANGE = (2**256//1000000000 - 1, 2**256//1000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.03e8
