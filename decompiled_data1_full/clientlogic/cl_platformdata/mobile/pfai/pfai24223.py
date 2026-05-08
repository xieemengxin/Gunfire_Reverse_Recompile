# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/pfai/pfai24223.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/pfai/pfai24223.pyc
# Source Generated with Decompyle++
# File: pfai24223.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 24223
    m_Name = '<三周目>蜘蛛猎手'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1101: {
            0: [
                24221,
                1,
                1,
                0] },
        1201: {
            0: [
                24222,
                1,
                1,
                0] },
        1301: {
            0: [
                24223,
                1,
                1,
                0] },
        1303: {
            0: [
                24223,
                1,
                1,
                0],
            1: [
                24222,
                1,
                1,
                12] } }
    m_GroupOfPF = {
        24221: [
            1101],
        24222: [
            1201,
            1303],
        24223: [
            1301,
            1303] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (20, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1301: 50,
                        1303: 50 } }],
            (10, 20, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1201: 30,
                        1301: 50,
                        1303: 20 } }],
            (5, 10, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1101: 20,
                        1201: 50,
                        1301: 30 } }],
            (0, 5, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1101: 80,
                        1201: 20 } }] } }
    m_CheckPFCanUse = { }
    m_PFGroupCheck = {
        1101: PF_GROUP_CHECK_FIRST,
        1201: PF_GROUP_CHECK_FIRST,
        1301: PF_GROUP_CHECK_FIRST,
        1303: PF_GROUP_CHECK_FIRST }

