# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/custom/seasonsuit/customaction.pyc
# RelativePath: clientlogic/cl_platformdata/custom/seasonsuit/customaction.pyc
# Source Generated with Decompyle++
# File: customaction.pyc (Python 3.6)

from cl_commondefines import STATE_TIME_FOREVER
from cl_only import ShufferList, SendAlert
import cl_war
import cl_formula
import cl_state
import cl_object

def Customaction1947(oWarrior, oEventCB, dInfo):
    iChooseMonsterNum = dInfo['ChooseMonsterNum'] if 'ChooseMonsterNum' in dInfo else 0
    if not iChooseMonsterNum:
        return None
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标-Customaction1947' % oEventCB.m_Key)
        return None
    oPerform = oWarrior.GetPerform(dInfo['PerformID'])
    if not oPerform:
        return None
    oScene = oWarrior.m_Game.m_SceneMgr.GetScene(oWarrior.m_Scene)
    if not oScene:
        SendAlert('err', '%s-Scene Error-Customaction1947' % oEventCB.m_Key)
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    dInfo = cl_formula.CalArgsFormula(oWarrior, dInfo, dEventInfo, dMsgInfo)
    iVictim = dMsgInfo['VID'] if 'VID' in dMsgInfo else 0
    dMonster = oScene.m_SceneData.GetFightMonster()
    if not dMonster:
        return None
    lstMonster = list(dMonster.keys())
    if iVictim in lstMonster:
        lstMonster.remove(iVictim)
    lstTarget = dTransInfo['TargetList']
    lstMonster = list(filter((lambda x: x not in lstTarget), lstMonster))
    if not lstMonster:
        return None
    lstMonster = ShufferList(oWarrior.m_Game, lstMonster)[:iChooseMonsterNum]
    dData = {
        'vStart': oWarrior.GetCenter(),
        'Custom': {
            'VID': iVictim,
            'SourceVID': iVictim,
            'LockTarget': lstMonster,
            'ElementExceptionSID': dInfo['ElementExceptionSID'] if 'ElementExceptionSID' in dInfo else 0 } }
    cl_war.UsePerform(oWarrior, oPerform, dData)


def CustomAction15122(oWarrior, oEventCB, dInfo):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    dEventInfo = oEventCB.GetCBEventInfo()
    iPerform = dEventInfo['pfid']
    iHeroID = oWarrior.m_ID
    oReason = cl_object.reason.CPerformReason(iPerform, iHeroID, oWarrior.m_SID, oWarrior.m_FightType, None, { })
    iCount = cl_formula.GetResultByData(oWarrior, dInfo['Count'], dEventInfo, dMsgInfo, dEventInfo)
    dCartoon = oSkill.GetCurCartoon()
    dRet = {
        'TargetPos': dCartoon['Start'],
        'Count': iCount,
        'Perform': dInfo['Perform'] }
    dArgs = {
        'AID': iHeroID,
        'RS': oReason,
        'pfid': iPerform,
        'PFLV': dEventInfo['PFLV'],
        'arg': dRet }
    oState = cl_state.AddState(oWarrior, dInfo['StateSID'], STATE_TIME_FOREVER, 0, dArgs)
    if not oState:
        return None
    oState.Enable(oWarrior)

