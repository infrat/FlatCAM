# -*- mode: python ; coding: utf-8 -*-
# PyInstaller spec file for FlatCAM macOS app bundle

import os
import sys
from pathlib import Path
from PyInstaller.utils.hooks import collect_data_files

block_cipher = None
vispy_datas = collect_data_files('vispy')

a = Analysis(
    ['__main__.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('config', 'config'),
        ('translate', 'translate'),
        ('assets', 'assets'),
        ('tclCommands', 'tclCommands'),
        ('preprocessors', 'preprocessors'),
        ('descartes', 'descartes'),
        ('appGUI/VisPyData', 'appGUI/VisPyData'),
    ] + vispy_datas,
    hiddenimports=[
        'PyQt5',
        'PyQt5.QtCore',
        'PyQt5.QtGui',
        'PyQt5.QtWidgets',
        'PyQt5.QtOpenGL',
        'PyQt5.sip',
        'vispy',
        'vispy.visuals',
        'vispy.scene',
        'vispy.gloo',
        'vispy.io',
        'vispy.color',
        'numpy',
        'scipy',
        'scipy.ndimage',
        'scipy.interpolate',
        'shapely',
        'shapely.geometry',
        'shapely.ops',
        'shapely.affinity',
        'shapely.prepared',
        'svg.path',
        'reportlab',
        'reportlab.pdfgen',
        'reportlab.lib',
        'reportlab.lib.pagesizes',
        'reportlab.lib.units',
        'reportlab.platypus',
        'reportlab.graphics',
        'reportlab.graphics.shapes',
        'plotly',
        'plotly.graph_objects',
        'plotly.io',
        'pandas',
        'matplotlib',
        'matplotlib.backends',
        'matplotlib.backends.backend_agg',
        'PIL',
        'PIL.Image',
        'PIL.ImageChops',
        'PIL.ImageDraw',
        'optuna',
        'optuna.visualization',
        'ezdxf',
        'dxf',
        'simplejson',
        'json',
        'logging',
        'multiprocessing',
        'concurrent.futures',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludedimports=['tcl', 'tk', 'tkinter'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='FlatCAM',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,
)

app = BUNDLE(
    exe,
    name='FlatCAM.app',
    icon=None,
    bundle_identifier='com.flatcam.app',
    info_plist={
        'NSPrincipalClass': 'NSApplication',
        'NSHighResolutionCapable': 'True',
    },
)
