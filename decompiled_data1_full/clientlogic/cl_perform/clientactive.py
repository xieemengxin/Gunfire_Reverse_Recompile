# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/clientactive.pyc
# RelativePath: clientlogic/cl_perform/clientactive.pyc
# Source Generated with Decompyle++
# File: clientactive.pyc (Python 3.6)

from cl_commondefines import DAM_TYPE_NORMAL, PF_TYPE_TRIGGERCLIENT, PF_SUBMSG_CLIENTACTIVE
from cl_perform.mobject import CPerform as CCustomPerform
import cl_object.elementtype as elementtype
import cl_msgcenter

class CPerform(CCustomPerform):
    m_PFType = PF_TYPE_TRIGGERCLIENT
    m_SubMsg = PF_SUBMSG_CLIENTACTIVE
    m_ElementType = DAM_TYPE_NORMAL
    m_UnCrtByOwnerSign = 1
    m_SyncCanUseCount = False
    m_CanUseCountMax = 0
    
    def __init__(self, oOwner, iLevel):
        super(CPerform, self).__init__(oOwner, iLevel)
        self.m_CanUseCount = 0
        self.m_TrueCanUseCountMax = self.m_CanUseCountMax

    
    def AddCanUseCount(self, iAdd = 1, bSync = True):
        if self.m_TrueCanUseCountMax and iAdd > 0:
            iAdd = min(self.m_TrueCanUseCountMax - self.m_CanUseCount, iAdd)
            if iAdd <= 0:
                return None
        self.m_CanUseCount += iAdd
        if iAdd > 0:
            dMsgInfo = {
                'pfid': self.m_SID,
                'UseCountAdd': iAdd }
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CLIENTACTIVEUSECOUNTCHANGE, self.GetOwner(), dMsgInfo)
        if self.m_SyncCanUseCount and bSync:
            self.GS2CPerformPropChange('CanUseCount', self.m_CanUseCount)

    
    def AddCanUseCountMax(self, iAdd = 1):
        self.m_TrueCanUseCountMax += iAdd

    
    def CanUse(self, oWarrior, dInfo):
        if self.m_CanUseCount < 1:
            return 0
        return super().CanUse(oWarrior, dInfo)

    
    def UsePerform(self, oWarrior, oSkill, bSync = True):
        self.AddCanUseCount(-1, bSync)
        super().UsePerform(oWarrior, oSkill)

    
    def OnInit(self):
        self.m_ElementTypeObj = elementtype.CPerformElementType(self, self.m_ElementType)

    
    def AttrCache(self):
        dData = { }
        for sAttr in self.m_Attr:
            dData[sAttr] = self.CalAttr(sAttr)
        
        for sAttr, iValue in self.m_BaseArgData.items():
            dData[sAttr] = iValue
        
        dData['ElementType'] = self.m_ElementType
        return dData


