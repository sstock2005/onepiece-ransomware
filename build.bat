@ECHO OFF
TITLE BUILDER
pyinstaller --name king_of_the_pirates --uac-admin --console --hide-console hide-early --onefile main.py --clean --disable-windowed-traceback --i flag.ico