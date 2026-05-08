# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_minigame/mobject.pyc
# RelativePath: clientlogic/cl_minigame/mobject.pyc
# Source Generated with Decompyle++
# File: mobject.pyc (Python 3.6)

import cl_reward
import cl_math
import cl_msgcenter
import cl_reward

class CBaseGameData(object):
    m_SID = 0
    m_Type = 0
    
    def InitMiniGame(cls, oMiniGame):
        raise NotImplementedError('subclasses must implement')

    InitMiniGame = classmethod(InitMiniGame)
    
    def CheckShiftGameClass(cls, oGame, iOwner):
        return cls.GetGameClass()

    CheckShiftGameClass = classmethod(CheckShiftGameClass)
    
    def GetGameClass(cls):
        raise NotImplementedError('subclasses must implement')

    GetGameClass = classmethod(GetGameClass)
    
    def InitGame(cls, oMiniGame):
        oMiniGame.m_SID = cls.m_SID
        oMiniGame.m_Type = cls.m_Type
        cls.InitMiniGame(oMiniGame)
        return oMiniGame

    InitGame = classmethod(InitGame)


class CBaseMiniGame(object):
    m_SID = 0
    m_Type = 0
    m_C2GSOPFunc = { }
    m_Source = 0
    
    def __init__(self, oGame):
        self.m_Game = oGame
        self.m_ID = 0
        self.m_Owner = 0
        self.m_Player = 0
        self.m_Data = { }
        self.m_EndCallBack = []
        self.m_ChooseWeight = { }

    
    def Init(self, iID, iOwner, iPlayer, iSource, dData):
        self.m_ID = iID
        self.m_Owner = iOwner
        self.m_Player = iPlayer
        self.m_Data = dict(dData)
        self.m_EndCallBack = []
        self.m_Source = iSource
        self.m_Data['Player'] = iPlayer

    
    def Set(self, k, v):
        self.m_Data[k] = v

    
    def Query(self, k, default = None):
        if k not in self.m_Data:
            return default
        return self.m_Data[k]

    
    def C2GSGameOP(self, who, iSub, iAnswer):
        if who.m_ID != self.m_Player:
            return None
        if iSub not in self.m_C2GSOPFunc:
            print('Err GameOP %d' % iSub)
            return None
        func = self.m_C2GSOPFunc[iSub]
        func(self, who, iAnswer)

    
    def Recycle(self):
        self.m_ID = 0
        self.m_Owner = 0
        self.m_Player = 0
        self.m_Data = { }
        self.m_EndCallBack = []
        self.m_ChooseWeight = { }

    
    def Release(self):
        self.m_Game = None

    
    def OnInit(self):
        dData = self.GetChooseData()
        oWarMgr = self.m_Game.m_WarMgr
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_MINIGAMEINIT, oWarMgr, dData)

    
    def Start(self):
        self.m_Game.m_MiniGameMgr.PlayerEnterMiniGame(self.m_Player, self.m_ID)

    
    def Leave(self):
        self.m_Game.m_MiniGameMgr.PlayerLeaveMiniGame(self.m_Player, self.m_ID)

    
    def End(self):
        if self.m_EndCallBack:
            lstFunc = self.m_EndCallBack
            self.m_EndCallBack = None
            for func in lstFunc:
                func(self)
            
        self.m_Game.m_MiniGameMgr.PlayerLeaveMiniGame(self.m_Player, self.m_ID)
        self.m_Game.m_MiniGameMgr.DeleteMiniGame(self)

    
    def OnPlayerReady(self):
        pass

    
    def AddEndCallBack(self, func):
        self.m_EndCallBack.append(func)

    
    def GetChooseData(self):
        dData = {
            'ChooseWeight': self.m_ChooseWeight,
            'MiniGameType': self.m_Type }
        return dData

    
    def GetDropBasePos(self):
        return cl_reward.GetDropBasePos(self.m_Game.GetObject(self.m_Owner))



class CDropChoose(object):
    
    def Choose(cls, oPlayer, dWeight):
        return 0

    Choose = classmethod(Choose)
    
    def ChooseExt(cls, oPlayer, dWeight, dExt):
        return cls.Choose(oPlayer, dWeight)

    ChooseExt = classmethod(ChooseExt)


class CDropGame(CBaseMiniGame):
    
    def OnInit(self):
        super(CDropGame, self).OnInit()
        if self.Query('AutoRefresh', 1):
            self.RefreshReward()

    
    def RefreshReward(self):
        lstReward = self.GetRewardInfo()
        self.Set('Reward', lstReward)

    
    def Start(self):
        super(CDropGame, self).Start()
        iAngle = self.m_Game.Random(360)
        vFly = cl_math.Vec2DestPosDir((0, 0), (0, 1), 10, iAngle)
        self.m_Data.update({
            'Face': vFly })
        if self.Query('AutoReward', 1):
            self.SendReward()
        else:
            self.Leave()

    
    def SendReward(self):
        who = self.m_Game.GetObject(self.m_Player)
        lstReward = self.Query('Reward', [])
        self.Set('Reward', [])
        if lstReward:
            cl_reward.RewardItem(self.m_Game, who, lstReward, 'MiniGame%s-%s' % (self.m_SID, self.m_ID), self.m_Data)
        self.End()

    
    def GetRewardInfo(self):
        return []



class CRewardChooseGame(CBaseMiniGame):
    
    def OnInit(self):
        super(CRewardChooseGame, self).OnInit()
        dReward = self.GetRewardInfo()
        self.Set('Reward', dReward)

    
    def Start(self):
        super(CRewardChooseGame, self).Start()
        self.SendChoose()

    
    def SendChoose(self):
        pass

    
    def GetRewardInfo(self):
        return { }


