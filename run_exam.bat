@echo off
chcp 65001 >nul
title Examen PyQt6 - Launcher

echo.
echo ========================================
echo 🎓 EXAMEN PYQT6 - PARTIE 1
echo ========================================
echo.

REM Vérifier si Python est installé
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ❌ Python n'est pas installé ou pas dans le PATH
    echo Veuillez installer Python 3.8+ depuis https://python.org
    pause
    exit /b 1
)

REM Lancer le script d'installation et l'application
python setup.py

echo.
echo 📝 Pour relancer l'application manuellement :
echo    1. Activez l'environnement : .\env\Scripts\activate
echo    2. Lancez l'app : python main.py
echo.

pause 