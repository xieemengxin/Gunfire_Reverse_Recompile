# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/pc/s1203.pyc
# RelativePath: clientlogic/cl_achievement/pc/s1203.pyc
# Source Generated with Decompyle++
# File: s1203.pyc (Python 3.6)

from cl_commondefines import PF_SUBMSG_CAREERPF
from cl_newformula import Func305, Func540
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CAchieveStat as CCustom

def EnableAction(oListener, oLifeCycle):
    if cl_condition.CheckHero(oListener, oLifeCycle, 215):
        cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF, 0, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_evcon.GetFormula(oListener, oEventCB, (lambda *a: Func540(*a))) >= cl_evcon.GetFormula(oListener, oEventCB, (lambda *a: Func305(*a, **{
'sAttr': 'EnergyMax' }))):
        cl_evact.AchieveCBAddStat(oListener, oEventCB, 1)


class CAchieveStat(CCustom):
    m_SID = 1203
    m_Name = '不遗余力'
    m_TargetValue = 200
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0 }

