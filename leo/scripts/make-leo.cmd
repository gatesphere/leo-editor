echo off
cls
rem -a: write all files  (make clean)
call set-repo-dir
cd leo\doc\html

echo.
echo sphinx-build -a (make clean)
echo.
sphinx-build -M html . _build -a
