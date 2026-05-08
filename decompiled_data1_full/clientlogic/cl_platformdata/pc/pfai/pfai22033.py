# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/pfai/pfai22033.pyc
# RelativePath: clientlogic/cl_platformdata/pc/pfai/pfai22033.pyc
# Source Generated with Decompyle++
# File: pfai22033.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

def Condition22031(oOwner, dInfo):
    if not cl_condition.AICheckHasState(oOwner, dInfo, 7079):
        pass
    return cl_condition.AICheckHasState(oOwner, dInfo, 7082)


class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 22033
    m_Name = '<三周目>【第三幕】重型远程-火炮怪'
    m_FillBulletData = (22033, 0, 100)
    m_UseBulletPF = (22031,)
    m_PFGroup = {
        1001: {
            0: [
                22031,
                3,
                6,
                0] },
        1101: {
            0: [
                22032,
                1,
                1,
                0] },
        1201: {
            0: [
                22033,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        22031: [
            1001],
        22032: [
            1101],
        22033: [
            1201] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (0, 4, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1101: 10 } }],
            (4, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 10 } }] } }
    m_CheckPFCanUse = {
        22031: Condition22031 }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1101: PF_GROUP_CHECK_FIRST,
        1201: PF_GROUP_CHECK_FIRST }

