#!/bin/sh
echo $(pwd)
python pack/pyinstaller/pyinstaller.py pack/package.spec --clean -y


