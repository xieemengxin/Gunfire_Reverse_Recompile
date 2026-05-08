# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_object/reason.pyc
# RelativePath: clientlogic/cl_object/reason.pyc
# Source Generated with Decompyle++
# File: reason.pyc (Python 3.6)

from cl_only import TraceWarning
REASON_TYPE_STR = 1
REASON_TYPE_PERFORM = 2

class CBaseReason(object):
    m_Type = 0
    m_InitOver = 0
    
    def __init__(self, oSrcReason, dData):
        self._CBaseReason__data = { }
        if dData:
            self._CBaseReason__data.update(dData)
        if oSrcReason:
            self.m_SrcReason = oSrcReason
            self.m_Depth = oSrcReason.m_Depth + 1
        else:
            self.m_SrcReason = None
            self.m_Depth = 1
        self.m_InitOver = 1

    
    def ExtInfo(self, dData):
        dExt = { }
        dExt.update(self._CBaseReason__data)
        dExt.update(dData)
        return self.GetCopyReason(dExt)

    
    def GetStrReason(self):
        raise Exception('Reason subclass need overwrite')

    
    def GetCopyReason(self, dExt):
        raise Exception('Reason subclass need overwrite')

    
    def Query(self, sAttr, Default = 0):
        if sAttr in self._CBaseReason__data:
            return self._CBaseReason__data[sAttr]
        return Default

    
    def __setattr__(self, attrname, value):
        if self.m_InitOver:
            raise Exception('Err! Reason attr changed')
        return None

    
    def __str__(self):
        return '%s' % self.GetStrReason()

    
    def __repr__(self):
        return '%s' % self.GetStrReason()

    
    def SetInfo(self, key, value):
        self._CBaseReason__data[key] = value



class CStrReason(CBaseReason):
    m_Type = REASON_TYPE_STR
    
    def __init__(self, sReason, oSrcReason = None, dData = None):
        if not isinstance(sReason, str):
            raise Exception('Err Reason')
        self.m_Reason = sReason
        super(CStrReason, self).__init__(oSrcReason, dData)

    
    def GetStrReason(self):
        return self.m_Reason

    
    def GetCopyReason(self, dExt):
        oReason = CStrReason(self.m_Reason, self.m_SrcReason, dExt)
        return oReason



class CPerformReason(CBaseReason):
    m_Type = REASON_TYPE_PERFORM
    
    def __init__(self, iPerform, iOwner, iSID, iFightType, oSrcReason = None, dData = None):
        self.m_Perform = iPerform
        self.m_Owner = iOwner
        self.m_SID = iSID
        self.m_FightType = iFightType
        super(CPerformReason, self).__init__(oSrcReason, dData)

    
    def GetStrReason(self):
        return 'PF%d|%d|%d|%d' % (self.m_Perform, self.m_Owner, self.m_SID, self.m_FightType)

    
    def GetCopyReason(self, dExt):
        oReason = CPerformReason(self.m_Perform, self.m_Owner, self.m_SID, self.m_FightType, self.m_SrcReason, dExt)
        return oReason


