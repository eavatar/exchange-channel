# -*- mode: python -*-
# -*- coding: utf-8 -*-

app_path = os.path.join('src', 'eavatar.channel')


exe_name = 'ava-channel'
hiddenimports = []
run_strip = True

ext_name = ''
run_strip = True
hiddenimports.append('depends_linux.py')


a = Analysis([os.path.join(app_path,'server.py')],
             pathex=['src'],
             hiddenimports=hiddenimports,
             hookspath=None,
             runtime_hooks=None,
             excludes=['PyQt4', 'wx', 'django', 'Tkinter', 'gi.repository', 'objc', 'AppKit', 'Foundation'])

run_strip = False


pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.dependencies,
          exclude_binaries=True,
          name=os.path.join('build', 'pyi.'+sys.platform, 'server', exe_name),
          debug=False,
          strip=run_strip,
          upx=True,
          console=True )


coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=run_strip,
               upx=True,
               name=os.path.join('dist', 'ava-channel'))

