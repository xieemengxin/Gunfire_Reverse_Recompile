# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_behavior/nodes/decorators/decoratoralwayssuccess.pyc
# RelativePath: clientlogic/cl_behavior/nodes/decorators/decoratoralwayssuccess.pyc
# Source Generated with Decompyle++
# File: decoratoralwayssuccess.pyc (Python 3.6)

from __future__ import absolute_import
from ... import defines
from ... import behaviortree
from ... import behaviortreetask

class CDecoratorAlwaysSuccess(behaviortree.CDecoratorNode):
    CLASS_NAME = 'DecoratorAlwaysSuccess'
    
    def __init__(self):
        super(CDecoratorAlwaysSuccess, self).__init__()

    
    def CreateTask(self):
        return CDecoratorAlwaysSuccessTask()



class CDecoratorAlwaysSuccessTask(behaviortreetask.CDecoratorTask):
    
    def __init__(self):
        super(CDecoratorAlwaysSuccessTask, self).__init__()

    
    def Decorate(self, iStatus):
        return defines.BT_SUCCESS


