# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_seasontalent/pc/data.pyc
# RelativePath: clientlogic/cl_seasontalent/pc/data.pyc
# Source Generated with Decompyle++
# File: data.pyc (Python 3.6)

g_SeasonTalent = { }
g_SeasonTalentUnlockGrade = { }
g_GSSeasonTalent = { }
g_DefaultUnlock = { }
g_SeasonTalentUnlockGrade = {
    3: {
        5: [
            1001],
        10: [
            1002],
        15: [
            1003],
        20: [
            1004],
        25: [
            1005],
        30: [
            1007],
        35: [
            1008],
        12: [
            1009],
        18: [
            1010] },
    4: {
        2: [
            1011],
        5: [
            1012],
        10: [
            1013],
        20: [
            1014],
        25: [
            1015],
        30: [
            1016],
        40: [
            1017],
        15: [
            1018],
        35: [
            1019] },
    5: {
        2: [
            1020],
        5: [
            1021],
        10: [
            1022],
        20: [
            1023],
        25: [
            1024],
        30: [
            1025],
        40: [
            1026],
        15: [
            1027],
        0: [
            1028],
        35: [
            1029] },
    6: {
        0: [
            1030],
        2: [
            1031],
        5: [
            1032],
        10: [
            1033],
        15: [
            1034],
        20: [
            1035],
        25: [
            1036],
        30: [
            1037],
        35: [
            1038],
        40: [
            1039] },
    7: {
        0: [
            1040],
        2: [
            1041],
        5: [
            1042],
        10: [
            1043],
        15: [
            1044],
        20: [
            1045],
        25: [
            1046],
        30: [
            1047],
        35: [
            1048],
        40: [
            1049] },
    8: {
        0: [
            1050],
        2: [
            1051],
        5: [
            1052],
        10: [
            1053],
        15: [
            1054],
        20: [
            1055],
        25: [
            1056],
        30: [
            1057],
        35: [
            1058],
        40: [
            1059] } }
g_SeasonTalent = {
    3: {
        1001: 5,
        1002: 10,
        1003: 15,
        1004: 20,
        1005: 25,
        1007: 30,
        1008: 35,
        1009: 12,
        1010: 18 },
    4: {
        1011: 2,
        1012: 5,
        1013: 10,
        1014: 20,
        1015: 25,
        1016: 30,
        1017: 40,
        1018: 15,
        1019: 35 },
    5: {
        1020: 2,
        1021: 5,
        1022: 10,
        1023: 20,
        1024: 25,
        1025: 30,
        1026: 40,
        1027: 15,
        1028: 0,
        1029: 35 },
    6: {
        1030: 0,
        1031: 2,
        1032: 5,
        1033: 10,
        1034: 15,
        1035: 20,
        1036: 25,
        1037: 30,
        1038: 35,
        1039: 40 },
    7: {
        1040: 0,
        1041: 2,
        1042: 5,
        1043: 10,
        1044: 15,
        1045: 20,
        1046: 25,
        1047: 30,
        1048: 35,
        1049: 40 },
    8: {
        1050: 0,
        1051: 2,
        1052: 5,
        1053: 10,
        1054: 15,
        1055: 20,
        1056: 25,
        1057: 30,
        1058: 35,
        1059: 40 } }
g_GSSeasonTalent = {
    1004: 1,
    1016: 1,
    1018: 1,
    1019: 1,
    1021: 1,
    1022: 1,
    1023: 1,
    1024: 1,
    1025: 1,
    1027: 1,
    1028: 1,
    1029: 1,
    1030: 1,
    1033: 1,
    1034: 1,
    1035: 1,
    1036: 1,
    1037: 1,
    1038: 1,
    1039: 1,
    1040: 1,
    1042: 1,
    1044: 1 }
g_DefaultUnlock = { }
g_CustomSeasonSuitTempTalent = 1016

def GetSeasonTalentBySeasonNum(iSeasonNum):
    if iSeasonNum not in g_SeasonTalent:
        return { }
    return g_SeasonTalent[iSeasonNum]


def GetSeasonTalentBySeasonGrade(iSeasonNum, iSeasonGrade):
    if iSeasonNum not in g_SeasonTalentUnlockGrade:
        return []
    if iSeasonGrade not in g_SeasonTalentUnlockGrade[iSeasonNum]:
        return []
    return g_SeasonTalentUnlockGrade[iSeasonNum][iSeasonGrade]


def HasGSReward(iSeasonTalent):
    return iSeasonTalent in g_GSSeasonTalent


def GetDefaultUnlock(iSeasonNum):
    if iSeasonNum not in g_DefaultUnlock:
        return { }
    return g_DefaultUnlock[iSeasonNum]


def GetCustomSeasonSuitTempTalent():
    return g_CustomSeasonSuitTempTalent

