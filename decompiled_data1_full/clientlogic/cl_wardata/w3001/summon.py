# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_wardata/w3001/summon.pyc
# RelativePath: clientlogic/cl_wardata/w3001/summon.pyc
# Source Generated with Decompyle++
# File: summon.pyc (Python 3.6)

from cl_resmgr.resdata import CSummonData as CCustom
import cl_wardata.summonaction as summonaction
import cl_resmgr.resdata as baseconfig

def SummonDieAction1006(oSummon, oKiller):
    summonaction.SummonDieRewardItemList(oSummon, oKiller, {
        201: {
            'Prop': 10000,
            'Times': 1 },
        202: {
            'Prop': 3000,
            'Times': 1 } }, 0, 0)


def SummonDieAction1016(oSummon, oKiller):
    summonaction.SummonDieRewardItemList(oSummon, oKiller, {
        201: {
            'Prop': 10000,
            'Times': 1 },
        202: {
            'Prop': 3000,
            'Times': 1 } }, 0, 1)


def SummonDieAction1024(oSummon, oKiller):
    summonaction.SummonDieRewardItemList(oSummon, oKiller, {
        201: {
            'Prop': 10000,
            'Times': 1 },
        202: {
            'Prop': 3000,
            'Times': 1 } }, 0, 1)


def SummonDieAction1028(oSummon, oKiller):
    summonaction.SummonDieRewardItemList(oSummon, oKiller, {
        205: {
            'Prop': 10000,
            'Times': 1 },
        202: {
            'Prop': 3000,
            'Times': 1 } }, 0, 0)


def SummonDieAction1029(oSummon, oKiller):
    summonaction.SummonDieRewardItemList(oSummon, oKiller, {
        205: {
            'Prop': 10000,
            'Times': 1 },
        202: {
            'Prop': 3000,
            'Times': 1 } }, 0, 0)


def SummonDieAction1045(oSummon, oKiller):
    summonaction.SummonDieRewardItemList(oSummon, oKiller, {
        201: {
            'Prop': 10000,
            'Times': 1 },
        202: {
            'Prop': 3000,
            'Times': 1 } }, 0, 1)


def SummonDieAction1053(oSummon, oKiller):
    summonaction.SummonDieRewardItemList(oSummon, oKiller, {
        204: {
            'Prop': 10000,
            'Times': 1 },
        202: {
            'Prop': 3000,
            'Times': 1 } }, 0, 1)


def SummonDieAction1074(oSummon, oKiller):
    summonaction.SummonDieRewardItemList(oSummon, oKiller, {
        204: {
            'Prop': 10000,
            'Times': 1 },
        202: {
            'Prop': 3000,
            'Times': 1 } }, 0, 1)


def SummonDieAction1075(oSummon, oKiller):
    summonaction.SummonDieRewardItemList(oSummon, oKiller, {
        205: {
            'Prop': 10000,
            'Times': 1 },
        202: {
            'Prop': 3000,
            'Times': 1 } }, 0, 0)


def SummonDieAction1076(oSummon, oKiller):
    summonaction.SummonDieRewardItemList(oSummon, oKiller, {
        201: {
            'Prop': 10000,
            'Times': 1 },
        202: {
            'Prop': 3000,
            'Times': 1 } }, 0, 1)


class CSummonData1001(baseconfig.CSummonData):
    m_SID = 1001
    m_DataSID = 1004
    m_Name = ''
    m_DieAction = None


class CSummonData1002(baseconfig.CSummonData):
    m_SID = 1002
    m_DataSID = 1005
    m_Name = ''
    m_DieAction = None


class CSummonData1003(baseconfig.CSummonData):
    m_SID = 1003
    m_DataSID = 1006
    m_Name = ''
    m_DieAction = None


class CSummonData1004(baseconfig.CSummonData):
    m_SID = 1004
    m_DataSID = 1007
    m_Name = ''
    m_DieAction = None


class CSummonData1005(baseconfig.CSummonData):
    m_SID = 1005
    m_DataSID = 1008
    m_Name = ''
    m_DieAction = None


class CSummonData1006(baseconfig.CSummonData):
    m_SID = 1006
    m_DataSID = 1009
    m_Name = ''
    m_DieAction = SummonDieAction1006


class CSummonData1008(baseconfig.CSummonData):
    m_SID = 1008
    m_DataSID = 1017
    m_Name = '毒桶'
    m_DieAction = None


