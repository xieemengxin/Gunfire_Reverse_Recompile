# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_behavior/nodes/conditions/false.pyc
# RelativePath: clientlogic/cl_behavior/nodes/conditions/false.pyc
# Source Generated with Decompyle++
# File: false.pyc (Python 3.6)

from __future__ import absolute_import
from ... import defines
from ... import behaviortree
from ... import behaviortreetask

class CFalse(behaviortree.CBehaviorNode):
    CLASS_NAME = 'False'
    
    def AddEffector(self, oAttachment):
        return False

    
    def AddPreCodition(self, oAttachment):
        return False

    
    def CreateTask(self):
        return CFalseTask()



class CFalseTask(behaviortreetask.CLeafTask):
    
    def Update(self, oAgent, iChildStatus):
        return defines.BT_FAILURE


