# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_behavior/nodes/decorators/decoratorloop.pyc
# RelativePath: clientlogic/cl_behavior/nodes/decorators/decoratorloop.pyc
# Source Generated with Decompyle++
# File: decoratorloop.pyc (Python 3.6)

from __future__ import absolute_import
from ... import defines
from . import decoratorcount

class CDecoratorLoop(decoratorcount.CDecoratorCount):
    CLASS_NAME = 'DecoratorLoop'
    
    def __init__(self):
        super(CDecoratorLoop, self).__init__()
        self.m_bDoneWithinFrame = False

    
    def CreateTask(self):
        return CDecoratorLoopTask()

    
    def LoadProperties(self, iVersion, sAgentType, dProperties):
        super(CDecoratorLoop, self).LoadProperties(iVersion, sAgentType, dProperties)
        self.m_bDoneWithinFrame = dProperties['DoneWithinFrame']

    
    def GetExportData(self):
        dData = super(CDecoratorLoop, self).GetExportData()
        dData.update({
            'DoneWithinFrame': self.m_bDoneWithinFrame })
        return dData



class CDecoratorLoopTask(decoratorcount.CDecoratorCountTask):
    
    def Decorate(self, iStatus):
        if self.m_n > 0:
            self.m_n -= 1
            if self.m_n == 0:
                return defines.BT_SUCCESS
            return defines.BT_RUNNING
        if self.m_n == -1:
            return defines.BT_RUNNING
        return defines.BT_SUCCESS

    
    def Update(self, oAgent, iChildStatus):
        oNode = self.m_Node
        if oNode.m_bDoneWithinFrame:
            for i in range(self.m_n):
                iStatus = self.m_Root.Exec(oAgent, iChildStatus)
                if oNode.m_bDecorateWhenChildEnds:
                    while True:
                        if iStatus == defines.BT_RUNNING:
                            iStatus = super(CDecoratorLoopTask, self).Update(oAgent, iChildStatus)
                            continue
                if iStatus == defines.BT_FAILURE:
                    return defines.BT_FAILURE
            
            return defines.BT_SUCCESS
        return super(CDecoratorLoopTask, self).Update(oAgent, iChildStatus)


