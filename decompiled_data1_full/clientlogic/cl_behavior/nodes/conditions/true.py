# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_behavior/nodes/conditions/true.pyc
# RelativePath: clientlogic/cl_behavior/nodes/conditions/true.pyc
# Source Generated with Decompyle++
# File: true.pyc (Python 3.6)

from __future__ import absolute_import
from ... import defines
from ... import behaviortree
from ... import behaviortreetask

class CTrue(behaviortree.CBehaviorNode):
    CLASS_NAME = 'True'
    
    def CreateTask(self):
        return CTrueTask()

    
    def AddEffector(self, oAttachment):
        return False

    
    def AddPreCodition(self, oAttachment):
        return False



class CTrueTask(behaviortreetask.CLeafTask):
    
    def Update(self, oAgent, iChildStatus):
        return defines.BT_SUCCESS


