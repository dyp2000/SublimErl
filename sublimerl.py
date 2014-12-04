import sublime
import sublime_plugin
import os
import sys

from .sublimerl_lib.sublimerl_core import SublimErlGlobal
from .sublimerl_lib.sublimerl_completion import SublimErlModuleNameCompletions
from .sublimerl_lib import *

# globals
SUBLIMERL_VERSION = '0.5.1'

def plugin_loaded():
    """Called directly from sublime on plugin load
    """
    package_folder = os.path.dirname(__file__)
    if os.path.exists(os.path.join(package_folder, 'sublimerl_lib')):
        sys.path.append(os.path.join(package_folder, 'sublimerl_lib'))

    # initialize
    SUBLIMERL = SublimErlGlobal()
    SublimErlModuleNameCompletions().set_completions_threaded(SUBLIMERL)