class CSummonData1010(baseconfig.CSummonData):
    m_SID = 1010
    m_DataSID = 1010
    m_Name = '吞天'
    m_DieAction = None


class CSummonData1011(baseconfig.CSummonData):
    m_SID = 1011
    m_DataSID = 1011
    m_Name = '吞天'
    m_DieAction = None


class CSummonData1015(baseconfig.CSummonData):
    m_SID = 1015
    m_DataSID = 1015
    m_Name = '#NT#1006武器信标'
    m_DieAction = None


class CSummonData1016(baseconfig.CSummonData):
    m_SID = 1016
    m_DataSID = 1016
    m_Name = '鱼龙后裔'
    m_DieAction = SummonDieAction1016


class CSummonData1017(baseconfig.CSummonData):
    m_SID = 1017
    m_DataSID = 1019
    m_Name = '#NT#1411武器信标'
    m_DieAction = None


class CSummonData1018(baseconfig.CSummonData):
    m_SID = 1018
    m_DataSID = 1018
    m_Name = '精英沙蜥'
    m_DieAction = None


class CSummonData1020(baseconfig.CSummonData):
    m_SID = 1020
    m_DataSID = 1020
    m_Name = '#NT#孵化物'
    m_DieAction = None


class CSummonData1021(baseconfig.CSummonData):
    m_SID = 1021
    m_DataSID = 1021
    m_Name = '敖龙'
    m_DieAction = None


class CSummonData1022(baseconfig.CSummonData):
    m_SID = 1022
    m_DataSID = 1022
    m_Name = '夜姬丸'
    m_DieAction = None


class CSummonData1023(baseconfig.CSummonData):
    m_SID = 1023
    m_DataSID = 1023
    m_Name = '河童'
    m_DieAction = None


class CSummonData1024(baseconfig.CSummonData):
    m_SID = 1024
    m_DataSID = 1024
    m_Name = '夜姬丸'
    m_DieAction = SummonDieAction1024


class CSummonData1025(baseconfig.CSummonData):
    m_SID = 1025
    m_DataSID = 1025
    m_Name = '白鲛'
    m_DieAction = None


class CSummonData1026(baseconfig.CSummonData):
    m_SID = 1026
    m_DataSID = 1026
    m_Name = '虚无僧'
    m_DieAction = None


class CSummonData1027(baseconfig.CSummonData):
    m_SID = 1027
    m_DataSID = 1027
    m_Name = '#NT#闪电球'
    m_DieAction = None


class CSummonData1028(baseconfig.CSummonData):
    m_SID = 1028
    m_DataSID = 1028
    m_Name = '风神'
    m_DieAction = SummonDieAction1028


class CSummonData1029(baseconfig.CSummonData):
    m_SID = 1029
    m_DataSID = 1029
    m_Name = '风神'
    m_DieAction = SummonDieAction1029


class CSummonData1030(baseconfig.CSummonData):
    m_SID = 1030
    m_DataSID = 1030
    m_Name = '#NT#海神冰雷'
    m_DieAction = None


class CSummonData1031(baseconfig.CSummonData):
    m_SID = 1031
    m_DataSID = 1031
    m_Name = '#NT#精英纵毒者'
    m_DieAction = None


class CSummonData1032(baseconfig.CSummonData):
    m_SID = 1032
    m_DataSID = 1032
    m_Name = '#NT#精英孵化物'
    m_DieAction = None


class CSummonData1033(baseconfig.CSummonData):
    m_SID = 1033
    m_DataSID = 1033
    m_Name = '#NT#石巨人39091追踪弹'
    m_DieAction = None


class CSummonData1034(baseconfig.CSummonData):
    m_SID = 1034
    m_DataSID = 1034
    m_Name = '#NT#精英敖龙双钳导弹'
    m_DieAction = None


class CSummonData1035(baseconfig.CSummonData):
    m_SID = 1035
    m_DataSID = 1035
    m_Name = '#NT#闪电球plus'
    m_DieAction = None


class CSummonData1036(baseconfig.CSummonData):
    m_SID = 1036
    m_DataSID = 1036
    m_Name = '#NT#精英敖龙加强炮'
    m_DieAction = None


class CSummonData1037(baseconfig.CSummonData):
    m_SID = 1037
    m_DataSID = 1037
    m_Name = '#NT#元素强化-火球'
    m_DieAction = None


class CSummonData1038(baseconfig.CSummonData):
    m_SID = 1038
    m_DataSID = 1038
    m_Name = '#NT#元素强化-毒球'
    m_DieAction = None


