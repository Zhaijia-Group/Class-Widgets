# -*- mode: python ; coding: utf-8 -*-
block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=['.'],
    binaries=[],
    datas=[
        ('*.ui', '.'),
        ('./audio/*', 'audio'),
        ('./config/**/*', 'config'),
        ('./img/**/*', 'img'),
        ('./ui/**/*', 'ui'),
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    cipher=block_cipher,
    noarchive=False
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='ClassManager',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,  # Set this to True if you want a console window for debugging
    icon='img/favicon.ico',
    onefile=False  # This ensures the output is a directory with the executable inside
)
