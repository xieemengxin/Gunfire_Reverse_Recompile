# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5703.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5703.pyc
# Source Generated with Decompyle++
# File: p5703.pyc (Python 3.6)

from cl_object import baseattr
import cl_object.reason
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import QUALITY_TYPE_NORMAL, RELIC_TYPE_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonForceSetAttr(oWarrior, oLifeCycle, 'HPMax', 100)
    cl_action.CommonChageMulAttr(oWarrior, oLifeCycle, 'ArmorMax', 10000)
    cl_action.CommonChageMulAttr(oWarrior, oLifeCycle, 'ShieldMax', 10000)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChageMulAttr(oWarrior, oLifeCycle, 'ArmorMax', 10000)
    cl_action.CommonChageMulAttr(oWarrior, oLifeCycle, 'ShieldMax', 10000)


class CPerform(CCustomPerform):
    m_SID = 5703
    m_Name = '异能之躯'
    m_MaxLevel = 2
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5524
    m_ValidRemove = 1
    m_BasePrice = 100
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_NORMAL
    
    def Enable(self, oWarrior, iNotify = 0):
        iCurrentHp = oWarrior.HP()
        oWarrior.Set('CacheHP', iCurrentHp)
        CCustomPerform.Enable(self, oWarrior, iNotify)

    
    def Disable(self, oWarrior, iNotify = 1, iReleaseFlag = 0):
        CCustomPerform.Disable(self, oWarrior, iNotify, iReleaseFlag)
        iCacheHP = oWarrior.Query('CacheHP', 0)
        if iCacheHP:
            iCurrentHP = oWarrior.HP()
            iChangeHP = iCacheHP - iCurrentHP
            oReason = cl_object.reason.CStrReason('恢复缓存属性')
            oWarrior.HPDirectModify('HP', oWarrior.m_ID, iChangeHP, oReason)


