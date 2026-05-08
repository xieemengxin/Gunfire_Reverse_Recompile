# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_dlcdata.pyc
# RelativePath: clientlogic/cl_dlcdata.pyc
# Source Generated with Decompyle++
# File: cl_dlcdata.pyc (Python 3.6)

from cl_commondefines import REWARD_UNLOCK_HERO, REWARD_UNLOCK_WAEAPON, VIRTUAL_ITEM_AVATAR
from cllib import lib_flag
from cllib.lib_only import RunMobileData
g_RewardTypeDict = {
    REWARD_UNLOCK_WAEAPON: { },
    REWARD_UNLOCK_HERO: { } }
g_Payment = { }
g_Dlc2Reward = { }

def GetAllDlcAppID(sKey):
    lstAppID = []
    for dPay in g_Payment.values():
        if sKey in dPay:
            lstAppID.append(dPay[sKey])
    
    return lstAppID


def GetDlcListByDlcType(lstDlcType, sType):
    lstDlc = []
    for iDlc, dPay in g_Payment.items():
        if sType not in dPay:
            continue
        iDlcType = dPay[sType]
        if iDlcType in lstDlcType:
            lstDlc.append(iDlc)
    
    return lstDlc

g_Payment = {
    2001: {
        'Name': '灵界来客',
        'DlcType': 2,
        'WegameDlcID': 2001827,
        'SteamQADlcID': 1822432,
        'SteamDlcID': 2111850 },
    2011: {
        'Name': '神谋巧匠',
        'DlcType': 3,
        'WegameDlcID': 2001969,
        'SteamQADlcID': 1822431,
        'SteamDlcID': 2430400 },
    2021: {
        'Name': '墨雪画境',
        'DlcType': 4,
        'WegameDlcID': 2002199,
        'SteamQADlcID': 0,
        'SteamDlcID': 3063250 },
    2031: {
        'Name': '古木灵歌',
        'DlcType': 5,
        'WegameDlcID': 0,
        'SteamQADlcID': 0,
        'SteamDlcID': 3920680 } }
g_PCDlc2Reward = {
    2001: {
        REWARD_UNLOCK_HERO: [
            214,
            215],
        REWARD_UNLOCK_WAEAPON: [
            1007,
            1214,
            1513,
            1514] },
    2011: {
        REWARD_UNLOCK_HERO: [
            216,
            217],
        REWARD_UNLOCK_WAEAPON: [
            1215,
            1312,
            1415,
            1108] },
    2021: {
        REWARD_UNLOCK_HERO: [
            218,
            219],
        REWARD_UNLOCK_WAEAPON: [
            1017,
            1417,
            1701,
            1703] },
    2031: {
        REWARD_UNLOCK_HERO: [
            220,
            221],
        REWARD_UNLOCK_WAEAPON: [
            1314,
            1516,
            1709,
            1217] } }
g_MobileDlc2Reward = {
    2: {
        REWARD_UNLOCK_HERO: [
            207] },
    3: {
        REWARD_UNLOCK_HERO: [
            212] },
    4: {
        REWARD_UNLOCK_HERO: [
            213] },
    5: {
        REWARD_UNLOCK_HERO: [
            215] },
    6: {
        REWARD_UNLOCK_HERO: [
            207] },
    7: {
        REWARD_UNLOCK_HERO: [
            212] },
    8: {
        REWARD_UNLOCK_HERO: [
            213] },
    9: {
        REWARD_UNLOCK_HERO: [
            215] },
    10: {
        REWARD_UNLOCK_HERO: [
            214] },
    11: {
        REWARD_UNLOCK_HERO: [
            214] },
    12: {
        REWARD_UNLOCK_HERO: [
            217] },
    13: {
        REWARD_UNLOCK_HERO: [
            217] },
    14: {
        REWARD_UNLOCK_HERO: [
            216] } }
g_MobileShenHeDlc2Reward = {
    2: {
        VIRTUAL_ITEM_AVATAR: [
            1004] },
    3: {
        VIRTUAL_ITEM_AVATAR: [
            1005] },
    4: {
        VIRTUAL_ITEM_AVATAR: [
            1006] },
    5: {
        VIRTUAL_ITEM_AVATAR: [
            1017] },
    6: {
        REWARD_UNLOCK_HERO: [
            207] },
    7: {
        REWARD_UNLOCK_HERO: [
            212] },
    8: {
        REWARD_UNLOCK_HERO: [
            213] },
    9: {
        REWARD_UNLOCK_HERO: [
            215] },
    10: {
        VIRTUAL_ITEM_AVATAR: [
            1016] },
    11: {
        REWARD_UNLOCK_HERO: [
            214] },
    12: {
        VIRTUAL_ITEM_AVATAR: [
            1018] },
    13: {
        REWARD_UNLOCK_HERO: [
            217] },
    14: {
        REWARD_UNLOCK_HERO: [
            216] } }

def InitDlcData():
    global g_Dlc2Reward, g_Dlc2Reward
    if RunMobileData():
        g_Dlc2Reward = g_MobileShenHeDlc2Reward if lib_flag.g_IsMobileShenHeRun else g_MobileDlc2Reward
    else:
        g_Dlc2Reward = g_PCDlc2Reward
    for iRewardType in g_RewardTypeDict:
        g_RewardTypeDict[iRewardType] = { }
    
    for iDlc, dReward in g_Dlc2Reward.items():
        for iRewardType, lstItem in dReward.items():
            if iRewardType not in g_RewardTypeDict:
                continue
            dItem2Dlc = g_RewardTypeDict[iRewardType]
            for iItem in lstItem:
                lstItem2Dlc = dItem2Dlc.setdefault(iItem, [])
                lstItem2Dlc.append(iDlc)
            
        
    


def GetDlc2Reward(iDlc):
    if iDlc not in g_Dlc2Reward:
        return { }
    return g_Dlc2Reward[iDlc]


def ValidDlc(iDlc):
    return iDlc in g_Dlc2Reward


def GetWeapon2Dlc():
    return g_RewardTypeDict[REWARD_UNLOCK_WAEAPON]


def GetHero2Dlc():
    return g_RewardTypeDict[REWARD_UNLOCK_HERO]

InitDlcData()
