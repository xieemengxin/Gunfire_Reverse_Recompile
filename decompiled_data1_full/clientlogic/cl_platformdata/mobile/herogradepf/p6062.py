# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/herogradepf/p6062.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/herogradepf/p6062.pyc
# Source Generated with Decompyle++
# File: p6062.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_item
import cl_reward
from cl_commondefines import DAM_TYPE_FIRE, LEVEL_TYPE_BOSS, NWARRIOR_DROP_EQUIP, DAM_TYPE_CORRISION, DAM_TYPE_THUNDER
from cl_item.defines import EQUIP_TYPE_FUNDAMENTALWEAPON
from cl_cscommondef.cs_itemdef import ITEM_SOURCE_TALENT
from . import CHeroGradePassive as CCustomPerform
from cl_commondefines import PF_SUBMSG_CAREERPF, PF_SUBMSG_THROW

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'ShieldMax', 0, 2000, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_THROW, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32780, 600, { }, -1, -1, None)


class CPerform(CCustomPerform):
    m_SID = 6062
    m_Name = '千岁lv.2'
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
    dValid = oWarrior.Query('Illus')['Weapon']
    lstAllWeapon = []
    for iWeapon in dValid:
        oWeapon = cl_item.GetItemCls(iWeapon)
        if dInfo['ElementTag'] in oWeapon.m_ClassifyTag and oWeapon.m_ElementType != DAM_TYPE_FIRE:
            continue
        if oWeapon.m_Type == EQUIP_TYPE_FUNDAMENTALWEAPON:
            continue
        lstAllWeapon.append(iWeapon)
    
    iWeapon = oGame.m_RandomMgr.ChooseKey('weapon%d' % oWarrior.m_ID, {
        'Select': lstAllWeapon })
    if not iWeapon:
        return None
    iGrade = cl_reward.GetWeaponRewardGrade(oGame)
    iNewInscriptionNum = 0
    oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
    oLevelNode = oLevelCtrl.m_CurNode
    if oLevelNode.m_LevelType == LEVEL_TYPE_BOSS:
        oWarData = oGame.m_WarData
        iLayer = oLevelCtrl.m_LayerNum + 1
        iGrade = oWarData.GetWeaponGrade(iLayer, 1, oGame)
        iNewInscriptionNum = oWarData.GetInscriptionNum(iLayer, 1, oLevelCtrl)
    oWeapon = cl_item.CreateEquip(oGame, iWeapon, iGrade, oOwner = oGame.GetObject(oWarrior.m_ID), iSource = ITEM_SOURCE_TALENT)
    oInscriptionCom = oWeapon.GetComponent('Inscription')
    if iNewInscriptionNum:
        oInscriptionCom.m_InscriptionNum = iNewInscriptionNum
    if oWeapon.m_ElementType != DAM_TYPE_FIRE:
        oInscriptionCom.CleanInscription()
        oInscriptionCom.AppendInscription(dInfo['FireInscription'])
    if oInscriptionCom.m_InscriptionNum > len(oInscriptionCom.m_Inscription):
        oInscriptionCom.AddInscription()
    oResMgr = oGame.GetResMgr()
    dFlyInfo = {
        'Abandoner': oWarrior.m_ID }
    lstDropData = [
        oWeapon]
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_DROPWEAPON, oWarrior, {
        'lstWeapon': lstDropData })
    oResMgr.CreateDrop(oWarrior.m_Scene, NWARRIOR_DROP_EQUIP, oWarrior.GetPos(), lstDropData, dFlyInfo, {
        'DropSource': oWarrior.m_PlayerID }, oWarrior.m_ID)

