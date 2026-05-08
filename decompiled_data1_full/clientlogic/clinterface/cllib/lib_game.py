# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/clinterface/cllib/lib_game.pyc
# RelativePath: clientlogic/clinterface/cllib/lib_game.pyc
# Source Generated with Decompyle++
# File: lib_game.pyc (Python 3.6)

import cllib.lib_flag
if cllib.lib_flag.g_IsLogicLayer:
    
    try:
        from C_game import SetSomething
    except:
        
        def SetSomething():
            pass

        print('err: no function SetSomething')

else:
    
    def SetSomething():
        pass

