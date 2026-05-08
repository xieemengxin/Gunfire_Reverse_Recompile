# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/pfai/pfai24221.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/pfai/pfai24221.pyc
# Source Generated with Decompyle++
# File: pfai24221.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 24221
    m_Name = '<一周目>蜘蛛猎手'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1101: {
            0: [
                24221,
                1,
                1,
                0] },
        1102: {
            0: [
                24222,
                1,
                1,
                0] },
        1103: {
            0: [
                24223,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        24221: [
            1101],
        24222: [
            1102],
        24223: [
            1103] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (10, 20, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1101: 30,
                        1102: 10,
                        1103: 60 } }],
            (5, 10, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1101: 70,
                        1102: 10,
                        1103: 20 } }],
            (0, 5, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1101: 100 } }] } }
    m_CheckPFCanUse = { }
    m_PFGroupCheck = {
        1101: PF_GROUP_CHECK_FIRST,
        1102: PF_GROUP_CHECK_FIRST,
        1103: PF_GROUP_CHECK_FIRST }

