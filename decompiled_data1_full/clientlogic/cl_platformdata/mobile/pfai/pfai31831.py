# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/pfai/pfai31831.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/pfai/pfai31831.pyc
# Source Generated with Decompyle++
# File: pfai31831.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

def Condition31831(oOwner, dInfo):
    return oOwner.Phase() == 1


def Condition31832(oOwner, dInfo):
    return oOwner.Phase() == 1


def Condition31833(oOwner, dInfo):
    return oOwner.Phase() == 1


def Condition31834(oOwner, dInfo):
    return oOwner.Phase() == 1


def Condition31836(oOwner, dInfo):
    return oOwner.Phase() >= 2


def Condition31837(oOwner, dInfo):
    return oOwner.Phase() >= 2


def Condition31838(oOwner, dInfo):
    return oOwner.Phase() >= 2


def Condition31839(oOwner, dInfo):
    return oOwner.Phase() >= 2


class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 31831
    m_Name = '【新三幕】精英蟹先锋'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1001: {
            0: [
                31831,
                1,
                1,
                0] },
        1002: {
            0: [
                31832,
                1,
                1,
                0] },
        1003: {
            0: [
                31833,
                1,
                1,
                0] },
        1004: {
            0: [
                31834,
                1,
                1,
                0] },
        2001: {
            0: [
                31836,
                1,
                1,
                0] },
        2002: {
            0: [
                31837,
                1,
                1,
                0] },
        2003: {
            0: [
                31838,
                1,
                1,
                0] },
        2004: {
            0: [
                31839,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        31831: [
            1001],
        31832: [
            1002],
        31833: [
            1003],
        31834: [
            1004],
        31836: [
            2001],
        31837: [
            2002],
        31838: [
            2003],
        31839: [
            2004] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (15, 99, -1, 100, -1, 100, 4): [
                {
                    'choose': {
                        2001: 10,
                        2003: 80,
                        2004: 10 } }],
            (8, 15, -1, 100, -1, 100, 4): [
                {
                    'choose': {
                        2001: 10,
                        2003: 60,
                        2004: 30 } }],
            (0, 8, -1, 100, -1, 100, 4): [
                {
                    'choose': {
                        2001: 30,
                        2002: 30,
                        2004: 10 } }],
            (15, 99, -1, 100, -1, 100, 3): [
                {
                    'choose': {
                        2001: 10,
                        2003: 80,
                        2004: 10 } }],
            (8, 15, -1, 100, -1, 100, 3): [
                {
                    'choose': {
                        2001: 10,
                        2003: 60,
                        2004: 30 } }],
            (0, 8, -1, 100, -1, 100, 3): [
                {
                    'choose': {
                        2001: 30,
                        2002: 30,
                        2004: 10 } }],
            (15, 99, -1, 100, -1, 100, 2): [
                {
                    'choose': {
                        2001: 10,
                        2003: 80,
                        2004: 10 } }],
            (8, 15, -1, 100, -1, 100, 2): [
                {
                    'choose': {
                        2001: 10,
                        2003: 60,
                        2004: 30 } }],
            (0, 8, -1, 100, -1, 100, 2): [
                {
                    'choose': {
                        2001: 30,
                        2002: 30,
                        2004: 10 } }],
            (15, 99, -1, 100, -1, 100, 1): [
                {
                    'choose': {
                        1001: 10,
                        1003: 80,
                        1004: 10 } }],
            (8, 15, -1, 100, -1, 100, 1): [
                {
                    'choose': {
                        1001: 10,
                        1003: 60,
                        1004: 30 } }],
            (0, 8, -1, 100, -1, 100, 1): [
                {
                    'choose': {
                        1001: 30,
                        1002: 30,
                        1004: 10 } }] } }
    m_CheckPFCanUse = {
        31831: Condition31831,
        31832: Condition31832,
        31833: Condition31833,
        31834: Condition31834,
        31836: Condition31836,
        31837: Condition31837,
        31838: Condition31838,
        31839: Condition31839 }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1002: PF_GROUP_CHECK_FIRST,
        1003: PF_GROUP_CHECK_FIRST,
        1004: PF_GROUP_CHECK_FIRST,
        2001: PF_GROUP_CHECK_FIRST,
        2002: PF_GROUP_CHECK_FIRST,
        2003: PF_GROUP_CHECK_FIRST,
        2004: PF_GROUP_CHECK_FIRST }

