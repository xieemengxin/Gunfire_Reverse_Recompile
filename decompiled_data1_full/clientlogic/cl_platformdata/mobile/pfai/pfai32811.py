# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/pfai/pfai32811.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/pfai/pfai32811.pyc
# Source Generated with Decompyle++
# File: pfai32811.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

def Condition32811(oOwner, dInfo):
    return cl_condition.GetPerformRecord(oOwner, dInfo, {
        32811: 1 }) <= 1


def Condition32812(oOwner, dInfo):
    return cl_condition.GetPerformRecord(oOwner, dInfo, {
        32811: 1 }) >= 1


def Condition32814(oOwner, dInfo):
    return cl_condition.GetPerformRecord(oOwner, dInfo, {
        32811: 1 }) <= 1


def Condition32815(oOwner, dInfo):
    return cl_condition.GetPerformRecord(oOwner, dInfo, {
        32811: 1 }) >= 1


class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 32811
    m_Name = '【第三幕】精英定点法师怪'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1001: {
            0: [
                32811,
                1,
                1,
                0] },
        1002: {
            0: [
                32812,
                1,
                1,
                0] },
        2001: {
            0: [
                32814,
                1,
                1,
                0],
            1: [
                32811,
                1,
                1,
                0] },
        2002: {
            0: [
                32815,
                1,
                1,
                0],
            1: [
                32812,
                1,
                1,
                0] },
        1003: {
            0: [
                32812,
                1,
                1,
                0] },
        2003: {
            0: [
                32815,
                1,
                1,
                0],
            1: [
                32812,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        32811: [
            1001,
            2001],
        32812: [
            1002,
            2002,
            1003,
            2003],
        32814: [
            2001],
        32815: [
            2002,
            2003] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (20, 99, 0, 100, -1, 100, 0): [
                {
                    'choose': {
                        2001: 10,
                        1002: 10,
                        1003: 0 } }],
            (10, 20, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 10,
                        2002: 10,
                        2003: 0 } }],
            (0, 10, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        2001: 20,
                        2002: 10,
                        2003: 0 } }] } }
    m_CheckPFCanUse = {
        32811: Condition32811,
        32812: Condition32812,
        32814: Condition32814,
        32815: Condition32815 }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1002: PF_GROUP_CHECK_FIRST,
        2001: PF_GROUP_CHECK_FIRST,
        2002: PF_GROUP_CHECK_FIRST,
        1003: PF_GROUP_CHECK_FIRST,
        2003: PF_GROUP_CHECK_FIRST }

