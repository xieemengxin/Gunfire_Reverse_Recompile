# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_behavior/debug/linkmanager.pyc
# RelativePath: clientlogic/cl_behavior/debug/linkmanager.pyc
# Source Generated with Decompyle++
# File: linkmanager.pyc (Python 3.6)

from __future__ import absolute_import
from only import GetSecond, SetGlobalManager, GetGlobalManager, Call_Out, Remove_Call_Out, GetObject
from pubbaselogin.p_defines import *
from pubbaselogin import GS2CErrorCode, GetLoginObject

class CLinkManager(object):
    m_DebugPlayer = set()
    
    def __init__(self):
        self.m_Link = { }
        self.m_DebugPlayer = set()

    
    def AddLink(self, oLink):
        pid = oLink.m_EditorPlayer
        self.RemoveOldLink(pid)
        self.m_Link[oLink.m_ID] = GetSecond()
        oLogin = GetLoginObject()
        oLinkManager = oLogin.m_LinkManager
        oLinkManager.DeleteRecordLinkObject(oLink.m_ID)
        self.m_DebugPlayer.add(pid)

    
    def RemoveOldLink(self, pid):
        lstRemove = []
        for uid in self.m_Link:
            oLink = GetObject(uid)
            if oLink and oLink.m_EditorPlayer == pid:
                lstRemove.append(uid)
        
        for uid in lstRemove:
            self.RemoveLink(uid)
        

    
    def RemoveLink(self, uid):
        if uid in self.m_Link:
            self.m_Link.pop(uid)
            oLink = GetObject(uid)
            if oLink:
                GS2CErrorCode(oLink, LOGIN_ERRORCODE_OVERDUE)
                oLink.Remove()

    
    def AddHeartBeat(self, uid):
        if uid in self.m_Link:
            self.m_Link[uid] = GetSecond()

    
    def GetLink(self, pid):
        for uid in self.m_Link:
            oLink = GetObject(uid)
            if oLink and oLink.m_EditorPlayer == pid:
                return oLink
        

    
    def CheckLinkAlive(self):
        Remove_Call_Out('CheckLinkAlive')
        Call_Out(self.CheckLinkAlive, 30, 'CheckLinkAlive')
        iSecond = GetSecond()
        lstRemove = []
        for uid, iTime in self.m_Link.items():
            oLink = GetObject(uid)
            if not not oLink:
                if iSecond - iTime > 120:
                    lstRemove.append(uid)
                    continue
        
        for uid in lstRemove:
            self.RemoveLink(uid)
        



def GetBehaviorLinkMgr():
    oMgr = GetGlobalManager('BehaviorLinkMgr')
    if not oMgr:
        oMgr = CLinkManager()
        oMgr.CheckLinkAlive()
        SetGlobalManager('BehaviorLinkMgr', oMgr)
    return oMgr

