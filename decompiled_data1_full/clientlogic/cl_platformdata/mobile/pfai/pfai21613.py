# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/pfai/pfai21613.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/pfai/pfai21613.pyc
# Source Generated with Decompyle++
# File: pfai21613.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 21613
    m_Name = '<三周目>狙击怪-追踪狙击怪'
    m_FillBulletData = (38016, 3, 33)
    m_UseBulletPF = (21611,)
    m_PFGroup = {
        1001: {
            0: [
                21611,
                3,
                3,
                0] },
        1002: {
            0: [
                21612,
                1,
                1,
                0] },
        1003: {
            0: [
                21621,
                1,
                1,
                0] },
        1004: {
            0: [
                21611,
                3,
                5,
                0] },
        1005: {
            0: [
                21611,
                4,
                6,
                0] },
        1006: {
            0: [
                38016,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        21611: [
            1001,
            1004,
            1005],
        21612: [
            1002],
        21621: [
            1003],
        38016: [
            1006] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (20, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1004: 40,
                        1005: 60 } }],
            (10, 20, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 20,
                        1004: 50,
                        1005: 30 } }],
            (4, 10, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 50,
                        1004: 40,
                        1005: 10 } }],
            (0, 4, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1002: 10 } }] } }
    m_CheckPFCanUse = { }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1002: PF_GROUP_CHECK_FIRST,
        1003: PF_GROUP_CHECK_FIRST,
        1004: PF_GROUP_CHECK_FIRST,
        1005: PF_GROUP_CHECK_FIRST,
        1006: PF_GROUP_CHECK_FIRST }

