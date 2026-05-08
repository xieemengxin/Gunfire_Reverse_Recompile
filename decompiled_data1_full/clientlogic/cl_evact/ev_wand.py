# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_evact/ev_wand.pyc
# RelativePath: clientlogic/cl_evact/ev_wand.pyc
# Source Generated with Decompyle++
# File: ev_wand.pyc (Python 3.6)

from cl_commondefines import WAND_COMP_TYPE_ACTION
from cl_wand import GetWandCompCls
import cl_formula

def WandCompCBAddArgValue(oOwner, oEventCB, sArg, iVal):
    oWandComp = oEventCB.GetObject()
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iVal = cl_formula.GetResultByData(oOwner, iVal, dEventInfo, dMsgInfo)
    oWandComp.AddArgValue(sArg, iVal)


def WandConditionCompCBAddCount(oOwner, oEventCB, iCount):
    oWandComp = oEventCB.GetObject()
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iCount = cl_formula.GetResultByData(oOwner, iCount, dEventInfo, dMsgInfo)
    oWandComp.AddConditionCount(iCount)


def WandConditionCompCBSetCount(oOwner, oEventCB, iCount):
    oWandComp = oEventCB.GetObject()
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iCount = cl_formula.GetResultByData(oOwner, iCount, dEventInfo, dMsgInfo)
    oWandComp.SetConditionCount(iCount)

