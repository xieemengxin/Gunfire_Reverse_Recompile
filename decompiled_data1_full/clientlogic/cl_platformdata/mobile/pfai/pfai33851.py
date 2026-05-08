# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/pfai/pfai33851.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/pfai/pfai33851.pyc
# Source Generated with Decompyle++
# File: pfai33851.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 33851
    m_Name = '精英骑乘怪坐骑-轮回10'
    m_FillBulletData = ()
    m_UseBulletPF = ()
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
                        23814: 25,
                        23815: 50,
                        23819: 25 } }],
            (20, 30, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        23814: 25,
                        23815: 50,
                        23819: 25 } }],
            (10, 20, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        23814: 20,
                        23815: 60,
                        23819: 20 } }],
            (4, 10, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        23815: 40,
                        23819: 30 } }],
            (0, 4, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        23814: 20,
                        23819: 10 } }] } }
    m_CheckPFCanUse = { }
    m_PFGroupCheck = {
        23811: PF_GROUP_CHECK_FIRST,
        23812: PF_GROUP_CHECK_FIRST,
        23813: PF_GROUP_CHECK_FIRST,
        23814: PF_GROUP_CHECK_FIRST,
        23815: PF_GROUP_CHECK_FIRST,
        23819: PF_GROUP_CHECK_FIRST }

