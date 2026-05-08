# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/pfai/pfai39054.pyc
# RelativePath: clientlogic/cl_platformdata/pc/pfai/pfai39054.pyc
# Source Generated with Decompyle++
# File: pfai39054.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_ALL, PF_GROUP_CHECK_FIRST

def Condition39051(oOwner, dInfo):
    if not oOwner.Phase() == 3:
        pass
    return oOwner.Phase() == 5


def Condition39054(oOwner, dInfo):
    if not oOwner.Phase() == 5:
        pass
    return oOwner.Phase() == 7


def Condition39056(oOwner, dInfo):
    if not oOwner.Phase() == 2:
        pass
    return oOwner.Phase() == 4


def Condition39057(oOwner, dInfo):
    if not oOwner.Phase() == 6:
        pass
    return oOwner.Phase() == 7


def Condition39060(oOwner, dInfo):
    if not oOwner.Phase() == 3:
        pass
    return oOwner.Phase() == 1


def Condition39066(oOwner, dInfo):
    if oOwner.Phase() == 4 or oOwner.Phase() == 6:
        pass
    return cl_condition.GetMonsterSummonCnt(oOwner, dInfo, 0) <= 0 + cl_condition.GetRound(oOwner) + cl_condition.GetGamePlayerCnt(oOwner) + cl_condition.GetGamePlayerCnt(oOwner)


def Condition39068(oOwner, dInfo):
    return oOwner.Phase() >= 6


def Condition39054_3_10(oOwner, dInfo):
    if not oOwner.Phase() == 5 or oOwner.Phase() == 7:
        pass
    return cl_condition.AIConGetCustomData(oOwner, 'EnablePf39054')


class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 39054
    m_Name = '<组队>BOSS海船'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        39051: {
            0: [
                39051,
                1,
                1,
                0] },
        39054: {
            0: [
                39054,
                2,
                2,
                0] },
        39056: {
            0: [
                39056,
                1,
                1,
                0] },
        39057: {
            0: [
                39057,
                1,
                2,
                0] },
        39060: {
            0: [
                39060,
                1,
                2,
                0] },
        39055: {
            0: [
                39054,
                2,
                2,
                0] },
        39061: {
            0: [
                39060,
                2,
                4,
                0] },
        39066: {
            0: [
                39066,
                3,
                3,
                0] },
        39067: {
            0: [
                39066,
                4,
                4,
                0] },
        39058: {
            0: [
                39057,
                2,
                3,
                0] },
        39071: {
            0: [
                39057,
                1,
                2,
                0] },
        39074: {
            0: [
                39057,
                2,
                2,
                0],
            1: [
                39054,
                3,
                3,
                40],
            2: [
                39057,
                3,
                3,
                80],
            3: [
                39054,
                3,
                3,
                45] },
        39075: {
            0: [
                39057,
                2,
                2,
                0],
            1: [
                39054,
                3,
                3,
                40],
            2: [
                39057,
                3,
                3,
                80],
            3: [
                39054,
                3,
                3,
                45],
            4: [
                39057,
                1,
                1,
                100],
            5: [
                39068,
                1,
                1,
                65] } }
    m_GroupOfPF = {
        39051: [
            39051],
        39054: [
            39054,
            39055,
            39074,
            39075],
        39056: [
            39056],
        39057: [
            39057,
            39058,
            39071,
            39074,
            39075],
        39060: [
            39060,
            39061],
        39066: [
            39066,
            39067],
        39068: [
            39075] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (0, 99, -1, 100, -1, 100, 7): [
                {
                    'choose': {
                        39071: 1,
                        39067: 1,
                        39074: 150,
                        39075: 150 } }],
            (0, 99, -1, 100, -1, 100, 6): [
                {
                    'choose': {
                        39054: 10,
                        39056: 10,
                        39057: 5 } }],
            (0, 99, -1, 100, -1, 100, 5): [
                {
                    'choose': {
                        39051: 10,
                        39054: 10,
                        39056: 10,
                        39066: 10 } }],
            (0, 99, -1, 100, -1, 100, 4): [
                {
                    'choose': {
                        39051: 10,
                        39054: 10,
                        39056: 10,
                        39066: 10 } }],
            (0, 99, -1, 100, -1, 100, 3): [
                {
                    'choose': {
                        39051: 10,
                        39061: 10,
                        39056: 10 } }],
            (0, 99, -1, 100, -1, 100, 2): [
                {
                    'choose': {
                        39051: 10,
                        39061: 10,
                        39056: 10 } }],
            (0, 99, -1, 100, -1, 100, 1): [
                {
                    'choose': {
                        39060: 10 } }] } }
    m_CheckPFCanUse = {
        39051: Condition39051,
        39054: Condition39054,
        39056: Condition39056,
        39057: Condition39057,
        39060: Condition39060,
        39066: Condition39066,
        39068: Condition39068 }
    m_PFGroupCheck = {
        39051: PF_GROUP_CHECK_FIRST,
        39054: PF_GROUP_CHECK_FIRST,
        39056: PF_GROUP_CHECK_FIRST,
        39057: PF_GROUP_CHECK_FIRST,
        39060: PF_GROUP_CHECK_FIRST,
        39055: PF_GROUP_CHECK_FIRST,
        39061: PF_GROUP_CHECK_FIRST,
        39066: PF_GROUP_CHECK_FIRST,
        39067: PF_GROUP_CHECK_FIRST,
        39058: PF_GROUP_CHECK_FIRST,
        39071: PF_GROUP_CHECK_FIRST,
        39074: PF_GROUP_CHECK_ALL,
        39075: PF_GROUP_CHECK_ALL }
    m_CheckPFCanUseByDifficulty = {
        (3, 10): {
            39054: Condition39054_3_10 } }

