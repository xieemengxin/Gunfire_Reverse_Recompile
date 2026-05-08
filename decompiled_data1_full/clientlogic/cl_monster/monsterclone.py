# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_monster/monsterclone.pyc
# RelativePath: clientlogic/cl_monster/monsterclone.pyc
# Source Generated with Decompyle++
# File: monsterclone.pyc (Python 3.6)

import cl_monster.mobject

class CSeaMonsterClone(cl_monster.mobject.CMonster):
    
    def GetPos(self):
        return self.Query('PerformAttackedPos', self.m_Pos)


