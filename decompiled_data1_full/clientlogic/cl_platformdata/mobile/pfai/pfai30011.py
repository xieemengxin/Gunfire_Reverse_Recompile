# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/pfai/pfai30011.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/pfai/pfai30011.pyc
# Source Generated with Decompyle++
# File: pfai30011.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

def Condition30012(oOwner, dInfo):
    return cl_condition.GetSceneAliveMonsterCnt(oOwner, dInfo, 20013) <= 20


class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 30011
    m_Name = '【第一幕】精英一刀怪'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1101: {
            0: [
                30011,
                1,
                1,
                0] },
        1102: {
            0: [
                30011,
                1,
                1,
                0],
            1: [
                30011,
                1,
                1,
                0] },
        1103: {
            0: [
                30011,
                1,
                1,
                0],
            1: [
                30011,
                1,
                1,
                0],
            2: [
                30011,
                1,
                1,
                0],
            3: [
                30012,
                1,
                1,
                0] },
        1201: {
            0: [
                30012,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        30011: [
            1101,
            1102,
            1103],
        30012: [
            1103,
            1201] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (20, 99, -1, 100, -1, 25, 0): [
                {
                    'choose': {
                        1201: 20 } }],
            (15, 20, -1, 100, -1, 25, 0): [
                {
                    'choose': {
                        1103: 10,
                        1201: 10 } }],
            (10, 15, -1, 100, -1, 25, 0): [
                {
                    'choose': {
                        1103: 10 } }],
            (5, 10, -1, 100, -1, 25, 0): [
                {
                    'choose': {
                        1103: 10 } }],
            (0, 5, -1, 100, -1, 25, 0): [
                {
                    'choose': {
                        1101: 10,
                        1102: 10 } }],
            (20, 99, -1, 100, 25, 50, 0): [
                {
                    'choose': {
                        1201: 20 } }],
            (15, 20, -1, 100, 25, 50, 0): [
                {
                    'choose': {
                        1102: 10,
                        1201: 10 } }],
            (10, 15, -1, 100, 25, 50, 0): [
                {
                    'choose': {
                        1102: 10,
                        1201: 10 } }],
            (5, 10, -1, 100, 25, 50, 0): [
                {
                    'choose': {
                        1102: 10 } }],
            (0, 5, -1, 100, 25, 50, 0): [
                {
                    'choose': {
                        1101: 10 } }],
            (20, 99, -1, 100, 50, 100, 0): [
                {
                    'choose': {
                        1201: 20 } }],
            (15, 20, -1, 100, 50, 100, 0): [
                {
                    'choose': {
                        1101: 10,
                        1201: 30 } }],
            (10, 15, -1, 100, 50, 100, 0): [
                {
                    'choose': {
                        1101: 10,
                        1201: 10 } }],
            (5, 10, -1, 100, 50, 100, 0): [
                {
                    'choose': {
                        1101: 30,
                        1201: 10 } }],
            (0, 5, -1, 100, 50, 100, 0): [
                {
                    'choose': {
                        1101: 10 } }] } }
    m_CheckPFCanUse = {
        30012: Condition30012 }
    m_PFGroupCheck = {
        1101: PF_GROUP_CHECK_FIRST,
        1102: PF_GROUP_CHECK_FIRST,
        1103: PF_GROUP_CHECK_FIRST,
        1201: PF_GROUP_CHECK_FIRST }

