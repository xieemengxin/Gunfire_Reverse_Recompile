# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/skilldebug.pyc
# RelativePath: clientlogic/cl_perform/skilldebug.pyc
# Source Generated with Decompyle++
# File: skilldebug.pyc (Python 3.6)

from cl_only import log_file_debug
from cl_commondefines import WARRIOR_HERO, WARRIOR_MASK
from cli_player import GetPlayer
import traceback
import itertools
import cl_notify
import cl_framegame
import cllib.lib_flag

def GetHero(pid):
    who = GetPlayer(pid)
    if not who:
        return None
    oGame = cl_framegame.GetGame(who.m_GameID)
    if not oGame:
        return None
    return oGame.m_WarMgr.GetHeroByPlayer(pid)


def GetPerformImportCode():
    sText = '\nimport cl_math\nimport cl_msgcenter\nimport cl_action\nimport cl_condition\nimport cl_evact\nimport cl_evcon\n'
    return sText


def CheckPythonSyntax(sCode):
    
    try:
        compile(sCode, '', 'exec')
        return ''
    except SyntaxError as err:
        
        try:
            return err.text
        finally:
            err = None
            del err




def ExceptionCatchFunc(oGame, iHero, iPerform, func):
    
    def _Run(*args, **kwargs):
        
        try:
            func(*args, **kwargs)
        except Exception as e:
            
            try:
                oHero = oGame.GetObject(iHero)
                if oHero:
                    cl_notify.GS2CDebugMsg(oHero.m_Game, oHero.m_PlayerID, '技能%d 执行%s 出错,请查看GM界面打印' % (iPerform, func.__name__))
                    cl_notify.InternalTips(oHero, str(traceback.format_exc()))
                    cl_notify.InternalTips(oHero, '%s:%s' % (e.__class__, e))
            finally:
                e = None
                del e



    return _Run


