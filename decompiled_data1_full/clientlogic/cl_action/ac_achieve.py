# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_action/ac_achieve.pyc
# RelativePath: clientlogic/cl_action/ac_achieve.pyc
# Source Generated with Decompyle++
# File: ac_achieve.pyc (Python 3.6)

from cl_only import Functor
import cl_msgcenter

def AchieveTeamEventCBFunc(oEventCB, iGroup, dEvent, oListener, oTarget, dMsgInfo):
    oEventCB.CBFuncAction(oListener, iGroup, dEvent, dMsgInfo)


def AchieveListenTeamMsgCallBack(oTarget, oLifeCycle, iMsg, iSub, iGroup):
    
    def ClearEvent(oOwner, oLifeCycle):
        for iHero in lstHero:
            cl_msgcenter.DoneAttention(oTarget, iHero, iMsg, sKey, iSub)
        

    if not oLifeCycle.GetObject():
        return None
    oGame = oTarget.m_Game
    lstHero = oGame.m_WarMgr.GetAllHero()
    for iHero in lstHero:
        oHero = oGame.GetObject(iHero)
        if not oHero:
            continue
        dEvent = oLifeCycle.AttrCache()
        dEvent['LifeCycle'] = oLifeCycle
        sKey = oLifeCycle.Key()
        func = Functor(AchieveTeamEventCBFunc, oLifeCycle.GetObject().m_EventCB, iGroup, dEvent)
        cl_msgcenter.AddAttentionFunc(oTarget, iHero, iMsg, func, sKey, iSub)
        oLifeCycle.AddDisableFunc(ClearEvent)
    


def AchieveEventCBFunc(oEventCB, iGroup, dEvent, oListener, oTarget, dMsgInfo):
    oEventCB.CBFuncAction(oListener, iGroup, dEvent, dMsgInfo)


def AchieveListenWarMgrMsgCallBack(oTarget, oLifeCycle, iMsg, iSub, iGroup):
    
    def ClearEvent(oOwner, oLifeCycle):
        cl_msgcenter.DoneAttention(oOwner, iWarMgr, iMsg, sKey, iSub)

    iWarMgr = oTarget.m_Game.m_WarMgr.m_ID
    sKey = oLifeCycle.Key()
    dEvent = oLifeCycle.AttrCache()
    dEvent['LifeCycle'] = oLifeCycle
    func = Functor(AchieveEventCBFunc, oLifeCycle.GetObject().m_EventCB, iGroup, dEvent)
    cl_msgcenter.AddAttentionFunc(oTarget, iWarMgr, iMsg, func, sKey, iSub)
    oLifeCycle.AddDisableFunc(ClearEvent)


def AchieveListenGlobalMsgCallBack(oTarget, oLifeCycle, iMsg, iSub, iGroup):
    
    def ClearEvent(oOwner, oLifeCycle):
        oOwner.m_Game.DoneGlobalAttention(iTarget, iMsg, sKey, iSub)

    iTarget = oTarget.m_ID
    sKey = oLifeCycle.Key()
    dEvent = oLifeCycle.AttrCache()
    dEvent['LifeCycle'] = oLifeCycle
    func = Functor(AchieveEventCBFunc, oLifeCycle.GetObject().m_EventCB, iGroup, dEvent)
    oTarget.m_Game.AddGlobalAttention(iTarget, iMsg, func, sKey, iSub)
    oLifeCycle.AddDisableFunc(ClearEvent)

