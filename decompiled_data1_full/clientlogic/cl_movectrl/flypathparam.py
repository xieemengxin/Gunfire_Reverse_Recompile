# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_movectrl/flypathparam.pyc
# RelativePath: clientlogic/cl_movectrl/flypathparam.pyc
# Source Generated with Decompyle++
# File: flypathparam.pyc (Python 3.6)

from cl_commondefines.cd_fight import CROWDMODE_NORMAL, PATHMODE_GHOST, CROWDMODE_GHOST

class CCrowdPathParam:
    m_ObstacleAvoidance = 0
    m_Separation = 0
    m_SeparationWeight = 3
    m_Collision = 1
    m_CrowdMode = CROWDMODE_NORMAL
    
    def GetCrowdParam(cls):
        dParam = {
            'mode': cls.m_CrowdMode,
            'rvo': cls.m_ObstacleAvoidance,
            'sep': cls.m_Separation,
            'sepweight': cls.m_SeparationWeight,
            'col': cls.m_Collision }
        return dParam

    GetCrowdParam = classmethod(GetCrowdParam)


class CGhostlParam(CCrowdPathParam):
    m_CrowdMode = CROWDMODE_GHOST

g_PathModeParamMap = {
    PATHMODE_GHOST: CGhostlParam }

def GetCrowdPathModeParam(iPathMode):
    if iPathMode in g_PathModeParamMap:
        clsParam = g_PathModeParamMap[iPathMode]
        return clsParam.GetCrowdParam()
    return CCrowdPathParam.GetCrowdParam()

