# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_container/emotioncon.pyc
# RelativePath: clientlogic/cl_container/emotioncon.pyc
# Source Generated with Decompyle++
# File: emotioncon.pyc (Python 3.6)

import cl_duonet.dn_cl_item_cnet

def GS2CEmotion(oGame, lstCurEmotion, pid):
    netData = {
        'lstCur': lstCurEmotion,
        'oGame': oGame,
        'pid': pid }
    cl_duonet.dn_cl_item_cnet.DN_GS2CEmotion(netData)


class CEmotionContainer(object):
    
    def __init__(self, oGame, iOwner, iPlayerID):
        self.m_Game = oGame
        self.m_Owner = iOwner
        self.m_PlayerID = iPlayerID

    
    def Refresh(self):
        lstCurEmotion = []
        oHero = self.m_Game.GetObject(self.m_Owner)
        for iIndex, iEmotion in oHero.Query('Illus')['Emotion'].items():
            lstCurEmotion.append((iIndex, iEmotion))
        
        GS2CEmotion(self.m_Game, lstCurEmotion, self.m_PlayerID)


