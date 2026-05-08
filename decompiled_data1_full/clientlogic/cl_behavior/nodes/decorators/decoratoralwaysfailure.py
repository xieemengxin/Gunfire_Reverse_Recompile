# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_behavior/nodes/decorators/decoratoralwaysfailure.pyc
# RelativePath: clientlogic/cl_behavior/nodes/decorators/decoratoralwaysfailure.pyc
# Source Generated with Decompyle++
# File: decoratoralwaysfailure.pyc (Python 3.6)

from __future__ import absolute_import
from ... import defines
from ... import behaviortree
from ... import behaviortreetask

class CDecoratorAlwaysFailure(behaviortree.CDecoratorNode):
    CLASS_NAME = 'DecoratorAlwaysFailure'
    
    def __init__(self):
        super(CDecoratorAlwaysFailure, self).__init__()

    
    def CreateTask(self):
        return CDecoratorAlwaysFailureTask()



class CDecoratorAlwaysFailureTask(behaviortreetask.CDecoratorTask):
    
    def __init__(self):
        super(CDecoratorAlwaysFailureTask, self).__init__()

    
    def Decorate(self, iStatus):
        return defines.BT_FAILURE


