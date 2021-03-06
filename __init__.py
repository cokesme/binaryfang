# Promote useful stuff to toplevel
from __future__ import absolute_import

#load afang plugin
from binaryfang.utils.utils import *
from binaryfang.mm.memtest import *
from binaryfang.dbg.dbgtest import *
from pwn.toplevel import *

pwnlib.args.initialize()
pwnlib.log.install_default_handler()
pwnlib.config.initialize()

log = pwnlib.log.getLogger('pwnlib.exploit')
args = pwnlib.args.args

if not platform.architecture()[0].startswith('64'):
    """Determines if the current Python interpreter is supported by Pwntools.

    See Gallopsled/pwntools#518 for more information."""
    log.warn_once('Pwntools does not support 32-bit Python.  Use a 64-bit release.')

with context.local(log_console=sys.stderr):
    pwnlib.update.check_automatically()
