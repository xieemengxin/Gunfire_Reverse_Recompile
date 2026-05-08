# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/pfai/pfai39022.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/pfai/pfai39022.pyc
# Source Generated with Decompyle++
# File: pfai39022.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_ALL, PF_GROUP_CHECK_FIRST

def Condition39030(oOwner, dInfo):
    if oOwner.Phase() == 3:
        pass
    return cl_condition.GetObstacleCnt(oOwner, dInfo, 1185) > 0


def Condition39024(oOwner, dInfo):
    return not cl_condition.AICheckHasState(oOwner, dInfo, 8093)


def Condition39021(oOwner, dInfo):
    return cl_condition.AICheckSelfStateCount(oOwner, 8083, 1)


def Condition39022(oOwner, dInfo):
    return cl_condition.AICheckSelfStateCount(oOwner, 8083, 1)


class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 39022
    m_Name = '【诡谲雪山】boss-罗睺'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1001: {
            0: [
                39021,
                1,
                1,
                0] },
        2001: {
            0: [
                39022,
                1,
                1,
                0] },
        2002: {
            0: [
                39021,
                1,
                1,
                0],
            1: [
                39022,
                1,
                1,
                25],
            2: [
                39021,
                1,
                1,
                25],
            3: [
                39044,
                1,
                1,
                25] },
        3001: {
            0: [
                39023,
                1,
                1,
                0] },
        4001: {
            0: [
                39043,
                1,
                1,
                0] },
        5001: {
            0: [
                39025,
                1,
                1,
                0] },
        6001: {
            0: [
                39026,
                1,
                1,
                0] },
        7001: {
            0: [
                39030,
                1,
                1,
                0] },
        8001: {
            0: [
                39044,
                1,
                1,
                0] },
        4002: {
            0: [
                39043,
                1,
                1,
                0],
            1: [
                39023,
                1,
                1,
                0],
            2: [
                39026,
                1,
                1,
                0] },
        4003: {
            0: [
                39043,
                1,
                1,
                0],
            1: [
                39026,
                1,
                1,
                0] },
        5002: {
            0: [
                39025,
                1,
                1,
                0],
            1: [
                39026,
                1,
                1,
                0],
            2: [
                39021,
                1,
                1,
                0] },
        5003: {
            0: [
                39025,
                1,
                1,
                0],
            1: [
                39022,
                1,
                1,
                0],
            2: [
                39021,
                1,
                1,
                0] },
        5004: {
            0: [
                39025,
                1,
                1,
                0],
            1: [
                39021,
                1,
                1,
                0],
            2: [
                39022,
                1,
                1,
                25],
            3: [
                39021,
                1,
                1,
                25],
            4: [
                39044,
                1,
                1,
                25] },
        5005: {
            0: [
                39025,
                1,
                1,
                0],
            1: [
                39026,
                1,
                1,
                0],
            2: [
                39021,
                1,
                1,
                0],
            3: [
                39022,
                1,
                1,
                25],
            4: [
                39021,
                1,
                1,
                25] },
        3002: {
            0: [
                39023,
                1,
                1,
                0],
            1: [
                39021,
                1,
                1,
                0],
            2: [
                39026,
                1,
                1,
                0] },
        3003: {
            0: [
                39023,
                1,
                1,
                0],
            1: [
                39021,
                1,
                1,
                0],
            2: [
                39022,
                1,
                1,
                25],
            3: [
                39021,
                1,
                1,
                25],
            4: [
                39026,
                1,
                1,
                0] },
        1002: {
            0: [
                39021,
                1,
                1,
                0],
            1: [
                39023,
                1,
                1,
                0],
            2: [
                39022,
                1,
                1,
                0] },
        4004: {
            0: [
                39043,
                1,
                1,
                0],
            1: [
                39023,
                1,
                1,
                0] },
        7002: {
            0: [
                39043,
                1,
                1,
                0],
            1: [
                39030,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        39021: [
            1001,
            2002,
            5002,
            5003,
            5004,
            5005,
            3002,
            3003,
            1002],
        39022: [
            2001,
            2002,
            5003,
            5004,
            5005,
            3003,
            1002],
        39044: [
            2002,
            8001,
            5004],
        39023: [
            3001,
            4002,
            3002,
            3003,
            1002,
            4004],
        39043: [
            4001,
            4002,
            4003,
            4004,
            7002],
        39025: [
            5001,
            5002,
            5003,
            5004,
            5005],
        39026: [
            6001,
            4002,
            4003,
            5002,
            5005,
            3002,
            3003],
        39030: [
            7001,
            7002] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (45, 100, -1, 60, -1, 100, 0): [
                {
                    'choose': {
                        2001: 10,
                        2002: 20,
                        7001: 3000,
                        5002: 10,
                        5001: 10,
                        4004: 20 } }],
            (0, 45, -1, 60, -1, 100, 0): [
                {
                    'choose': {
                        5003: 10,
                        1001: 10,
                        7001: 3000,
                        1002: 10,
                        5001: 10,
                        4004: 20,
                        5004: 0 } }],
            (45, 100, 60, 70, -1, 100, 0): [
                {
                    'choose': {
                        2001: 10,
                        2002: 20,
                        4003: 10,
                        5001: 10,
                        4004: 10,
                        7001: 3000 } }],
            (0, 45, 60, 70, -1, 100, 0): [
                {
                    'choose': {
                        1001: 10,
                        4003: 10,
                        4002: 10,
                        7001: 3000 } }],
            (45, 100, 70, 85, -1, 100, 0): [
                {
                    'choose': {
                        5002: 10,
                        4003: 5,
                        5001: 5,
                        4002: 10,
                        2001: 20,
                        2002: 20,
                        7001: 40,
                        5005: 0 } }],
            (0, 45, 70, 85, -1, 100, 0): [
                {
                    'choose': {
                        5002: 10,
                        4003: 5,
                        5001: 5,
                        4002: 10,
                        1001: 30,
                        4004: 10,
                        7001: 50,
                        3002: 10,
                        5005: 0,
                        3003: 0 } }],
            (0, 100, 85, 100, -1, 100, 0): [
                {
                    'choose': {
                        4002: 5,
                        4003: 5,
                        3001: 15,
                        6001: 15,
                        8001: 10 } }] } }
    m_CheckPFCanUse = {
        39030: Condition39030,
        39024: Condition39024,
        39021: Condition39021,
        39022: Condition39022 }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        2001: PF_GROUP_CHECK_FIRST,
        2002: PF_GROUP_CHECK_ALL,
        3001: PF_GROUP_CHECK_FIRST,
        4001: PF_GROUP_CHECK_FIRST,
        5001: PF_GROUP_CHECK_FIRST,
        6001: PF_GROUP_CHECK_FIRST,
        7001: PF_GROUP_CHECK_FIRST,
        8001: PF_GROUP_CHECK_ALL,
        4002: PF_GROUP_CHECK_FIRST,
        4003: PF_GROUP_CHECK_FIRST,
        5002: PF_GROUP_CHECK_FIRST,
        5003: PF_GROUP_CHECK_FIRST,
        5004: PF_GROUP_CHECK_FIRST,
        5005: PF_GROUP_CHECK_FIRST,
        3002: PF_GROUP_CHECK_FIRST,
        3003: PF_GROUP_CHECK_FIRST,
        1002: PF_GROUP_CHECK_FIRST,
        4004: PF_GROUP_CHECK_FIRST,
        7002: PF_GROUP_CHECK_FIRST }

