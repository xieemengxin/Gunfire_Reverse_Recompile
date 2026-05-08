# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/pfai/pfai23831.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/pfai/pfai23831.pyc
# Source Generated with Decompyle++
# File: pfai23831.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

def Condition23831(oOwner, dInfo):
    return oOwner.Phase() == 1


def Condition23832(oOwner, dInfo):
    return oOwner.Phase() == 1


def Condition23833(oOwner, dInfo):
    return oOwner.Phase() == 3


def Condition23834(oOwner, dInfo):
    return oOwner.Phase() == 2


def Condition23835(oOwner, dInfo):
    return oOwner.Phase() == 2


class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 23831
    m_Name = '【测试】骑乘怪'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        23831: {
            0: [
                23831,
                1,
                1,
                0] },
        23832: {
            0: [
                23832,
                1,
                1,
                0] },
        23833: {
            0: [
                23833,
                1,
                1,
                0] },
        23834: {
            0: [
                23834,
                1,
                1,
                0] },
        23835: {
            0: [
                23835,
                1,
                1,
                0] },
        1001: {
            0: [
                23831,
                1,
                1,
                0],
            1: [
                23831,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        23831: [
            23831,
            1001],
        23832: [
            23832],
        23833: [
            23833],
        23834: [
            23834],
        23835: [
            23835] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (30, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        23831: 10,
                        23833: 10,
                        23834: 25,
                        23835: 50 } }],
            (20, 30, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 10,
                        23833: 10,
                        23834: 25,
                        23835: 50 } }],
            (10, 20, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 10,
                        23833: 10,
                        23834: 20,
                        23835: 60 } }],
            (4, 10, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 10,
                        23833: 10,
                        23834: 30,
                        23835: 40 } }],
            (0, 4, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        23832: 10,
                        23833: 10,
                        23834: 20 } }] } }
    m_CheckPFCanUse = {
        23831: Condition23831,
        23832: Condition23832,
        23833: Condition23833,
        23834: Condition23834,
        23835: Condition23835 }
    m_PFGroupCheck = {
        23831: PF_GROUP_CHECK_FIRST,
        23832: PF_GROUP_CHECK_FIRST,
        23833: PF_GROUP_CHECK_FIRST,
        23834: PF_GROUP_CHECK_FIRST,
        23835: PF_GROUP_CHECK_FIRST,
        1001: PF_GROUP_CHECK_FIRST }

