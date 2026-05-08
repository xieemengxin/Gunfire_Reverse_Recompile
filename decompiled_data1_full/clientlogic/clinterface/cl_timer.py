# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/clinterface/cl_timer.pyc
# RelativePath: clientlogic/clinterface/cl_timer.pyc
# Source Generated with Decompyle++
# File: cl_timer.pyc (Python 3.6)

import cllib.lib_flag
if cllib.lib_flag.g_IsLogicLayer:
    from C_logic import CreateLObject, DeleteLObject
    from C_logic import TimerCall, FindTimerCall, RemoveTimerCall, ClearTimerCall
    
    class CTimerObject(object):
        
        def __init__(self, iTimerID):
            self.m_ID = iTimerID


    
    class CTimerManager(object):
        
        def CreateTimer(self):
            obj = CTimerObject(0)
            obj.m_ID = CreateLObject(0, {
                'object': obj })
            return obj.m_ID

        
        def DeleteTimer(self, iTimerID):
            DeleteLObject(iTimerID)

        
        def TimerCall(self, iTimerID, sFlag, iDelayTime, func):
            TimerCall(iTimerID, func, iDelayTime, sFlag)

        
        def FindTimer(self, iTimerID, sFlag):
            return FindTimerCall(iTimerID, sFlag)

        
        def RemoveTimerCall(self, iTimerID, sFlag):
            RemoveTimerCall(iTimerID, sFlag)

        
        def ClearTimerCall(self, iTimerID):
            ClearTimerCall(iTimerID)


else:
    from C_object import CreateObject, DeleteObject
    from C_object import TimerCall, FindTimerCall, RemoveTimerCall, RemoveAllCallOut
    
    class CTimerObject(object):
        
        def __init__(self, iTimerID):
            self.m_ID = iTimerID


    
    class CTimerManager(object):
        
        def CreateTimer(self):
            obj = CTimerObject(0)
            obj.m_ID = CreateObject(0, {
                'object': obj })
            return obj.m_ID

        
        def DeleteTimer(self, iTimerID):
            DeleteObject(iTimerID)

        
        def TimerCall(self, iTimerID, sFlag, iDelayTime, func):
            TimerCall(iTimerID, func, iDelayTime, sFlag)

        
        def FindTimer(self, iTimerID, sFlag):
            return FindTimerCall(iTimerID, sFlag)

        
        def RemoveTimerCall(self, iTimerID, sFlag):
            RemoveTimerCall(iTimerID, sFlag)

        
        def ClearTimerCall(self, iTimerID):
            RemoveAllCallOut(iTimerID)


if 'g_TimerMgr' not in globals():
    g_TimerMgr = CTimerManager()
    g_GlobalTimer = g_TimerMgr.CreateTimer()

def Logic_Call_Out(func, delaytime, flag):
    if delaytime <= 0:
        delaytime = 1
    g_TimerMgr.TimerCall(g_GlobalTimer, flag, delaytime, func)


def Logic_Find_Call_Out(flag):
    return g_TimerMgr.FindTimer(g_GlobalTimer, flag)


def Logic_Remove_Call_Out(flag):
    g_TimerMgr.RemoveTimerCall(g_GlobalTimer, flag)


def Logic_Remove_All_Call_Out():
    g_TimerMgr.ClearTimerCall(g_GlobalTimer)

