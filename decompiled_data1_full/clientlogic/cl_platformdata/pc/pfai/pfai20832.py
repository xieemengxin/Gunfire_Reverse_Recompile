# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/pfai/pfai20832.pyc
# RelativePath: clientlogic/cl_platformdata/pc/pfai/pfai20832.pyc
# Source Generated with Decompyle++
# File: pfai20832.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

def Condition20831(oOwner, dInfo):
    return cl_condition.GetWinkDisSubTargetDis(oOwner, dInfo) <= 0.5


class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 20832
    m_Name = '<二周目>小型近战-持矛近战怪'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1001: {
            0: [
                20832,
                1,
                1,
                0] },
        1002: {
            0: [
                38021,
                1,
                1,
                0] },
        1003: {
            0: [
                38022,
                1,
                1,
                0] },
        1004: {
            0: [
                20831,
                1,
                1,
                0] },
        1005: {
            0: [
                20834,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        20832: [
            1001],
        38021: [
            1002],
        38022: [
            1003],
        20831: [
            1004],
        20834: [
            1005] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: {
            (0, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1002: 10 },
                    'angle': (0, 180) },
                {
                    'choose': {
                        1003: 10 },
                    'angle': (-180, 0) }] },
        MONSTER_PFAI_CATCH: {
            (0, 8, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 15,
                        1005: 15,
                        1004: 10 } }],
            (8, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1004: 15,
                        1005: 15 } }] } }
    m_CheckPFCanUse = {
        20831: Condition20831 }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1002: PF_GROUP_CHECK_FIRST,
        1003: PF_GROUP_CHECK_FIRST,
        1004: PF_GROUP_CHECK_FIRST,
        1005: PF_GROUP_CHECK_FIRST }

