# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['cli.py'],
             binaries=[],
             datas=[('README.md', '.'),
                    ('icons/python_icon.ico', 'icons')],
             hiddenimports=['pkg_resources'],
             hookspath=[],
             runtime_hooks=[],
             excludes=['test'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='ProjectExplorer',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='ProjectExplorer')
