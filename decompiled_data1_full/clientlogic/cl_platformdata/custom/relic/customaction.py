# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/custom/relic/customaction.pyc
# RelativePath: clientlogic/cl_platformdata/custom/relic/customaction.pyc
# Source Generated with Decompyle++
# File: customaction.pyc (Python 3.6)

from cl_only import ShufferList, Functor
from cl_evact import GetCommonEventKey
from cl_object.logging import WartalentLog
from cl_commondefines import VIRTUAL_ITEM_TALENT, VIRTUAL_ITEM_RELIC, VIRTUAL_ITEM_GOLDENCUP, RELIC_SUBMSG_GENERATE_GOOD, NWARRIOR_NPC_SHOP
from cl_commondefines import PLAYMODE_SURVIVOR
from cl_object.logging import WarobjLog
import cl_condition
import cl_reward
import cl_action
import cl_perform
import cl_msgcenter
import cl_shop

def CustomAction5860(oWarrior, oEventCB, dArgs):
    iCurCash = oWarrior.Cash()
    iFinalCash = 0
    if 'Enhance' in dArgs:
        for _ in range(2):
            iTempCash = GenerateFunc(oWarrior, 4, iCurCash, dArgs)
            if iTempCash > iFinalCash:
                iFinalCash = iTempCash
        
    else:
        iFinalCash = GenerateFunc(oWarrior, 4, iCurCash, dArgs)
    if iFinalCash:
        oWarrior.AddCash(iFinalCash - iCurCash, '5860RelicAdd')


def GenerateFunc(oWarrior, iRange, iCurCash, dArgs):
    sRangeString = str(iCurCash)[-iRange:]
    if iCurCash < 10 ** iRange:
        return ShuffleFunc(oWarrior, sRangeString, dArgs)
    return (iCurCash - int(sRangeString)) + ShuffleFunc(oWarrior, sRangeString, dArgs)


def ShuffleFunc(oWarrior, sTarget, dArgs):
    lstTarget = list(sTarget)
    iExChange = dArgs['Exchange']
    if 'Enhance' not in dArgs:
        iIndex = lstTarget.index(max(lstTarget))
        lstTarget[iIndex] = str(iExChange)
    else:
        iIndex = lstTarget.index(min(lstTarget))
        lstTarget[iIndex] = str(iExChange)
    return int(''.join(ShufferList(oWarrior.m_Game, lstTarget)))


def CustomAction5879(oWarrior, oLifeCycle, dInfo):
    
    def ClearFunc(bClearWeight, oWarrior, oLifeCycle):
        if bClearWeight:
            dWeight = oWarrior.Query('AddtionalGoodsWeight', { })
            dWeight.pop(VIRTUAL_ITEM_RELIC, 0)
        oWarrior.Delete('ForceRelicGoodsPos')
        oWarrior.Delete('CanReplaceRelicGoodsNum')

    dWeight = oWarrior.SetDefault('AddtionalGoodsWeight', { })
    if VIRTUAL_ITEM_RELIC in dWeight:
        bClearWeight = False
    else:
        bClearWeight = True
        dWeight[VIRTUAL_ITEM_RELIC] = 100
    if oWarrior.m_Game.m_WarMgr.m_PlayMode == PLAYMODE_SURVIVOR:
        lstReplacePos = [
            5,
            8]
    else:
        for iHidden, lstPos in {
            8: [
                7,
                8],
            7: [
                5,
                7] }.items():
            if iHidden in oWarrior.m_BuyMgr.m_ShowHidden:
                lstReplacePos = lstPos
                break
        else:
            lstReplacePos = [
                4,
                5]
    oWarrior.Set('ForceRelicGoodsPos', lstReplacePos)
    oWarrior.Set('CanReplaceRelicGoodsNum', dInfo['CanReplaceNum'])
    oLifeCycle.AddDisableFunc(Functor(ClearFunc, bClearWeight))

