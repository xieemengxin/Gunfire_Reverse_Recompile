# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/pfai/pfai20211.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/pfai/pfai20211.pyc
# Source Generated with Decompyle++
# File: pfai20211.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import FIGHT_LOGIC_DEFAULT, FIGHT_LOGIC_OVERALLCHARGE, FIGHT_LOGIC_OVERALLGUERRILLA, MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

def Condition20212(oOwner, dInfo):
    if not cl_condition.JudgeAIFightLogicType(oOwner, dInfo, FIGHT_LOGIC_OVERALLCHARGE):
        pass
    return cl_condition.JudgeAIFightLogicType(oOwner, dInfo, FIGHT_LOGIC_DEFAULT)


def Condition20211(oOwner, dInfo):
    if not cl_condition.JudgeAIFightLogicType(oOwner, dInfo, FIGHT_LOGIC_OVERALLGUERRILLA):
        pass
    return cl_condition.JudgeAIFightLogicType(oOwner, dInfo, FIGHT_LOGIC_DEFAULT)


class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 20211
    m_Name = '四足兽'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1001: {
            0: [
                20211,
                1,
                1,
                0] },
        1002: {
            0: [
                20212,
                1,
                1,
                0] },
        1003: {
            0: [
                20213,
                1,
                1,
                0] },
        1004: {
            0: [
                38028,
                1,
                1,
                0] },
        1005: {
            0: [
                38029,
                1,
                1,
                0] },
        1006: {
            0: [
                20211,
                1,
                1,
                0],
            1: [
                20211,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        20211: [
            1001,
            1006],
        20212: [
            1002],
        20213: [
            1003],
        38028: [
            1004],
        38029: [
            1005] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: {
            (0, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1004: 10 },
                    'angle': (0, 180) },
                {
                    'choose': {
                        1005: 10 },
                    'angle': (-180, 0) }] },
        MONSTER_PFAI_CATCH: {
            (0, 4, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1003: 100 } }],
            (4, 8, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1002: 50,
                        1003: 50 } }],
            (8, 14, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 70,
                        1006: 30 } }],
            (14, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 70,
                        1006: 30 } }] } }
    m_CheckPFCanUse = {
        20212: Condition20212,
        20211: Condition20211 }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1002: PF_GROUP_CHECK_FIRST,
        1003: PF_GROUP_CHECK_FIRST,
        1004: PF_GROUP_CHECK_FIRST,
        1005: PF_GROUP_CHECK_FIRST,
        1006: PF_GROUP_CHECK_FIRST }

