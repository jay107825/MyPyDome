import PyInstaller.__main__ as pyi

pyi.run([
    'puit.py',
    '--onefile',
    '--name=exit_tq',
    '--clean',
    '--noconfirm',
])
