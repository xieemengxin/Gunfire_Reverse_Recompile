# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_msgcenter/eventcbobj.pyc
# RelativePath: clientlogic/cl_msgcenter/eventcbobj.pyc
# Source Generated with Decompyle++
# File: eventcbobj.pyc (Python 3.6)

from cl_only import PythonError, SendAlert
from cl_object.logging import EventcbactionLog
import cl_object.reason

class CEventCB(object):
    m_CBSelf = 1
    
    def __init__(self, cbFunc, sKey):
        self.m_CBFuncAction = cbFunc
        self.m_Key = sKey
        self.m_EventCBActionData = { }
        self.m_EventCBActionStack = []

    
    def Key(self):
        return self.m_Key

    
    def GetStableKey(self, dEvent):
        if 'LifeCycle' in dEvent and dEvent['LifeCycle']:
            return dEvent['LifeCycle'].GetStableKey()
        return self.m_Key

    
    def GetCBFuncAction(self):
        return self.m_CBFuncAction

    
    def CBFuncAction(self, oTarget, iGroup, dEvent, dMsgInfo):
        if not (self.m_CBFuncAction) or iGroup not in self.m_CBFuncAction:
            EventcbactionLog.TraceAlert('%d %s未找到回调行为组%s' % (oTarget.m_OwnerPlayerID, self.GetStableKey(dEvent), iGroup))
            return None
        if not self.InitEventCBInfo(dEvent, dMsgInfo, iGroup):
            return None
        
        try:
            self.m_CBFuncAction[iGroup](self, oTarget)
        except:
            PythonError()

        self.ClearEventCBInfo(iGroup)

    
    def InitEventCBInfo(self, dEventInfo, dMsgInfo, oSubActionKey = 0):
        if oSubActionKey in self.m_EventCBActionData:
            return False
        dActionInfo = { }
        dActionInfo['TransInfo'] = { }
        dActionInfo['EventInfo'] = dEventInfo
        if 'ItemID' not in dEventInfo:
            dActionInfo['EventInfo']['ItemID'] = 0
        dActionInfo['MsgInfo'] = dMsgInfo
        self.m_EventCBActionData[oSubActionKey] = dActionInfo
        self.m_EventCBActionStack.append(oSubActionKey)
        return True

    
    def ClearEventCBInfo(self, oSubActionKey = 0):
        if self.m_EventCBActionStack[-1] != oSubActionKey or oSubActionKey not in self.m_EventCBActionData:
            raise Exception('清理事件回调行为信息时栈信息错误')
        self.m_EventCBActionStack.pop(-1)
        self.m_EventCBActionData.pop(oSubActionKey)

    
    def GetCBTransInfo(self):
        if not self.m_EventCBActionStack:
            return None
        oKey = self.m_EventCBActionStack[-1]
        return self.m_EventCBActionData[oKey]['TransInfo']

    
    def GetCBMsgInfo(self):
        if not self.m_EventCBActionStack:
            return None
        oKey = self.m_EventCBActionStack[-1]
        return self.m_EventCBActionData[oKey]['MsgInfo']

    
    def GetCBEventInfo(self):
        if not self.m_EventCBActionStack:
            return None
        oKey = self.m_EventCBActionStack[-1]
        return self.m_EventCBActionData[oKey]['EventInfo']

    
    def GetCBEventData(self, sArg):
        if not self.m_EventCBActionStack:
            return None
        oKey = self.m_EventCBActionStack[-1]
        if 'ArgData' not in self.m_EventCBActionData[oKey]['EventInfo']:
            return None
        if sArg in self.m_EventCBActionData[oKey]['EventInfo']['ArgData']:
            return self.m_EventCBActionData[oKey]['EventInfo']['ArgData'][sArg]

    
    def GetCBLifeCycle(self):
        return self.GetCBEventInfo()['LifeCycle']

    
    def GetObject(self):
        if not self.m_EventCBActionStack:
            return None
        oKey = self.m_EventCBActionStack[-1]
        oLifeCycle = self.m_EventCBActionData[oKey]['EventInfo']['LifeCycle']
        return oLifeCycle.GetObject()

    
    def CBReason(self, sDefault = ''):
        dEventInfo = self.GetCBEventInfo()
        dCBMsgInfo = self.GetCBMsgInfo()
        if 'RS' in dEventInfo:
            oReason = dEventInfo['RS']
        elif 'RS' in dCBMsgInfo:
            oReason = dCBMsgInfo['RS']
        elif not sDefault:
            sDefault = self.Key()
        oReason = cl_object.reason.CStrReason(sDefault)
        return oReason

    
    def SetMaxCBCycle(self, iCount):
        SendAlert('err', '%s 暂不支持设置循环次数，如有需求请联系后端值班' % self.Key())


