# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_behavior/nodes/decorators/decoratorloopuntil.pyc
# RelativePath: clientlogic/cl_behavior/nodes/decorators/decoratorloopuntil.pyc
# Source Generated with Decompyle++
# File: decoratorloopuntil.pyc (Python 3.6)

from __future__ import absolute_import
from ... import defines
from . import decoratorcount

class CDecoratorLoopUntil(decoratorcount.CDecoratorCount):
    CLASS_NAME = 'DecoratorLoopUntil'
    
    def __init__(self):
        super(CDecoratorLoopUntil, self).__init__()
        self.m_bUntil = True

    
    def CreateTask(self):
        return CDecoratorLoopUntilTask()

    
    def LoadProperties(self, iVersion, sAgentType, dProperties):
        super(CDecoratorLoopUntil, self).LoadProperties(iVersion, sAgentType, dProperties)
        self.m_bUntil = dProperties['Until']

    
    def GetExportData(self):
        dData = super(CDecoratorLoopUntil, self).GetExportData()
        dData.update({
            'Until': self.m_bUntil })
        return dData



class CDecoratorLoopUntilTask(decoratorcount.CDecoratorCountTask):
    
    def Decorate(self, iStatus):
        if self.m_n > 0:
            self.m_n -= 1
        if self.m_n == 0:
            return defines.BT_SUCCESS
        oNode = self.m_Node
        if oNode.m_bUntil or iStatus == defines.BT_SUCCESS:
            return defines.BT_SUCCESS
        if iStatus == defines.BT_FAILURE:
            return defines.BT_FAILURE
        return defines.BT_RUNNING


