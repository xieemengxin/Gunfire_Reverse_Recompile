# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_behavior/nodes/decorators/decoratorrepeat.pyc
# RelativePath: clientlogic/cl_behavior/nodes/decorators/decoratorrepeat.pyc
# Source Generated with Decompyle++
# File: decoratorrepeat.pyc (Python 3.6)

from __future__ import absolute_import
from ... import defines
from . import decoratorcount

class CDecoratorRepeat(decoratorcount.CDecoratorCount):
    CLASS_NAME = 'DecoratorRepeat'
    
    def CreateTask(self):
        return CDecoratorRepeatTask()



class CDecoratorRepeatTask(decoratorcount.CDecoratorCountTask):
    
    def Update(self, oAgent, iChildStatus):
        oNode = self.m_Node
        for i in range(self.m_n):
            iStatus = self.m_Root.Exec(oAgent, iChildStatus)
            if oNode.m_bDecorateWhenChildEnds:
                while True:
                    if iStatus == defines.BT_RUNNING:
                        iStatus = super(CDecoratorRepeatTask, self).Update(oAgent, iChildStatus)
                        continue
            if iStatus == defines.BT_FAILURE:
                return defines.BT_FAILURE
        
        return defines.BT_SUCCESS


