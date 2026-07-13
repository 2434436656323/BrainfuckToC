# BrainfuckToC
Brainfuck To C (BF2C) программа на пайтоне позваляющая конвертировать Brainfuck в чистый C код.
Нужно:
Python 3.X,
MinGW64,
Windows CMD.

Как использовать:
1. Переместите файл bf2c.py в корневую папку MinGW64 и создайте файл .bf .
2. Пропишите type filename.bf | python bf2c.py > filename.c .
3. Компиляция прописываем в cmd bin\gcc.exe -o filename.exe filename.c .
4. Запуск просто пропишите filename.exe .
