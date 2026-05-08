# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/pfai/pfai34212.pyc
# RelativePath: clientlogic/cl_platformdata/pc/pfai/pfai34212.pyc
# Source Generated with Decompyle++
# File: pfai34212.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

def Condition34214(oOwner, dInfo):
    return cl_condition.CheckTopObstacleDis(oOwner, 5)


class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 34212
    m_Name = '<二周目>精英蜘蛛猎手'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1001: {
            0: [
                34211,
                1,
                1,
                0] },
        1003: {
            0: [
                34212,
                1,
                1,
                0] },
        1004: {
            0: [
                34213,
                1,
                1,
                0] },
        1005: {
            0: [
                34214,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        34211: [
            1001],
        34212: [
            1003],
        34213: [
            1004],
        34214: [
            1005] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (15, 99, -1, 100, -1, 50, 0): [
                {
                    'choose': {
                        1003: 10,
                        1004: 10,
                        1005: 100 } }],
            (10, 15, -1, 100, -1, 50, 0): [
                {
                    'choose': {
                        1003: 10,
                        1004: 10,
                        1005: 100 } }],
            (5, 10, -1, 100, -1, 50, 0): [
                {
                    'choose': {
                        1001: 10,
                        1004: 30,
                        1005: 100 } }],
            (0, 5, -1, 100, -1, 50, 0): [
                {
                    'choose': {
                        1001: 100 } }],
            (15, 99, -1, 100, 50, 100, 0): [
                {
                    'choose': {
                        1003: 20,
                        1004: 70,
                        1005: 70 } }],
            (10, 15, -1, 100, 50, 100, 0): [
                {
                    'choose': {
                        1003: 30,
                        1004: 100,
                        1005: 30 } }],
            (5, 10, -1, 100, 50, 100, 0): [
                {
                    'choose': {
                        1003: 50,
                        1004: 100 } }],
            (0, 5, -1, 100, 50, 100, 0): [
                {
                    'choose': {
                        1001: 100 } }] } }
    m_CheckPFCanUse = {
        34214: Condition34214 }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1003: PF_GROUP_CHECK_FIRST,
        1004: PF_GROUP_CHECK_FIRST,
        1005: PF_GROUP_CHECK_FIRST }

