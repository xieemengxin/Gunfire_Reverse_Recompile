# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_npc/tasknpcaction.pyc
# RelativePath: clientlogic/cl_npc/tasknpcaction.pyc
# Source Generated with Decompyle++
# File: tasknpcaction.pyc (Python 3.6)

from cl_item.defines import WEAPON_ACTION_INSC_ALL_NOR2RARE, WEAPON_ACTION_INSC_ONE_NOR2RARE, WEAPON_ACTION_INSC_ONE_NORRARE2EXCLU
from cl_commondefines import VIRTUAL_ITEM_TALENT, NPC_CB_VALUELIST, TASK_CHOOSEFUN_END, UPGRADE_INS_RS_TASK
from cl_cscommondef.cs_itemdef import EQUIP_TYPE_MAINWEAPON
from cl_object.logging import WarnpcLog, TaskLog
from cl_only import Functor
from cl_npc import net
import cl_msgcenter
import cl_item
import cl_putdata
import cl_minigame
EVENT_TYPE_CHOOSE_UPGRADE_TALENT = 11

def CBChooseFunc(iNpc, iTask, cbEndFunc, dArgs, oHero, lstAnswer):
    oNpc = oHero.m_Game.GetObject(iNpc)
    if not oNpc:
        return None
    if not lstAnswer:
        oNpc.RefreshUI(oHero)
        return None
    oTask = oNpc.HeroChooseTask(oHero, iTask)
    cbEndFunc(oHero, oTask, lstAnswer)
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_TASK, oHero, {
        'TaskID': oTask.m_ID,
        'TaskSID': oTask.m_SID }, iSub = TASK_CHOOSEFUN_END)


def TaskChooseUpgradeTalentReward(oHero, oNpc, iChoose, tArgs):
    
    def ChooseEnd(oHero, oTask, lstAnswer):
        if not ValidChooseTalent(oHero, lstAnswer):
            return None
        oTask.SetSaveData('ChooseUpgradeTalent', lstAnswer)

    
    def ValidChooseTalent(oHero, lstAnswer):
        oTalentCon = oHero.m_TalentCon
        iLen = 0
        iCanChoose = 0
        for iTalent in lstAnswer:
            iLen += 1
            oTalent = oTalentCon.GetPerform(iTalent)
            if oTalent and oTalent.m_Level == oTalent.m_MaxLevel:
                WarnpcLog.Alert('task choose valid talent %s %s %s %s' % (oHero.m_PlayerID, lstAnswer, iTalent, oTalent.m_Level))
                break
            iCanChoose += 1
        
        return iCanChoose >= iLen

    lstHasTalent = []
    net.GS2CNPCEventChoose(oHero, VIRTUAL_ITEM_TALENT, 1, lstHasTalent, EVENT_TYPE_CHOOSE_UPGRADE_TALENT)
    net.SetNpcUICallBackFunction(oHero, NPC_CB_VALUELIST, Functor(CBChooseFunc, oNpc.m_ID, iChoose, ChooseEnd, 'ChooseUpgradeTalent'), oNpc)


def TaskChooseUpgradeInscription(oHero, oNpc, iChoose, tArgs):
    
    def ChooseEnd(oHero, oTask, lstAnswer):
        iWeapon = lstAnswer[0]
        oWeapon = oHero.m_WieldCon.GetItemByID(iWeapon)
        iGame = oHero.m_Game.m_ID
        iPlayer = oHero.m_PlayerID
        if not oWeapon:
            TaskLog.Alert('%s taskupgradeinscriptionnoweapon %s %s %s' % (iGame, iPlayer, oTask.m_SID, lstAnswer))
            return None
        oInscriptionCom = oWeapon.GetComponent('Inscription')
        if not oInscriptionCom:
            TaskLog.Alert('%s taskupgradeinscriptionnocom %s %s %s' % (iGame, iPlayer, oTask.m_SID, lstAnswer))
            return None
        if not oInscriptionCom.ValidUpgradeActionType(iActionType):
            TaskLog.Alert('%s taskupgradeinscriptionfail %s %s %s' % (iGame, iPlayer, oTask.m_SID, lstAnswer))
            return None
        dInfo = {
            'Reason': UPGRADE_INS_RS_TASK }
        if iActionType in [
            WEAPON_ACTION_INSC_ONE_NOR2RARE,
            WEAPON_ACTION_INSC_ONE_NORRARE2EXCLU]:
            iInscription = lstAnswer[1]
            dInfo['Appoint'] = [
                iInscription]
        lstUpgrade = oInscriptionCom.UpgradeByActionType(iActionType, dInfo)
        oTask.SetSaveData('ChooseUpgradeInscription', lstUpgrade)

    lstInfo = []
    lstWeapon = oHero.m_WieldCon.GetAllItemByType(EQUIP_TYPE_MAINWEAPON)
    lstWeaponInfo = []
    iActionType = tArgs[0]
    for oWeapon in lstWeapon:
        oInscriptionCom = oWeapon.GetComponent('Inscription')
        if not oInscriptionCom:
            continue
        iValid = oInscriptionCom.ValidUpgradeActionType(iActionType)
        lstWeaponInfo.append([
            oWeapon.m_ID,
            oWeapon.m_Pos,
            iValid,
            {
                'Attr': [] }])
    
    lstInfo = [
        [
            lstWeaponInfo,
            0]]
    net.GS2CNPCEventWeaponAction(oHero, iActionType, oNpc.m_FightType, lstInfo)
    net.SetNpcUICallBackFunction(oHero, NPC_CB_VALUELIST, Functor(CBChooseFunc, oNpc.m_ID, iChoose, ChooseEnd, 'ChooseUpgradeTalent'), oNpc)


