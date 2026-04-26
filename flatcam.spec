# -*- mode: python ; coding: utf-8 -*-
# PyInstaller spec file for FlatCAM macOS app bundle

import os
import sys
from pathlib import Path
from PyInstaller.utils.hooks import collect_data_files, collect_submodules, collect_dynamic_libs

block_cipher = None
vispy_datas = collect_data_files('vispy')
vispy_hiddenimports = collect_submodules('vispy')
rasterio_datas = collect_data_files('rasterio')
rasterio_hiddenimports = collect_submodules('rasterio')
rasterio_binaries = collect_dynamic_libs('rasterio')
language_data_datas = collect_data_files('language_data')
language_data_hiddenimports = collect_submodules('language_data')

a = Analysis(
    ['__main__.py'],
    pathex=['FlatCAM'],
    binaries=rasterio_binaries,
    datas=[
        ('FlatCAM/config', 'config'),
        ('FlatCAM/translate', 'translate'),
        ('FlatCAM/assets', 'assets'),
        ('FlatCAM/tclCommands', 'tclCommands'),
        ('FlatCAM/preprocessors', 'preprocessors'),
        ('FlatCAM/descartes', 'descartes'),
        ('FlatCAM/appGUI/VisPyData', 'appGUI/VisPyData'),
    ] + vispy_datas + rasterio_datas + language_data_datas,
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
        'resources_dark',
        'resources',
    ] + vispy_hiddenimports + rasterio_hiddenimports + language_data_hiddenimports,
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
    [],
    exclude_binaries=True,
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
    COLLECT(
        exe,
        a.binaries,
        a.zipfiles,
        a.datas,
        strip=False,
        upx=True,
        upx_exclude=[],
        name='FlatCAM',
    ),
    name='FlatCAM.app',
    icon=None,
    bundle_identifier='com.flatcam.app',
    info_plist={
        'NSPrincipalClass': 'NSApplication',
        'NSHighResolutionCapable': 'True',
    },
)
