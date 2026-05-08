# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_condition/con_suit.pyc
# RelativePath: clientlogic/cl_condition/con_suit.pyc
# Source Generated with Decompyle++
# File: con_suit.pyc (Python 3.6)


def HasCondition(oSuitElement, iTarget, iSuit, iCondition):
    return oSuitElement.m_CurSituate[iTarget][iSuit].get(iCondition, 0)


def HasNumConditionInConditionList(oSuitElement, iTarget, iSuit, iNum, lstCondition):
    iRes = 0
    for iCondition in lstCondition:
        if oSuitElement.m_CurSituate[iTarget][iSuit].get(iCondition, 0):
            iRes += 1
    
    return iRes + oSuitElement.GetConditionReduceNum(iTarget, iSuit) >= iNum

