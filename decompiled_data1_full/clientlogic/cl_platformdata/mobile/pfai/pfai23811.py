# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/pfai/pfai23811.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/pfai/pfai23811.pyc
# Source Generated with Decompyle++
# File: pfai23811.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

def Condition23811(oOwner, dInfo):
    return oOwner.Phase() == 1


def Condition23812(oOwner, dInfo):
    return oOwner.Phase() == 1


def Condition23813(oOwner, dInfo):
    return oOwner.Phase() == 3


def Condition23814(oOwner, dInfo):
    return oOwner.Phase() == 2


def Condition23815(oOwner, dInfo):
    return oOwner.Phase() == 2


def Condition23819(oOwner, dInfo):
    return oOwner.Phase() == 2


class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 23811
    m_Name = '骑乘怪'
    m_FillBulletData = (23820, 0, 100)
    m_UseBulletPF = (23811, 23813)
    m_PFGroup = {
        23811: {
            0: [
                23811,
                1,
                1,
                0] },
        23812: {
            0: [
                23812,
                1,
                1,
                0] },
        23813: {
            0: [
                23813,
                18,
                20,
                0] },
        23814: {
            0: [
                23814,
                1,
                1,
                0] },
        23815: {
            0: [
                23815,
                1,
                1,
                0] },
        23819: {
            0: [
                23819,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        23811: [
            23811],
        23812: [
            23812],
        23813: [
            23813],
        23814: [
            23814],
        23815: [
            23815],
        23819: [
            23819] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (30, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        23811: 10,
                        23813: 10,
                        23814: 25,
                        23815: 50,
                        23819: 25 } }],
            (20, 30, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        23811: 10,
                        23813: 10,
                        23814: 25,
                        23815: 50,
                        23819: 25 } }],
            (10, 20, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        23811: 10,
                        23813: 10,
                        23814: 20,
                        23815: 60,
                        23819: 20 } }],
            (4, 10, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        23813: 10,
                        23814: 30,
                        23815: 40,
                        23819: 30,
                        23811: 10 } }],
            (0, 4, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        23812: 10,
                        23813: 10,
                        23814: 20,
                        23819: 10,
                        23811: 10 } }] } }
    m_CheckPFCanUse = {
        23811: Condition23811,
        23812: Condition23812,
        23813: Condition23813,
        23814: Condition23814,
        23815: Condition23815,
        23819: Condition23819 }
    m_PFGroupCheck = {
        23811: PF_GROUP_CHECK_FIRST,
        23812: PF_GROUP_CHECK_FIRST,
        23813: PF_GROUP_CHECK_FIRST,
        23814: PF_GROUP_CHECK_FIRST,
        23815: PF_GROUP_CHECK_FIRST,
        23819: PF_GROUP_CHECK_FIRST }

