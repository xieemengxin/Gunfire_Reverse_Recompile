# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/commonative/p1922.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/commonative/p1922.pyc
# Source Generated with Decompyle++
# File: p1922.pyc (Python 3.6)

from cl_commondefines import PARAM_LEVEL_MEDIUM_HIGH, MONSTERAI_TYPE_DEFAULT, MONSTERAI_TYPE_HATESEARCH, SIDE_TYPE_MONSTER
from cl_only import SendAlert, PY_FLAG_DEAD
from cl_resmgr.aitempparam import GetAIConfParam
import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon

def Action(skill):
    pass


def Halt(skill):
    pass


def End(skill):
    pass

from cl_perform.commonative import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1922
    m_Name = '#NT#方尖碑召唤特效'
    m_ExtPerform = ()
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_ElementType = DAM_TYPE_NORMAL
    m_BaseAttrData = {
        'ColdTime': 0,
        'AttDistance': 0,
        'ChargeTime': 0 }
    m_ClientNeed = 0
    m_UseCurWeapon = 0
    m_ForbidRule = 0


def CreateMonster(oSkill, *args):
    oGame = oSkill.m_Game
    tPos = oSkill.m_Custom['vEnd']
    dInfo = oSkill.m_Custom['dInfo']
    oOwner = oGame.GetObject(oSkill.m_Base['AID'], PY_FLAG_DEAD)
    iScene = dInfo['iScene']
    iMonsterSID = dInfo['iMonsterSID']
    tFace = dInfo['tFace']
    vFixDropPos = dInfo['vFixDropPos']
    dCheckDropInfo = dInfo['dCheckDropInfo']
    tMonsterSuper = dInfo['tMonsterSuper']
    tLineIdx = dInfo['tLineIdx']
    oDeviceElement = oGame.m_WarMgr.GetComponent('DeviceElement')
    oDeviceElement.m_DeviceChallengeMgr.DecreaseCreatingCount(tLineIdx)
    dAI = {
        'AIParamLv': PARAM_LEVEL_MEDIUM_HIGH,
        'AIMethod': MONSTERAI_TYPE_DEFAULT }
    dHateSearchAI = GetAIConfParam(MONSTERAI_TYPE_HATESEARCH, PARAM_LEVEL_MEDIUM_HIGH)
    dAI.update(dHateSearchAI)
    oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
    oLevelNode = oLevelCtrl.GetLevelNode(tLineIdx[0])
    dExtInfo = {
        'SummonStela': 1 }
    oMonster = oGame.m_ResMgr.CreateMonster(iScene, iMonsterSID, tPos, tFace, SIDE_TYPE_MONSTER, 0, dAI, tLineIdx, dExtInfo)
    if not oMonster:
        iWarNo = oGame.GetWarMgr().m_SID
        SendAlert('err', '战场%d 地图%d 关卡%d 未配置怪物SID%d' % (iWarNo, oLevelNode.m_Map, oLevelNode.m_Level, iMonsterSID))
    else:
        oMonster.Set('FixDropPos', vFixDropPos)
        oMonster.Set('CheckDropInfo', dCheckDropInfo)
        (iSuperLevel, iPlusPF, iAfPF) = tMonsterSuper
        if iSuperLevel != 0:
            oMonster.MonsterSuper(iSuperLevel, iPlusPF, iAfPF)
        if oOwner:
            oOwner.m_CreateMonsterSet.add(oMonster.m_ID)

