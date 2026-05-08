# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_behavior/nodes/decorators/decoratoralwaysrunning.pyc
# RelativePath: clientlogic/cl_behavior/nodes/decorators/decoratoralwaysrunning.pyc
# Source Generated with Decompyle++
# File: decoratoralwaysrunning.pyc (Python 3.6)

from __future__ import absolute_import
from ... import defines
from ... import behaviortree
from ... import behaviortreetask

class CDecoratorAlwaysRunning(behaviortree.CDecoratorNode):
    CLASS_NAME = 'DecoratorAlwaysRunning'
    
    def __init__(self):
        super(CDecoratorAlwaysRunning, self).__init__()

    
    def CreateTask(self):
        return CDecoratorAlwaysRunningTask()



class CDecoratorAlwaysRunningTask(behaviortreetask.CDecoratorTask):
    
    def __init__(self):
        super(CDecoratorAlwaysRunningTask, self).__init__()

    
    def Decorate(self, iStatus):
        return defines.BT_RUNNING


