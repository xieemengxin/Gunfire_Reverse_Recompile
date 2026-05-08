# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/pfai/pfai33001.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/pfai/pfai33001.pyc
# Source Generated with Decompyle++
# File: pfai33001.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 33001
    m_Name = '【灵界狂潮】精英巡海夜叉（黄金）'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1101: {
            0: [
                31261,
                1,
                1,
                0] },
        1201: {
            0: [
                31262,
                1,
                1,
                0] },
        1003: {
            0: [
                38033,
                1,
                1,
                0] },
        1004: {
            0: [
                38034,
                1,
                1,
                0] },
        1301: {
            0: [
                31263,
                1,
                1,
                0] },
        1401: {
            0: [
                31264,
                1,
                1,
                0] },
        1402: {
            0: [
                31264,
                1,
                1,
                0],
            1: [
                31262,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        31261: [
            1101],
        31262: [
            1201,
            1402],
        38033: [
            1003],
        38034: [
            1004],
        31263: [
            1301],
        31264: [
            1401,
            1402] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: {
            (0, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1003: 10 },
                    'angle': (0, 180) },
                {
                    'choose': {
                        1004: 10 },
                    'angle': (-180, 0) }] },
        MONSTER_PFAI_CATCH: {
            (18, 99, -1, 40, -1, 100, 0): [
                {
                    'choose': {
                        1201: 10,
                        1401: 20 } }],
            (12, 18, -1, 40, -1, 100, 0): [
                {
                    'choose': {
                        1201: 10,
                        1401: 10 } }],
            (8, 12, -1, 40, -1, 100, 0): [
                {
                    'choose': {
                        1201: 10,
                        1402: 10 } }],
            (4, 8, -1, 40, -1, 100, 0): [
                {
                    'choose': {
                        1201: 10,
                        1301: 10 } }],
            (0, 4, -1, 40, -1, 100, 0): [
                {
                    'choose': {
                        1101: 10,
                        1201: 10 } }],
            (18, 99, 40, 70, -1, 100, 0): [
                {
                    'choose': {
                        1201: 10 } }],
            (12, 18, 40, 70, -1, 100, 0): [
                {
                    'choose': {
                        1201: 10 } }],
            (8, 12, 40, 70, -1, 100, 0): [
                {
                    'choose': {
                        1201: 5,
                        1301: 10 } }],
            (4, 8, 40, 70, -1, 100, 0): [
                {
                    'choose': {
                        1201: 5,
                        1301: 10 } }],
            (0, 4, 40, 70, -1, 100, 0): [
                {
                    'choose': {
                        1101: 10 } }],
            (18, 99, 70, 100, -1, 100, 0): [
                {
                    'choose': {
                        1101: 10 } }],
            (12, 18, 70, 100, -1, 100, 0): [
                {
                    'choose': {
                        1101: 10 } }],
            (8, 12, 70, 100, -1, 100, 0): [
                {
                    'choose': {
                        1101: 10 } }],
            (4, 8, 70, 100, -1, 100, 0): [
                {
                    'choose': {
                        1101: 10 } }],
            (0, 4, 70, 100, -1, 100, 0): [
                {
                    'choose': {
                        1101: 10 } }] } }
    m_CheckPFCanUse = { }
    m_PFGroupCheck = {
        1101: PF_GROUP_CHECK_FIRST,
        1201: PF_GROUP_CHECK_FIRST,
        1003: PF_GROUP_CHECK_FIRST,
        1004: PF_GROUP_CHECK_FIRST,
        1301: PF_GROUP_CHECK_FIRST,
        1401: PF_GROUP_CHECK_FIRST,
        1402: PF_GROUP_CHECK_FIRST }

