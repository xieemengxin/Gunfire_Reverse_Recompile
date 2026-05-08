# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_season/mobile/data.pyc
# RelativePath: clientlogic/cl_season/mobile/data.pyc
# Source Generated with Decompyle++
# File: data.pyc (Python 3.6)

g_MBAllSeasonTask = { }
g_MBGSSeasonTask = { }
g_MBGSWarTask = { }
g_MBGSWarDoneTask = { }
g_MBWarSeasonTask = { }
g_MBOldSeasonPutInfo = { }
g_MBAllSeasonTask[1] = {
    1002: 1000,
    1003: 200,
    1004: 10,
    1005: 2000,
    1008: 1,
    1009: 1,
    1010: 1,
    1011: 1,
    1012: 1,
    1013: 1,
    1014: 1,
    1015: 1,
    1016: 20,
    1017: 150,
    1018: 30000,
    1019: 3000,
    1021: 10,
    1022: 60,
    1023: 1,
    1024: 1,
    1025: 1,
    1026: 1,
    1027: 1,
    1028: 4,
    1029: 0x2540BE400,
    1030: 5,
    1031: 25,
    1032: 30,
    1033: 1,
    1034: 100,
    1035: 1,
    1036: 1,
    1037: 1,
    1039: 1,
    1041: 50,
    1042: 1,
    1043: 1,
    1044: 1,
    1045: 1,
    1046: 1,
    1047: 1,
    1048: 8,
    1049: 1,
    1051: 30,
    1052: 1,
    1053: 1,
    1054: 1,
    1055: 300,
    1056: 500,
    1057: 100 }
g_MBGSSeasonTask[1] = {
    1019: 1,
    1030: 1,
    1031: 1,
    1033: 1,
    1035: 1,
    1042: 1 }
g_MBGSWarTask[1] = {
    1019: 1 }
g_MBWarSeasonTask[1] = {
    1002: 1,
    1003: 1,
    1004: 1,
    1005: 1,
    1008: 1,
    1009: 1,
    1010: 1,
    1011: 1,
    1012: 1,
    1013: 1,
    1014: 1,
    1015: 1,
    1016: 1,
    1017: 1,
    1018: 1,
    1019: 1,
    1021: 1,
    1022: 1,
    1023: 1,
    1024: 1,
    1025: 1,
    1026: 1,
    1027: 1,
    1028: 1,
    1029: 1,
    1032: 1,
    1034: 1,
    1036: 1,
    1037: 1,
    1039: 1,
    1041: 1,
    1043: 1,
    1044: 1,
    1045: 1,
    1046: 1,
    1047: 1,
    1048: 1,
    1049: 1,
    1051: 1,
    1052: 1,
    1053: 1,
    1054: 1,
    1055: 1,
    1056: 1,
    1057: 1 }
g_MBGSWarDoneTask[1] = { }
g_MBAllSeasonTask[4] = {
    1001: 20,
    1002: 10 }
g_MBGSSeasonTask[4] = {
    1002: 1 }
g_MBWarSeasonTask[4] = {
    1001: 1 }
g_MBGSWarDoneTask[4] = {
    1002: 1 }
g_MBAllSeasonTask[5] = { }
g_MBGSSeasonTask[5] = { }
g_MBWarSeasonTask[5] = { }
g_MBGSWarDoneTask[5] = { }
g_MBAllSeasonTask[6] = { }
g_MBGSSeasonTask[6] = { }
g_MBWarSeasonTask[6] = { }
g_MBGSWarDoneTask[6] = { }

def GetAllSeasonTask(iSeason):
    if iSeason in g_MBAllSeasonTask:
        return g_MBAllSeasonTask[iSeason]
    return { }


def GetGSSeasonTask(iSeason):
    if iSeason in g_MBGSSeasonTask:
        return g_MBGSSeasonTask[iSeason]
    return { }


def GetGSWarTask(iSeason):
    if iSeason in g_MBGSWarTask:
        return g_MBGSWarTask[iSeason]
    return { }


def GetGSWarDoneTask(iSeason):
    if iSeason in g_MBGSWarDoneTask:
        return g_MBGSWarDoneTask[iSeason]
    return { }


def GetWarSeasonTask(iSeason):
    if iSeason in g_MBWarSeasonTask:
        return g_MBWarSeasonTask[iSeason]
    return { }


def OldSeasonPutInfo():
    return g_MBOldSeasonPutInfo

