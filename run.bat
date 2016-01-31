@echo off
color 02
title GUI converter
set /p input="Digite o nome do arquivo .ui que sera convertido: "
set /p saida="Digite o nome do arquivo .py de saida: "
C:\Python34\Lib\site-packages\PyQt5\pyuic5 %input% -o %saida%
set /p saida = "Digite enter para sair"