class CSummonData1039(baseconfig.CSummonData):
    m_SID = 1039
    m_DataSID = 1039
    m_Name = '#NT#精英河童-三色火球'
    m_DieAction = None


class CSummonData1040(baseconfig.CSummonData):
    m_SID = 1040
    m_DataSID = 1040
    m_Name = '#NT#精英河童-三色毒球'
    m_DieAction = None


class CSummonData1041(baseconfig.CSummonData):
    m_SID = 1041
    m_DataSID = 1041
    m_Name = '#NT#精英河童-三色雷球'
    m_DieAction = None


class CSummonData1042(baseconfig.CSummonData):
    m_SID = 1042
    m_DataSID = 1042
    m_Name = '#NT#精英河童-召唤物法球'
    m_DieAction = None


class CSummonData1043(baseconfig.CSummonData):
    m_SID = 1043
    m_DataSID = 1043
    m_Name = '#NT#瞄准关-普通靶子'
    m_DieAction = None


class CSummonData1044(baseconfig.CSummonData):
    m_SID = 1044
    m_DataSID = 1044
    m_Name = '#NT#卫士-屏障'
    m_DieAction = None


class CSummonData1045(baseconfig.CSummonData):
    m_SID = 1045
    m_DataSID = 1045
    m_Name = '#NT#海怪-小触手'
    m_DieAction = SummonDieAction1045


class CSummonData1046(baseconfig.CSummonData):
    m_SID = 1046
    m_DataSID = 1046
    m_Name = '#NT#卫士-屏障-1'
    m_DieAction = None


class CSummonData1047(baseconfig.CSummonData):
    m_SID = 1047
    m_DataSID = 1047
    m_Name = '#NT#卫士-屏障-2'
    m_DieAction = None


class CSummonData1048(baseconfig.CSummonData):
    m_SID = 1048
    m_DataSID = 1048
    m_Name = '#NT#卫士-屏障-3'
    m_DieAction = None


class CSummonData1049(baseconfig.CSummonData):
    m_SID = 1049
    m_DataSID = 1049
    m_Name = '#NT#卫士-屏障-ex1'
    m_DieAction = None


class CSummonData1050(baseconfig.CSummonData):
    m_SID = 1050
    m_DataSID = 1050
    m_Name = '#NT#卫士-屏障-ex2'
    m_DieAction = None


class CSummonData1051(baseconfig.CSummonData):
    m_SID = 1051
    m_DataSID = 1051
    m_Name = '#NT#卫士-屏障-ex3'
    m_DieAction = None


class CSummonData1052(baseconfig.CSummonData):
    m_SID = 1052
    m_DataSID = 1052
    m_Name = '#NT#卫士-屏障-ex'
    m_DieAction = None


class CSummonData1053(baseconfig.CSummonData):
    m_SID = 1053
    m_DataSID = 1053
    m_Name = '虬蛇'
    m_DieAction = SummonDieAction1053


class CSummonData1055(baseconfig.CSummonData):
    m_SID = 1055
    m_DataSID = 1055
    m_Name = '#NT#精英骑乘-测试子弹'
    m_DieAction = None


class CSummonData1056(baseconfig.CSummonData):
    m_SID = 1056
    m_DataSID = 1057
    m_Name = '#NT#瞄准关-爆炸球'
    m_DieAction = None


class CSummonData1057(baseconfig.CSummonData):
    m_SID = 1057
    m_DataSID = 1058
    m_Name = '#NT#瞄准关-高级靶子'
    m_DieAction = None


class CSummonData1059(baseconfig.CSummonData):
    m_SID = 1059
    m_DataSID = 1059
    m_Name = '#NT#四幕投雷怪鱼雷'
    m_DieAction = None


class CSummonData1060(baseconfig.CSummonData):
    m_SID = 1060
    m_DataSID = 1060
    m_Name = '龙卷风'
    m_DieAction = None


class CSummonData1061(baseconfig.CSummonData):
    m_SID = 1061
    m_DataSID = 1061
    m_Name = '#NT#电镖信标'
    m_DieAction = None


class CSummonData1062(baseconfig.CSummonData):
    m_SID = 1062
    m_DataSID = 1062
    m_Name = '#NT#藏宝室宝石'
    m_DieAction = None


class CSummonData1063(baseconfig.CSummonData):
    m_SID = 1063
    m_DataSID = 1063
    m_Name = '#NT#精英弱点怪冰刃'
    m_DieAction = None


