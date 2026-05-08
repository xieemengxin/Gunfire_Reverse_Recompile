# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/pfai/pfai39133.pyc
# RelativePath: clientlogic/cl_platformdata/pc/pfai/pfai39133.pyc
# Source Generated with Decompyle++
# File: pfai39133.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

def Condition39133(oOwner, dInfo):
    return oOwner.Phase() == 1


def Condition39134(oOwner, dInfo):
    return oOwner.Phase() == 1


def Condition39135(oOwner, dInfo):
    return oOwner.Phase() == 1


def Condition39136(oOwner, dInfo):
    return oOwner.Phase() == 2


def Condition39137(oOwner, dInfo):
    return oOwner.Phase() == 2


def Condition39138(oOwner, dInfo):
    return oOwner.Phase() == 2


class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 39133
    m_Name = '<三周目>boss-第二幕-全身'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1301: {
            0: [
                39133,
                1,
                1,
                0] },
        1401: {
            0: [
                39134,
                1,
                1,
                0] },
        1501: {
            0: [
                39135,
                1,
                1,
                0] },
        2701: {
            0: [
                39137,
                3,
                4,
                0],
            1: [
                39137,
                4,
                4,
                0],
            2: [
                39138,
                1,
                1,
                0] },
        2801: {
            0: [
                39138,
                1,
                1,
                0],
            1: [
                39137,
                4,
                4,
                0],
            2: [
                39138,
                1,
                1,
                0] },
        3301: {
            0: [
                39133,
                1,
                1,
                0],
            1: [
                39134,
                1,
                1,
                0],
            2: [
                39135,
                1,
                1,
                25] },
        3302: {
            0: [
                39133,
                1,
                1,
                0],
            1: [
                39135,
                1,
                1,
                0],
            2: [
                39134,
                1,
                1,
                25] },
        3401: {
            0: [
                39134,
                1,
                1,
                0],
            1: [
                39135,
                1,
                1,
                25] },
        3501: {
            0: [
                39135,
                1,
                1,
                0],
            1: [
                39134,
                1,
                1,
                25] },
        3701: {
            0: [
                39137,
                5,
                6,
                0],
            1: [
                39137,
                6,
                6,
                0],
            2: [
                39138,
                4,
                4,
                0] },
        3801: {
            0: [
                39138,
                3,
                3,
                0],
            1: [
                39137,
                6,
                6,
                0],
            2: [
                39138,
                3,
                3,
                0] } }
    m_GroupOfPF = {
        39133: [
            1301,
            3301,
            3302],
        39134: [
            1401,
            3301,
            3302,
            3401,
            3501],
        39135: [
            1501,
            3301,
            3302,
            3401,
            3501],
        39137: [
            2701,
            2801,
            3701,
            3801],
        39138: [
            2701,
            2801,
            3701,
            3801] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (0, 12, -1, 100, -1, 50, 0): [
                {
                    'choose': {
                        3301: 10,
                        3302: 10,
                        3801: 10 } }],
            (12, 99, -1, 100, -1, 50, 0): [
                {
                    'choose': {
                        3401: 10,
                        3501: 10,
                        3701: 10,
                        3801: 10 } }],
            (0, 12, -1, 100, 50, 100, 0): [
                {
                    'choose': {
                        1301: 10,
                        2801: 10 } }],
            (12, 99, -1, 100, 50, 100, 0): [
                {
                    'choose': {
                        1401: 10,
                        1501: 10,
                        2701: 10,
                        2801: 10 } }] } }
    m_CheckPFCanUse = {
        39133: Condition39133,
        39134: Condition39134,
        39135: Condition39135,
        39136: Condition39136,
        39137: Condition39137,
        39138: Condition39138 }
    m_PFGroupCheck = {
        1301: PF_GROUP_CHECK_FIRST,
        1401: PF_GROUP_CHECK_FIRST,
        1501: PF_GROUP_CHECK_FIRST,
        2701: PF_GROUP_CHECK_FIRST,
        2801: PF_GROUP_CHECK_FIRST,
        3301: PF_GROUP_CHECK_FIRST,
        3302: PF_GROUP_CHECK_FIRST,
        3401: PF_GROUP_CHECK_FIRST,
        3501: PF_GROUP_CHECK_FIRST,
        3701: PF_GROUP_CHECK_FIRST,
        3801: PF_GROUP_CHECK_FIRST }

