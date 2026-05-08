# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_behavior/attachments/attachaction.pyc
# RelativePath: clientlogic/cl_behavior/attachments/attachaction.pyc
# Source Generated with Decompyle++
# File: attachaction.pyc (Python 3.6)

from __future__ import absolute_import
from .. import defines
from .. import behaviortree
from .. import meta

class CAttachAction(behaviortree.CBehaviorNode):
    CLASS_NAME = 'AttachAction'
    
    def __init__(self):
        super(CAttachAction, self).__init__()
        self.m_Method = None

    
    def LoadProperties(self, iVersion, sAgentType, dProperties):
        super(CAttachAction, self).LoadProperties(iVersion, sAgentType, dProperties)
        self.m_Method = meta.ParseMethod(dProperties, 'Method', None)

    
    def Execute(self, oAgent):
        return self.m_Method(oAgent)

    
    def Evaluate(self, oAgent, iChildStatus = None):
        bValid = self.Execute(oAgent)
        if not bValid:
            bValid = defines.BT_SUCCESS == self.UpdateImpl(oAgent, defines.BT_INVALID)
        return bValid

    
    def CreateTask(self):
        pass

    
    def GetExportData(self):
        dData = super(CAttachAction, self).GetExportData()
        dData.update({
            'Method': meta.TransMethod(self.m_Method) })
        return dData