MAX_CB_CYCLE = 5

class CCycleEventCB(CEventCB):
    
    def __init__(self, cbFunc, sKey):
        super().__init__(cbFunc, sKey)
        self.m_CBCycle = { }
        self.m_MaxCBCycle = 0
        self.m_CacheInfo = []

    
    def CBFuncAction(self, oTarget, iGroup, dEvent, dMsgInfo):
        if not (self.m_CBFuncAction) or iGroup not in self.m_CBFuncAction:
            EventcbactionLog.TraceAlert('%d %s未找到回调行为组%s' % (oTarget.m_OwnerPlayerID, self.GetStableKey(dEvent), iGroup))
            return None
        if iGroup not in self.m_CBCycle:
            self.m_CBCycle[iGroup] = 0
        if not self.InitEventCBInfo(dEvent, dMsgInfo, iGroup):
            return None
        
        try:
            self.m_CBCycle[iGroup] += 1
            self.m_CBFuncAction[iGroup](self, oTarget)
            self.m_CBCycle[iGroup] -= 1
        except:
            PythonError()

        self.ClearEventCBInfo(iGroup)

    
    def InitEventCBInfo(self, dEventInfo, dMsgInfo, oSubActionKey = 0):
        if oSubActionKey in self.m_EventCBActionData:
            if self.m_MaxCBCycle or self.m_CBCycle[oSubActionKey] > self.m_MaxCBCycle:
                EventcbactionLog.TraceAlert('%s-%s 循环次数 %s > %s  msginfo:%s' % (self.Key(), oSubActionKey, self.m_CBCycle[oSubActionKey], self.m_MaxCBCycle, dMsgInfo))
                return False
            return False
        dActionInfo = { }
        dActionInfo['TransInfo'] = { }
        dActionInfo['EventInfo'] = dEventInfo
        if 'ItemID' not in dEventInfo:
            dActionInfo['EventInfo']['ItemID'] = 0
        dActionInfo['MsgInfo'] = dMsgInfo
        if oSubActionKey in self.m_EventCBActionData:
            self.m_CacheInfo.append(self.m_EventCBActionData[oSubActionKey])
        self.m_EventCBActionData[oSubActionKey] = dActionInfo
        self.m_EventCBActionStack.append(oSubActionKey)
        return True

    
    def ClearEventCBInfo(self, oSubActionKey = 0):
        if self.m_EventCBActionStack[-1] != oSubActionKey or oSubActionKey not in self.m_EventCBActionData:
            raise Exception('清理事件回调行为信息时栈信息错误')
        self.m_EventCBActionStack.pop(-1)
        if self.m_CBCycle[oSubActionKey] <= 0:
            self.m_EventCBActionData.pop(oSubActionKey)
        else:
            self.m_EventCBActionData[oSubActionKey] = self.m_CacheInfo.pop(-1)

    
    def SetMaxCBCycle(self, iCount):
        if iCount > MAX_CB_CYCLE:
            SendAlert('err', '%s 事件设置循环次数 %s 超出上限 %s，请联系后端值班' % (self.Key(), iCount, MAX_CB_CYCLE))
            iCount = MAX_CB_CYCLE
        self.m_MaxCBCycle = iCount


