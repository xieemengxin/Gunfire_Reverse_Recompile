# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_action/ac_suit.pyc
# RelativePath: clientlogic/cl_action/ac_suit.pyc
# Source Generated with Decompyle++
# File: ac_suit.pyc (Python 3.6)

from cl_platformdata import GetSeasonSuitCls
from cl_commondefines import RELIC_LIFECYCLE_FORCE

def RewardPassive(oTarget, iPerform, iLevel = 1):
    oPerform = oTarget.AddPerform(iPerform, iLevel)
    if oPerform:
        dSaveCD = oTarget.Query('SaveLiteCD', { })
        if iPerform in dSaveCD:
            oPerform.LoadLiteCD(dSaveCD.pop(iPerform))


def RemovePassive(oTarget, iPerform):
    oPerformCon = oTarget.m_Perform
    oPerform = oPerformCon.GetPerform(iPerform)
    if oPerform:
        if oPerform.CheckLiteCD():
            dSaveCD = oTarget.SetDefault('SaveLiteCD', { })
            dSaveCD[iPerform] = oPerform.m_LiteCD
        oPerformCon.RemovePerform(oTarget, iPerform)


def ReplaceCoreRelic(oTarget, iSuit, iReplaceSID):
    clsSuit = GetSeasonSuitCls(iSuit)
    if not clsSuit:
        return None
    iCoreRelic = clsSuit.m_CoreRelic
    if not iCoreRelic:
        return None
    oRelic = oTarget.m_RelicCon.GetPerform(iCoreRelic)
    if not oRelic:
        return None
    if iReplaceSID not in clsSuit.m_CoreRelicAction:
        return None
    dCoreRelicAction = clsSuit.m_CoreRelicAction[iReplaceSID]
    enableFunc = dCoreRelicAction['Enable']
    disableFunc = dCoreRelicAction['Disable']
    cdFunc = dCoreRelicAction['CDAction']
    cbFunc = clsSuit.m_CoreRelicCBFuncAction
    dInfo = {
        'enableFunc': enableFunc,
        'disableFunc': disableFunc,
        'cdFunc': cdFunc,
        'cbFunc': cbFunc }
    oRelic.SetOtherLifeCycle(oTarget, RELIC_LIFECYCLE_FORCE, dInfo)


def RemoveCoreRelic(oTarget, iSuit):
    clsSuit = GetSeasonSuitCls(iSuit)
    if not clsSuit:
        return None
    iCoreRelic = clsSuit.m_CoreRelic
    if not iCoreRelic:
        return None
    oRelic = oTarget.m_RelicCon.GetPerform(iCoreRelic)
    if not oRelic:
        return None
    oRelic.RemoveOtherLifeCycle(oTarget, RELIC_LIFECYCLE_FORCE)

