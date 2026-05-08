# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_anima/mobject.pyc
# RelativePath: clientlogic/cl_anima/mobject.pyc
# Source Generated with Decompyle++
# File: mobject.pyc (Python 3.6)

from cl_commondefines import MODULE_STATE_UP, MODULE_STATE_DOWN, MODULE_STATE_LEFT, MODUEL_STATE_RIGHT, GetModuleShapeData
from cl_only import SendAlert

class CModuleData(object):
    m_SID = 0
    m_Name = '灵气模块'
    m_LimitHero = 0
    m_MaxLevel = 1
    m_Shape = 1
    m_LevelInfo = {
        1: {
            'CashCost': 1,
            'WarReward': [] } }
    
    def GetPlaceholderData(cls, iStatu):
        dShapeData = GetModuleShapeData(cls.m_Shape)
        if not dShapeData:
            SendAlert('anima', 'shape %s invalid' % cls.m_SID)
            return ()
        tPlaceholderInfo = dShapeData['PlaceholderInfo']
        if iStatu not in (MODULE_STATE_UP, MODULE_STATE_DOWN, MODULE_STATE_LEFT, MODUEL_STATE_RIGHT):
            SendAlert('anima', '%s-%s invalid' % (cls.m_SID, iStatu))
            return ()
        if iStatu == MODULE_STATE_UP:
            return tPlaceholderInfo
        if iStatu == MODULE_STATE_DOWN:
            return tuple(((-iX, -iY) for iX, iY in tPlaceholderInfo))
        if iStatu == MODULE_STATE_LEFT:
            return tuple(((-iY, iX) for iX, iY in tPlaceholderInfo))
        return tuple(((iY, -iX) for iX, iY in tPlaceholderInfo))

    GetPlaceholderData = classmethod(GetPlaceholderData)


class CKnapsackData(object):
    m_SID = 0
    m_Name = '灵气背包'
    m_CashCost = 1
    m_Shape = 1

