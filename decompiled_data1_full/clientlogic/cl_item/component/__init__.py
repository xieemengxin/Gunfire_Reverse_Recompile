# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_item/component/__init__.pyc
# RelativePath: clientlogic/cl_item/component/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

if 'g_ComponentClass' not in globals():
    g_ComponentClass = { }

def InitComponent():
    global g_ComponentClass
    from . import combullet
    from . import comhold
    from . import comperform
    from . import comspoolup
    from . import comsnipe
    from . import cominscription
    from . import comenhance
    g_ComponentClass = {
        'Bullet': combullet.CBulletComponent,
        'Hold': comhold.CHoldComponent,
        'Perform': comperform.CPerformComponent,
        'Spoolup': comspoolup.CSpoolupCompontent,
        'Snipe': comsnipe.CSnipeComponent,
        'Inscription': cominscription.CInscriptionComponent,
        'Enhance': comenhance.CEnhanceComponent }

InitComponent()

def CreateItemComponent(oItem, sCom, dParser):
    if sCom not in g_ComponentClass:
        return None
    cls = g_ComponentClass[sCom]
    return cls(oItem, dParser)

