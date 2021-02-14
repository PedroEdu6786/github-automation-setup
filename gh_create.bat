SET my_path=%~dp0
SET project=%1
cls
python "%my_path%app.py" %project%