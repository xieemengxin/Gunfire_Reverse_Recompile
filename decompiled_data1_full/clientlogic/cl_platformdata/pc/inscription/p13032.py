# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/inscription/p13032.pyc
# RelativePath: clientlogic/cl_platformdata/pc/inscription/p13032.pyc
# Source Generated with Decompyle++
# File: p13032.pyc (Python 3.6)

from cl_msgcenter.defines import MSG_WAR_TRIGGER_EXTERNALDRIVE
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, INSCRIPTION_TYPE_EXCLUSIVE, ITEMPERFORM_ENABLE_HOLD

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckFromSameItem(oWarrior, oEventCB):
        CustomAction(oWarrior, oEventCB, {
            'Ratio': 100 })


class CPerform(CCustomPerform):
    m_SID = 13032
    m_Name = '青鸾'
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
    m_ItemAttr = { }
    m_InscriptionType = INSCRIPTION_TYPE_EXCLUSIVE
    m_ElementType = None
    m_LimitList = ((), (1304,), ())
    m_ExcludeList = ((), (), ())
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD


def CustomAction(oWarrior, oEventCB, dInfo):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'CurVID' in dMsgInfo:
        iVictim = dMsgInfo['CurVID']
    elif 'VID' in dMsgInfo:
        iVictim = dMsgInfo['VID']
    else:
        iVictim = 0
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    dSkillCollect = oSkill.m_Collect
    iNowVictim = dSkillCollect.get('pf13032-VID', 0)
    if iNowVictim and iNowVictim != iVictim:
        return None
    iRatio = dInfo.get('Ratio', 100)
    if 'pf13032' not in dSkillCollect:
        cl_msgcenter.SendMsg(MSG_WAR_TRIGGER_EXTERNALDRIVE, oWarrior, {
            'iVictim': iVictim })
        dSkillCollect['pf13032'] = 1
        cl_evact.PassiveCBUsePerformWithMonsterCenter(oWarrior, oEventCB, 1699, (0, 0, 0), iRatio)
        dSkillCollect['pf1699'] = oWarrior.Query('pf1699')
        dSkillCollect['pf13032-VID'] = iVictim
        oWarrior.Delete('pf1699')
    else:
        iActNum = dSkillCollect.get('pf1699', 0)
        oSkill1699 = oWarrior.m_Game.m_SkillMgr.GetSkill(oWarrior.m_ID, iActNum)
        if oSkill1699 and 'PredictChange' in dMsgInfo and 'TransmitAtt' in oSkill1699.m_Custom:
            oSkill1699.m_Custom['TransmitAtt'] += sum(dMsgInfo['PredictChange']) * iRatio // 100