class SkillDebug(object):
    
    def __init__(self, oGame):
        self.m_Game = oGame
        self.m_SkillDebugger = { }
        self.m_SkillData = { }
        self.m_SkillStr = { }
        self.m_SkillTmpFunc = set()
        self.m_TmpFunc = { }

    
    def SetDebugFunc(self):
        self.m_TmpFunc['NewPerform'] = self.m_Game.m_ResMgr.NewPerform
        self.m_TmpFunc['Release'] = self.m_Game.Release
        self.m_TmpFunc['NewSkill'] = self.m_Game.m_SkillMgr.NewSkill
        self.m_TmpFunc['Recycle'] = self.m_Game.m_SkillMgr.Recycle
        self.m_Game.m_ResMgr.NewPerform = self.NewPerform
        self.m_Game.Release = self.GameRelease
        self.m_Game.m_SkillMgr.NewSkill = self.NewSkill
        self.m_Game.m_SkillMgr.Recycle = self.Recycle
        self.m_Game.m_SkillDebug = self

    
    def NewPerform(self, iPerform, oOwner, iLevel):
        oPerform = self.m_TmpFunc['NewPerform'](iPerform, oOwner, iLevel)
        if oPerform and iPerform in self.m_SkillData:
            self.ReplacePerform(oPerform, self.m_SkillData[iPerform])
        return oPerform

    
    def GameRelease(self):
        oSkillMgr = self.m_Game.m_SkillMgr
        for tKey in self.m_SkillTmpFunc:
            oSkill = oSkillMgr.GetSkill(*tKey)
            if not oSkill:
                continue
            del oSkill.Start
            del oSkill.Update
            del oSkill.NetTriggerUpdate
        
        self.m_SkillTmpFunc = set()
        self.m_TmpFunc['Release']()
        self.m_Game.m_ResMgr.NewPerform = self.m_TmpFunc['NewPerform']
        self.m_Game.Release = self.m_TmpFunc['Release']
        oSkillMgr.NewSkill = self.m_TmpFunc['NewSkill']
        oSkillMgr.Recycle = self.m_TmpFunc['Recycle']
        del self.m_Game.m_SkillDebug
        del self.m_Game.m_ResMgr.NewPerform
        del self.m_Game.Release
        del oSkillMgr.NewSkill
        del oSkillMgr.Recycle
        self.Release()

    
    def NewSkill(self, oAttack, pfobj, dData):
        oGame = self.m_Game
        oSkill = self.m_TmpFunc['NewSkill'](oAttack, pfobj, dData)
        iPerform = pfobj.m_SID
        if iPerform in self.m_SkillData:
            pid = self.m_SkillDebugger[iPerform]
            tKey = (oSkill.m_Base['AID'], oSkill.m_Base['ActNum'])
            self.m_SkillTmpFunc.add(tKey)
            oSkill.Start = ExceptionCatchFunc(oGame, pid, iPerform, oSkill.Start)
            oSkill.Update = ExceptionCatchFunc(oGame, pid, iPerform, oSkill.Update)
            oSkill.NetTriggerUpdate = ExceptionCatchFunc(oGame, pid, iPerform, oSkill.NetTriggerUpdate)
            oSkill.m_Base['Debug'] = 1
        return oSkill

    
    def Recycle(self, tKey, iPerfrom):
        oSkill = self.m_Game.m_SkillMgr.GetSkill(*tKey)
        if tKey in self.m_SkillTmpFunc:
            del oSkill.Start
            del oSkill.Update
            del oSkill.NetTriggerUpdate
            self.m_SkillTmpFunc.remove(tKey)
        self.m_TmpFunc['Recycle'](tKey, iPerfrom)

    
    def SkillImport(self):
        return GetPerformImportCode()

    
    def SetSkillData(self, oHero, iPerform, sCode):
        sCode = self.SkillImport() + sCode
        err = CheckPythonSyntax(sCode)
        if err:
            sReason = '%s有错误\n#R%s#n' % (iPerform, err)
            cl_notify.GS2CDebugMsg(self.m_Game, oHero.m_PlayerID, sReason)
            return None
        dRet = { }
        
        try:
            exec(sCode, dRet)
        except:
            cl_notify.GS2CDebugMsg(self.m_Game, oHero.m_PlayerID, 'SetSkillDataError')
            return None

        self.Load(oHero, iPerform, dRet, sCode)

    
    def Load(self, oHero, iPerform, dCode, sCode):
        for oWarrior in self.m_Game.Scene_GetObjects(oHero.m_Scene):
            if oWarrior.m_FightType & WARRIOR_HERO:
                self.ReplaceHeroOldPerform(oWarrior, iPerform, dCode)
                continue
            if oWarrior.m_FightType & WARRIOR_MASK:
                self.ReplaceWarriorOldPerform(oWarrior, iPerform, dCode)
        
        self.m_SkillStr[iPerform] = sCode
        self.m_SkillData[iPerform] = dCode
        self.m_SkillDebugger[iPerform] = oHero.m_ID

    
    def ReplaceHeroOldPerform(self, oHero, iPerform, dCode):
        oPerform = oHero.GetPerform(iPerform)
        if oPerform:
            self.ReplacePerform(oPerform, dCode)
            return None
        lstEquip = oHero.m_WieldCon.ItemList()
        lstItem = oHero.m_ItemCon.ItemList()
        for oItem in itertools.chain(lstEquip, lstItem):
            oPerformCom = oItem.GetComponent('Perform')
            if not oPerformCom:
                continue
            oPerform = oPerformCom.GetPerform(iPerform)
            if oPerform:
                self.ReplacePerform(oPerform, dCode)
        

    
    def ReplaceWarriorOldPerform(self, oWarrior, iPerform, dCode):
        oPerform = oWarrior.GetPerform(iPerform)
        if oPerform:
            self.ReplacePerform(oPerform, dCode)

    
    def ReplacePerform(self, oPerform, dCode):
        oPerform.DebugReplace(dCode)

    
    def Release(self):
        self.m_Game = None
        self.m_SkillData = { }
        self.m_SkillStr = { }
        self.m_TmpFunc = { }
        self.m_SkillTmpFunc = set()
        self.m_SkillDebugger = { }



def R_StartSkillDebug(resfunc, pid):
    if not cllib.lib_flag.g_IsInternalRun:
        return None
    oHero = GetHero(pid)
    if not oHero:
        return None
    if not hasattr(oHero.m_Game, 'm_SkillDebug'):
        oGame = oHero.m_Game
        oDebug = SkillDebug(oGame)
        oDebug.SetDebugFunc()
        if oGame.m_WarKeep:
            oGame.m_WarKeep.ChangeKickDelayTime(12000)


def R_SkillDebugData(resfunc, pid, iPerform, sSkillContent):
    if not cllib.lib_flag.g_IsInternalRun:
        return None
    oHero = GetHero(pid)
    if not oHero:
        return None
    oSkillDebug = getattr(oHero.m_Game, 'm_SkillDebug', None)
    if not oSkillDebug:
        return None
    oSkillDebug.SetSkillData(oHero, iPerform, sSkillContent)

