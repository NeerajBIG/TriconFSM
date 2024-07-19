@echo off
call C:\Users\neera\PycharmProjects\TriconFSM\.venv\Scripts\activate.bat
pytest -v -s -m "sanity or regression"  --html=Reports/report.html testCases/
pause