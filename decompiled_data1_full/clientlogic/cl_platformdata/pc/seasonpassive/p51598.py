# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51598.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51598.pyc
# Source Generated with Decompyle++
# File: p51598.pyc (Python 3.6)

from cl_commondefines import BASEATTR_REFRESH, BASEATTR_CLIENT
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_modeldata
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import OBJ_SELF, WARRIOR_SUMMON_AIRFOLLOWEFFECT
from cl_newformula import Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'PF1992DamMul', 8000)
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'PF1992Interval', 0)
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'PF1992Interval', 60)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MoveSpeedAdd', 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ScaleAdd', 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CREATESUMMON, -1, 1, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'PF1992DamMul', 12000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MoveSpeedAdd', 500)
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'PF1992Interval', -20)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ScaleAdd', 25)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CREATESUMMON, -1, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'PF1992DamMul', 16000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MoveSpeedAdd', 1000)
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'PF1992Interval', -30)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ScaleAdd', 50)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CREATESUMMON, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventGetTargetBySummonType(oWarrior, oEventCB, WARRIOR_SUMMON_AIRFOLLOWEFFECT)
    cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 2)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByMsgInfoSummon(oWarrior, oEventCB)
    if cl_evcon.CheckTargetIsSelfSummon(oWarrior, oEventCB, WARRIOR_SUMMON_AIRFOLLOWEFFECT):
        cl_evact.EventChangeTargetAttr(oWarrior, oEventCB, 'MoveSpeed', (lambda *a: Func717(*a, **{
'sArg': 'MoveSpeedAdd' })), 0, 0)
        CustomAction(oWarrior, oEventCB, {
            'FogID': cl_evact.EventGetTargeID(oWarrior, oEventCB),
            'ScaleAdd': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'ScaleAdd') })


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventChangeTargetAttr(oWarrior, oEventCB, 'MoveSpeed', (lambda *a: Func717(*a, **{
'sArg': 'MoveSpeedAdd' })), 0, 0)
    CustomAction(oWarrior, oEventCB, {
        'FogID': cl_evact.EventGetTargeID(oWarrior, oEventCB),
        'ScaleAdd': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'ScaleAdd') })


class CPerform(CCustomPerform):
    m_SID = 51598
    m_Name = '#NT#毒雾伤害'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0


def CustomAction(oHero, oEventCB, dInfo):
    
    def ClearFunc(oWarrior, oLifeCycle):
        dSummon = oWarrior.Query(sKey, { })
        if not dSummon:
            return None
        oGame = oWarrior.m_Game
        for iSummon in dSummon:
            oSummon = oGame.GetObject(iSummon)
            if not oSummon:
                continue
            oSummon.ClearScaleFactor(sKey)
            iScale = oSummon.GetCurScale()
            oSummon.SetAttr('Scale', iScale, BASEATTR_REFRESH | BASEATTR_CLIENT)
            fScale = iScale / 100
            oModel = oSummon.m_ModelData
            if not oModel:
                continue
            ChangeTargetModelDataWithScale(oSummon, oModel, fScale)
        

    iSummon = dInfo['FogID']
    iScaleAdd = dInfo['ScaleAdd']
    if iScaleAdd < 0:
        return None
    oSummon = oHero.m_Game.GetObject(iSummon)
    if not oSummon:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    sKey = 'ExpandFog-%s' % oEventCB.m_Key
    oSummon.SetScaleFactor(sKey, iScaleAdd)
    iScale = oSummon.GetCurScale()
    oSummon.SetAttr('Scale', iScale, BASEATTR_REFRESH | BASEATTR_CLIENT)
    oModel = oSummon.m_ModelData
    if not oModel:
        return None
    fScale = iScale / 100
    ChangeTargetModelDataWithScale(oSummon, oModel, fScale)
    dSummon = oHero.SetDefault(sKey, { })
    dSummon[oSummon.m_ID] = 1
    sUniqueKey = 'PF51598-ExpandFog-%s' % oSummon.m_SID
    oLifeCycle.AddUniqueDisableFunc(sUniqueKey, ClearFunc, iCover = 0)


def ChangeTargetModelDataWithScale(oSummon, oModel, fScale):
    dParam = {
        'Shape': oModel.m_ModelShape,
        'Angle': oModel.m_ModelAngle,
        'Center': oModel.m_ModelCenter,
        'Scale': (fScale, fScale, fScale),
        'Size': oModel.m_ModelSize }
    oSummon.m_ModelData = cl_modeldata.GetModel(dParam)

