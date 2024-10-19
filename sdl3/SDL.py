from .SDL_stdinc import *
from .SDL_assert import *
from .SDL_atomic import *
from .SDL_audio import *
from .SDL_bits import *
from .SDL_blendmode import *
from .SDL_camera import *
from .SDL_clipboard import *
from .SDL_cpuinfo import *
from .SDL_dialog import *
from .SDL_endian import *
from .SDL_error import *
from .SDL_events import *
from .SDL_filesystem import *
from .SDL_gamepad import *
from .SDL_guid import *
from .SDL_haptic import *
from .SDL_hidapi import *
from .SDL_hints import *
from .SDL_init import *
from .SDL_iostream import *
from .SDL_joystick import *
from .SDL_keyboard import *
from .SDL_keycode import *
from .SDL_loadso import *
from .SDL_locale import *
from .SDL_log import *
from .SDL_messagebox import *
from .SDL_metal import *
from .SDL_misc import *
from .SDL_mouse import *
from .SDL_mutex import *
from .SDL_pen import *
from .SDL_pixels import *
from .SDL_platform import *
from .SDL_power import *
from .SDL_process import *
from .SDL_properties import *
from .SDL_rect import *
from .SDL_render import *
from .SDL_scancode import *
from .SDL_sensor import *
from .SDL_storage import *
from .SDL_surface import *
from .SDL_system import *
from .SDL_thread import *
from .SDL_time import *
from .SDL_timer import *
from .SDL_touch import *
from .SDL_version import *
from .SDL_video import *

import sys, platform

from .SDL_image import *
from .SDL_mixer import *
from .SDL_net import *

if not (sys.platform in ["linux"] and platform.machine() in ["aarch64"]):
    # SDL_ttf and SDL_rtf are not supported on linux-aarch64 for now.
    from .SDL_ttf import *
    from .SDL_textengine import *
    from .SDL_rtf import *