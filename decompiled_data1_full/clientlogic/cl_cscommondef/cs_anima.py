# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_cscommondef/cs_anima.pyc
# RelativePath: clientlogic/cl_cscommondef/cs_anima.pyc
# Source Generated with Decompyle++
# File: cs_anima.pyc (Python 3.6)

DEFAULT_KNAPSACK = 1001
MODULE_STATE_UP = 0
MODUEL_STATE_RIGHT = 1
MODULE_STATE_DOWN = 2
MODULE_STATE_LEFT = 3
MODULE_STATE_OLD = 4
LOCK_BLOCK = 0
UNLOCK_BLOCK = 1
g_KnapsackShapeDatas = {
    1001: {
        LOCK_BLOCK: ((1, 0), (2, 0), (1, 1), (2, 1), (1, 2), (0, 1), (0, 2), (-1, 1), (-1, 2), (-2, 1), (-2, 0), (0, -2), (-1, -2), (-2, -1), (1, -1), (2, -1), (1, -2)),
        UNLOCK_BLOCK: ((0, 0), (-1, 0), (-1, -1), (0, -1)),
        'Offset': (2, 2),
        'Height': 5,
        'Width': 5 } }
g_ModuleShapeDatas = {
    1001: {
        'PlaceholderInfo': ((0, 0),) },
    1002: {
        'PlaceholderInfo': ((0, 0), (0, 1)) },
    1003: {
        'PlaceholderInfo': ((0, 0), (0, -1), (-1, 0)) },
    1004: {
        'PlaceholderInfo': ((0, 0), (0, 1), (1, 0), (1, 1)) },
    1005: {
        'PlaceholderInfo': ((0, 0), (1, 0), (2, 0), (-1, 0), (-2, 0)) },
    1006: {
        'PlaceholderInfo': ((0, 0), (1, 0), (-1, 0), (0, 1), (1, 1), (-1, 1)) },
    1007: {
        'PlaceholderInfo': ((0, 0), (0, 1), (0, -1), (-1, 0), (-1, 1), (-1, -1), (1, 0), (1, 1), (1, -1)) } }

def GetKnapsackShapeData(iKnapsackShape):
    if iKnapsackShape not in g_KnapsackShapeDatas:
        return { }
    return g_KnapsackShapeDatas[iKnapsackShape]


def GetModuleShapeData(iShape):
    if iShape not in g_ModuleShapeDatas:
        return { }
    return g_ModuleShapeDatas[iShape]

