# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_behavior/nodes/actions/noop.pyc
# RelativePath: clientlogic/cl_behavior/nodes/actions/noop.pyc
# Source Generated with Decompyle++
# File: noop.pyc (Python 3.6)

from __future__ import absolute_import
from ... import defines
from ... import behaviortree
from ... import behaviortreetask

class CNoop(behaviortree.CBehaviorNode):
    CLASS_NAME = 'Noop'
    
    def CreateTask(self):
        return CNoopTask()



class CNoopTask(behaviortreetask.CLeafTask):
    
    def Update(self, oAgent, iChildStatus):
        return defines.BT_SUCCESS


