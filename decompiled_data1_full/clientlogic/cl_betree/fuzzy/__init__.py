# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betree/fuzzy/__init__.pyc
# RelativePath: clientlogic/cl_betree/fuzzy/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

from .mobject import CFuzzy
from fuzzymodule import *
if 'g_Fuzzy' not in globals():
    g_Fuzzy = { }

def CreateFuzzy(sName):
    if sName not in g_AllFuzzy:
        return None
    if sName not in g_Fuzzy:
        g_Fuzzy[sName] = g_AllFuzzy[sName]()
    return g_Fuzzy[sName]

g_AllFuzzy = {
    'FarCharge': CFarCharge,
    'FarGuerrilla': CFarGuerrilla,
    'FarSquareGuerrilla': CFarSquareGuerrilla,
    'FarHide': CFarHide,
    'GrenadeHide': CGrenadeHide,
    'GrenadeGuerrilla': CGrenadeGuerrilla,
    'OverallCharge': COverallCharge,
    'OverallGuerrilla': COverallGuerrilla,
    'OverallAwait': COverallAwait }
