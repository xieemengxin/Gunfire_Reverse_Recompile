# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/benediction/p13735.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/benediction/p13735.pyc
# Source Generated with Decompyle++
# File: p13735.pyc (Python 3.6)

from cl_platformdata.custom.benediction.customaction import CustomAction13735 as CustomAction
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_commondefines import PICK_S7CRYSTAL, S7SHOP_ADD_CRYSTALGOODS
from cl_newformula import Func651

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S7CRYSTALSHOPINIT, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PICK, PICK_S7CRYSTAL, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S7SHOP, S7SHOP_ADD_CRYSTALGOODS, 3, 0, 0)
    CustomAction(oWarrior, oLifeCycle, {
        'Key': 'PF-13735',
        'TotalPoint': 1,
        'MaxPoint': 5 })


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBAddS7CrystalExtPoint(oWarrior, oEventCB, 'PF-13735', 1, 0, 5)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBAddS7CrystalShopExtPoint(oWarrior, oEventCB, 'PF-13735', 1, 5)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventCBReEnableS7CrystalExtPointEffect(oWarrior, oEventCB, 'PF-13735')


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventCBAddMessageInfo(oWarrior, oEventCB, 'MaxPoint', (lambda *a: Func651(*a, **{
'sKey': 'MaxPoint' }) + 1))


class CPerform(CCustomPerform):
    m_SID = 13735
    m_Name = '符能奔涌'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Career = None

