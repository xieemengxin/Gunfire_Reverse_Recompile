# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_movectrl/crowdpathparam.pyc
# RelativePath: clientlogic/cl_movectrl/crowdpathparam.pyc
# Source Generated with Decompyle++
# File: crowdpathparam.pyc (Python 3.6)

from cl_commondefines.cd_fight import CROWDMODE_NORMAL, PATHMODE_POWERPUSH, PATHMODE_STAYSTATUS, PATHMODE_COLLISIONLESS, PATHMODE_CROWDPUSH, PATHMODE_GHOST, CROWDMODE_GHOST, PATHMODE_CROWDWINK
import cllib.lib_flag as lib_flag

class CCrowdPathParam(object):
    m_AnticipateTurns = 0
    m_OptimizeVis = 1
    m_OptimizeTopo = 0
    m_ObstacleAvoidance = 1
    if lib_flag.g_IsMobileRun:
        m_Separation = 0
    else:
        m_Separation = 1
    m_SeparationWeight = 3
    m_Nobody = 0
    m_StayStatus = 0
    m_PositiveAvoidance = 1
    m_CrowdMode = CROWDMODE_NORMAL
    
    def GetCrowdParam(cls):
        dParam = {
            'mode': cls.m_CrowdMode,
            'anti': cls.m_AnticipateTurns,
            'vis': cls.m_OptimizeVis,
            'topo': cls.m_OptimizeTopo,
            'rvo': cls.m_ObstacleAvoidance,
            'sep': cls.m_Separation,
            'sepweight': cls.m_SeparationWeight,
            'nobody': cls.m_Nobody,
            'stay': cls.m_StayStatus,
            'post': cls.m_PositiveAvoidance }
        return dParam

    GetCrowdParam = classmethod(GetCrowdParam)


class CGhostlParam(CCrowdPathParam):
    m_CrowdMode = CROWDMODE_GHOST


class CCrowdPushParam(CCrowdPathParam):
    m_ObstacleAvoidance = 0
    m_Separation = 0


class CCrowdWinkParam(CCrowdPathParam):
    m_ObstacleAvoidance = 0


class CCollisionlessParam(CCrowdPathParam):
    m_Nobody = 1
    m_ObstacleAvoidance = 0


class CStayStatusParam(CCrowdPathParam):
    m_StayStatus = 1


class CPowerPushParam(CCrowdPathParam):
    m_ObstacleAvoidance = 0
    m_StayStatus = 1

g_PathModeParamMap = {
    PATHMODE_CROWDWINK: CCrowdWinkParam,
    PATHMODE_POWERPUSH: CPowerPushParam,
    PATHMODE_STAYSTATUS: CStayStatusParam,
    PATHMODE_COLLISIONLESS: CCollisionlessParam,
    PATHMODE_CROWDPUSH: CCrowdPushParam,
    PATHMODE_GHOST: CGhostlParam }

def GetCrowdPathModeParam(iPathMode):
    if iPathMode in g_PathModeParamMap:
        clsParam = g_PathModeParamMap[iPathMode]
        dParam = clsParam.GetCrowdParam()
        return dParam
    dParam = CCrowdPathParam.GetCrowdParam()
    return dParam

