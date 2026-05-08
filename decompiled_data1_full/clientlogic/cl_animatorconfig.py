# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_animatorconfig.pyc
# RelativePath: clientlogic/cl_animatorconfig.pyc
# Source Generated with Decompyle++
# File: cl_animatorconfig.pyc (Python 3.6)

g_AnimatorConfig = {
    1001: ('圈未被占领', 1, 'reset', 0),
    1002: ('圈被占领中', 1, 'start', 0),
    1003: ('占领真圈表现', 4, 'end', 1),
    1004: ('占领假圈表现', 4, 'end', 0),
    1005: ('灵界狂潮开局圈进入战斗', 1, 'start', 0),
    1006: ('灵界狂潮开局圈移除前特效', 1, 'end', 0) }

def GetAnimatorConfig(iConfig):
    return g_AnimatorConfig[iConfig]

