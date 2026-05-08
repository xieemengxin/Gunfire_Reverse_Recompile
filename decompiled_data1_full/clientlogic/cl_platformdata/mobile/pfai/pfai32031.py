# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/pfai/pfai32031.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/pfai/pfai32031.pyc
# Source Generated with Decompyle++
# File: pfai32031.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

def Condition32035(oOwner, dInfo):
    if not cl_condition.AICheckHasState(oOwner, dInfo, 7105) or cl_condition.AICheckHasState(oOwner, dInfo, 7106) or cl_condition.AICheckHasState(oOwner, dInfo, 7107):
        pass
    return cl_condition.AICheckHasState(oOwner, dInfo, 7108)


def Condition32031(oOwner, dInfo):
    if cl_condition.AICheckHasState(oOwner, dInfo, 7103):
        pass
    return cl_condition.AICheckHasState(oOwner, dInfo, 7104)


def Condition32033(oOwner, dInfo):
    if cl_condition.AICheckHasState(oOwner, dInfo, 7103):
        pass
    return cl_condition.AICheckHasState(oOwner, dInfo, 7104)


class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 32031
    m_Name = '【第三幕】精英火箭兵'
    m_FillBulletData = (32033, 0, 100)
    m_UseBulletPF = (32031,)
    m_PFGroup = {
        1101: {
            0: [
                32031,
                1,
                1,
                0] },
        1201: {
            0: [
                32032,
                1,
                1,
                0] },
        1301: {
            0: [
                32033,
                1,
                1,
                0] },
        1501: {
            0: [
                32035,
                25,
                30,
                0] } }
    m_GroupOfPF = {
        32031: [
            1101],
        32032: [
            1201],
        32033: [
            1301],
        32035: [
            1501] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (0, 4, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1201: 10,
                        1101: 10 } }],
            (4, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1101: 10,
                        1501: 10 } }] } }
    m_CheckPFCanUse = {
        32035: Condition32035,
        32031: Condition32031,
        32033: Condition32033 }
    m_PFGroupCheck = {
        1101: PF_GROUP_CHECK_FIRST,
        1201: PF_GROUP_CHECK_FIRST,
        1301: PF_GROUP_CHECK_FIRST,
        1501: PF_GROUP_CHECK_FIRST }

