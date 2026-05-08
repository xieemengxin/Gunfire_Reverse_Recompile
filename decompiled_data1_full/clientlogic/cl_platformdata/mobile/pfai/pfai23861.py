# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/pfai/pfai23861.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/pfai/pfai23861.pyc
# Source Generated with Decompyle++
# File: pfai23861.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 23861
    m_Name = '飞鸟骑士'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        23861: {
            0: [
                23861,
                1,
                1,
                0] },
        23862: {
            0: [
                23862,
                1,
                1,
                0] },
        23863: {
            0: [
                23863,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        23861: [
            23861],
        23862: [
            23862],
        23863: [
            23863] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (30, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        23861: 10,
                        23863: 30 } }],
            (20, 30, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        23861: 10,
                        23863: 10 } }],
            (12, 20, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        23861: 50,
                        23863: 10 } }],
            (8, 12, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        23861: 50,
                        23862: 40,
                        23863: 10 } }],
            (0, 8, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        23862: 100,
                        23863: 10 } }] } }
    m_CheckPFCanUse = { }
    m_PFGroupCheck = {
        23861: PF_GROUP_CHECK_FIRST,
        23862: PF_GROUP_CHECK_FIRST,
        23863: PF_GROUP_CHECK_FIRST }

