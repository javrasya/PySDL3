from .__init__ import ctypes, SDL_FUNC

class SDL_Locale(ctypes.Structure):
    _fields_ = [
        ("language", ctypes.c_char_p),
        ("country", ctypes.c_char_p)
    ]

SDL_FUNC("SDL_GetPreferredLocales", ctypes.POINTER(ctypes.POINTER(SDL_Locale)), ctypes.POINTER(ctypes.c_int))