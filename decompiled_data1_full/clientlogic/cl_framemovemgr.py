# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_framemovemgr.pyc
# RelativePath: clientlogic/cl_framemovemgr.pyc
# Source Generated with Decompyle++
# File: cl_framemovemgr.pyc (Python 3.6)


class CFrameMoveMgr(object):
    
    def __init__(self):
        self.m_MoveInfo = { }

    
    def AddSimObj(self, obj, tVec, iFrame):
        oGame = obj.m_Game
        iCurFrame = oGame.GetFrameNum()
        self.m_MoveInfo[obj.m_ID] = (tVec, iCurFrame + iFrame)

    
    def RemoveSimObj(self, obj):
        oid = obj.m_ID
        if oid not in self.m_MoveInfo:
            return None
        self.m_MoveInfo.pop(oid)

    
    def GetMoveInfo(self, obj):
        oid = obj.m_ID
        if oid not in self.m_MoveInfo:
            return None
        return self.m_MoveInfo[oid]

    
    def Update(self, oGame, iCurFrame):
        if not self.m_MoveInfo:
            return None
        lstDead = []
        for oid, (tVec, iDstFrame) in self.m_MoveInfo.items():
            oMove = oGame.GetObject(oid)
            if not oMove or oMove.IsDead():
                lstDead.append(oid)
                continue
            if iDstFrame < iCurFrame:
                oMove.TerminalPos()
                lstDead.append(oid)
                continue
            oMove.UpdatePos(tVec)
        
        for oid in lstDead:
            self.m_MoveInfo.pop(oid)
        

    
    def Release(self):
        self.m_MoveInfo = { }