def TaskForbidNpcExtraInteract(oHero, oNpc, iChoose, tArgs):
    oNpc.ForbidExtraInteract(oHero)
    oNpc.HeroChooseTask(oHero, iChoose)


def TaskChooseSubTask(oHero, oNpc, iTask, tArgs):
    if len(tArgs) < 3:
        TaskLog.Error('%s %s args not enough %s' % (oHero.m_Game.m_ID, oHero.m_PlayerID, iTask))
        return None
    iQuality = tArgs[0]
    iMiniGameID = tArgs[1]
    dExcludeTask = tArgs[2]
    iHero = oHero.m_ID
    dLimitTaskInfo = {
        iHero: {
            'Quality': [
                iQuality],
            'ChooseNum': 1,
            'ExcludeTasks': list(dExcludeTask),
            'ExecChooseBeforeCond': 0 } }
    oMiniGame = cl_minigame.NewMiniGame(oHero.m_Game, iMiniGameID, 0, iHero, {
        'LimitTaskInfo': dLimitTaskInfo })
    lstReward = oMiniGame.Query('Reward')
    if not lstReward:
        TaskLog.Error('%s %s %s choose subtask err %s' % (oHero.m_Game.m_ID, oHero.m_PlayerID, iTask, iQuality))
        return None
    iSubTask = lstReward[0]
    dTaskExtraSubTask = oNpc.m_TaskExtraSubTask.setdefault(iHero, { })
    dTaskExtraSubTask[iTask] = iSubTask
    oNpc.m_TaskExtraSubTask[iHero] = dTaskExtraSubTask

g_TaskOptionAction = {
    1011: {
        'Func': TaskChooseUpgradeInscription,
        'Args': (WEAPON_ACTION_INSC_ONE_NOR2RARE,) },
    1017: {
        'Func': TaskForbidNpcExtraInteract,
        'Args': () },
    1111: {
        'Func': TaskChooseUpgradeInscription,
        'Args': (WEAPON_ACTION_INSC_ALL_NOR2RARE,) },
    1117: {
        'Func': TaskForbidNpcExtraInteract,
        'Args': () },
    1211: {
        'Func': TaskChooseUpgradeInscription,
        'Args': (WEAPON_ACTION_INSC_ONE_NORRARE2EXCLU,) },
    1217: {
        'Func': TaskForbidNpcExtraInteract,
        'Args': () } }

def GetTaskOptionAction():
    return g_TaskOptionAction

g_TaskSelectedAction = {
    1016: {
        'Func': TaskChooseSubTask,
        'Args': (1, 8001, {
            1016: 1,
            1017: 1,
            1005: 1,
            1001: 1,
            1014: 1,
            1015: 1 }) },
    1017: {
        'Func': TaskChooseSubTask,
        'Args': (1, 8001, {
            1016: 1,
            1017: 1,
            1005: 1,
            1001: 1,
            1014: 1,
            1015: 1 }) },
    1117: {
        'Func': TaskChooseSubTask,
        'Args': (2, 8001, {
            1116: 1,
            1117: 1,
            1105: 1,
            1101: 1,
            1114: 1,
            1115: 1 }) },
    1217: {
        'Func': TaskChooseSubTask,
        'Args': (3, 8001, {
            1216: 1,
            1217: 1,
            1205: 1,
            1201: 1,
            1215: 1 }) } }

def GetTaskSelectedAction():
    return g_TaskSelectedAction

