# powershell开启conda
```bash
C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -ExecutionPolicy ByPass -NoExit -Command "& 'd:\anaconda3\shell\condabin\conda-hook.ps1
' ; conda activate 'd:\anaconda3' "
```

# powershell中启动训练
```bash
powershell.exe -ExecutionPolicy Bypass -File .\train_models.ps1
```