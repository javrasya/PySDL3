from .__init__ import ctypes, \
    SDL_FUNC, SDL_SET_CURRENT_BINARY, SDL_BINARY

SDL_SET_CURRENT_BINARY(SDL_BINARY)

SDL_BlendMode = ctypes.c_uint32

SDL_BLENDMODE_NONE = 0x00000000
SDL_BLENDMODE_BLEND = 0x00000001
SDL_BLENDMODE_BLEND_PREMULTIPLIED = 0x00000010
SDL_BLENDMODE_ADD = 0x00000002
SDL_BLENDMODE_ADD_PREMULTIPLIED = 0x00000020
SDL_BLENDMODE_MOD = 0x00000004
SDL_BLENDMODE_MUL = 0x00000008
SDL_BLENDMODE_INVALID = 0x7FFFFFFF

SDL_BlendOperation = ctypes.c_int

SDL_BLENDOPERATION_ADD = 0x1
SDL_BLENDOPERATION_SUBTRACT = 0x2
SDL_BLENDOPERATION_REV_SUBTRACT = 0x3
SDL_BLENDOPERATION_MINIMUM = 0x4
SDL_BLENDOPERATION_MAXIMUM = 0x5

SDL_BlendFactor = ctypes.c_int

SDL_BLENDFACTOR_ZERO = 0x1
SDL_BLENDFACTOR_ONE = 0x2
SDL_BLENDFACTOR_SRC_COLOR = 0x3
SDL_BLENDFACTOR_ONE_MINUS_SRC_COLOR = 0x4
SDL_BLENDFACTOR_SRC_ALPHA = 0x5
SDL_BLENDFACTOR_ONE_MINUS_SRC_ALPHA = 0x6
SDL_BLENDFACTOR_DST_COLOR = 0x7
SDL_BLENDFACTOR_ONE_MINUS_DST_COLOR = 0x8
SDL_BLENDFACTOR_DST_ALPHA = 0x9
SDL_BLENDFACTOR_ONE_MINUS_DST_ALPHA = 0xA

SDL_FUNC("SDL_ComposeCustomBlendMode", SDL_BlendMode, SDL_BlendFactor, SDL_BlendFactor, SDL_BlendOperation, SDL_BlendFactor, SDL_BlendFactor, SDL_BlendOperation)