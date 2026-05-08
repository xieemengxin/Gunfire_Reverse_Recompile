# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/daytrialpf/p6771.pyc
# RelativePath: clientlogic/cl_platformdata/pc/daytrialpf/p6771.pyc
# Source Generated with Decompyle++
# File: p6771.pyc (Python 3.6)

from cl_item.defines import EQUIP_TYPE_FUNDAMENTALWEAPON
from cl_commondefines import DAM_TYPE_NORMAL
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.daytrial import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDWEAPON, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    CustomAction(oWarrior, oEventCB, {
        4832: 4832,
        4833: 4833,
        4834: 4834 })


class CPerform(CCustomPerform):
    m_SID = 6771
    m_Name = '所有非元素武器随机获得一种属性'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0


def CustomAction(oWarrior, oEventCB, dInfo):
    oGame = oWarrior.m_Game
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Weapon' not in dMsgInfo:
        return None
    oWeapon = dMsgInfo['Weapon']
    oInscriptionCom = oWeapon.GetComponent('Inscription')
    if oWeapon.m_Type == EQUIP_TYPE_FUNDAMENTALWEAPON:
        return None
    if oWeapon.m_ElementType != DAM_TYPE_NORMAL:
        return None
    oInscriptionCom = oWeapon.GetComponent('Inscription')
    if not oInscriptionCom:
        return None
    lstInscription = []
    for iInscription in dInfo.keys():
        lstInscription.append(iInscription)
    
    if len(list(set(lstInscription) & set(oInscriptionCom.m_Inscription))) > 0:
        return None
    iInscription = lstInscription[oGame.Random(len(lstInscription))]
    oInscriptionCom.AppendInscription(iInscription)
    oInscriptionCom.m_Item.GS2CItemPropChange('Inscription', oInscriptionCom.GetAllInscription())

