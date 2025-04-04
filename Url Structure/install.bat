@echo off
REM Python gerekli kütüphaneleri yükleyen batch dosyası
echo Gerekli Python kütüphaneleri yükleniyor...
echo.

REM Python'un kurulu olduğunu kontrol et
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Hata: Python kurulu değil veya PATH'te yok!
    pause
    exit /b
)

REM Pip'in güncel olduğundan emin ol
python -m pip install --upgrade pip

REM Kütüphaneleri yükle
pip install requests beautifulsoup4 anytree

echo.
echo Kütüphaneler başarıyla yüklendi!
echo Programı çalıştırmak için: python main.py
pause