class CSummonData1064(baseconfig.CSummonData):
    m_SID = 1064
    m_DataSID = 1064
    m_Name = '#NT#墨墙'
    m_DieAction = None


class CSummonData1065(baseconfig.CSummonData):
    m_SID = 1065
    m_DataSID = 1065
    m_Name = '#NT#虚化墨墙'
    m_DieAction = None


class CSummonData1066(baseconfig.CSummonData):
    m_SID = 1066
    m_DataSID = 1066
    m_Name = '#NT#妖灵河童元素球'
    m_DieAction = None


class CSummonData1067(baseconfig.CSummonData):
    m_SID = 1067
    m_DataSID = 1067
    m_Name = '妖灵三色火球'
    m_DieAction = None


class CSummonData1068(baseconfig.CSummonData):
    m_SID = 1068
    m_DataSID = 1068
    m_Name = '妖灵三色毒球'
    m_DieAction = None


class CSummonData1069(baseconfig.CSummonData):
    m_SID = 1069
    m_DataSID = 1069
    m_Name = '妖灵三色雷球'
    m_DieAction = None


class CSummonData1070(baseconfig.CSummonData):
    m_SID = 1070
    m_DataSID = 1070
    m_Name = '虚无妖灵僧'
    m_DieAction = None


class CSummonData1071(baseconfig.CSummonData):
    m_SID = 1071
    m_DataSID = 1071
    m_Name = '妖灵剧毒沙蜥召唤物'
    m_DieAction = None


class CSummonData1072(baseconfig.CSummonData):
    m_SID = 1072
    m_DataSID = 1072
    m_Name = '妖灵投射火球'
    m_DieAction = None


class CSummonData1073(baseconfig.CSummonData):
    m_SID = 1073
    m_DataSID = 1073
    m_Name = '妖灵投射雷球'
    m_DieAction = None


class CSummonData1074(baseconfig.CSummonData):
    m_SID = 1074
    m_DataSID = 1074
    m_Name = '首领秘卷-小触手'
    m_DieAction = SummonDieAction1074


class CSummonData1075(baseconfig.CSummonData):
    m_SID = 1075
    m_DataSID = 1075
    m_Name = '首领秘卷-龙卷风'
    m_DieAction = SummonDieAction1075


class CSummonData1076(baseconfig.CSummonData):
    m_SID = 1076
    m_DataSID = 1076
    m_Name = '首领秘卷-夜姬丸水母'
    m_DieAction = SummonDieAction1076


class CSummonData1077(baseconfig.CSummonData):
    m_SID = 1077
    m_DataSID = 1077
    m_Name = '首领秘卷-连城陨石'
    m_DieAction = None


class CSummonData1078(baseconfig.CSummonData):
    m_SID = 1078
    m_DataSID = 1078
    m_Name = '首领秘卷-鱼龙毒球'
    m_DieAction = None


class CSummonData1079(baseconfig.CSummonData):
    m_SID = 1079
    m_DataSID = 1079
    m_Name = '轮回10-石巨人左手'
    m_DieAction = None


class CSummonData1080(baseconfig.CSummonData):
    m_SID = 1080
    m_DataSID = 1080
    m_Name = '轮回10-石巨人右手'
    m_DieAction = None


class CSummonData1081(baseconfig.CSummonData):
    m_SID = 1081
    m_DataSID = 1081
    m_Name = '轮回10-石巨人大陨石'
    m_DieAction = None


class CSummonData1082(baseconfig.CSummonData):
    m_SID = 1082
    m_DataSID = 1082
    m_Name = '#NT#园丁种子'
    m_DieAction = None


class CSummonData1083(baseconfig.CSummonData):
    m_SID = 1083
    m_DataSID = 1083
    m_Name = '#NT#园丁屏障召唤物'
    m_DieAction = None


class CSummonData1084(baseconfig.CSummonData):
    m_SID = 1084
    m_DataSID = 1084
    m_Name = '#NT#第二赛季屏障召唤物'
    m_DieAction = None


class CSummonData1085(baseconfig.CSummonData):
    m_SID = 1085
    m_DataSID = 1085
    m_Name = '#NT#S7毒雾组件召唤物'
    m_DieAction = None


class CSummonData1086(baseconfig.CSummonData):
    m_SID = 1086
    m_DataSID = 1086
    m_Name = '#NT#天袭标枪'
    m_DieAction = None

