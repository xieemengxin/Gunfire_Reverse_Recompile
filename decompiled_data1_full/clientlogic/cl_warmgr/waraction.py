# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/waraction.pyc
# RelativePath: clientlogic/cl_warmgr/waraction.pyc
# Source Generated with Decompyle++
# File: waraction.pyc (Python 3.6)

from cl_only import Functor, Time2Frame
import cl_msgcenter

def NextTimeStep(oWarMgr, iStepIdx, iNextTime):
    oWarMgr.AddStep(iStepIdx, Time2Frame(iNextTime) + oWarMgr.m_Game.GetFrameNum())


def SureTimeStep(oWarMgr, iStepIdx, iSureTime):
    oWarMgr.AddStep(iStepIdx, Time2Frame(iSureTime))


def AddFunction(oWarMgr, iStepIdx, iMsg, iSub):
    cl_msgcenter.AddFunction(oWarMgr, iMsg, Functor(DoCallBackAction, iStepIdx), 'WarMgrAct%d' % iStepIdx, iSub)


def DoCallBackAction(iStepIdx, oWarMgr, dInfo):
    oWarMgr.DoStep(iStepIdx)


def DoneEvent(oWarMgr, iStepIdx, iMsg, iSub):
    cl_msgcenter.DoneEvent(oWarMgr, iMsg, 'WarMgrAct%d' % iStepIdx, iSub)

