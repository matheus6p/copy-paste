import os

DePasta = "C:\\pastaA" #pasta origem
ParaPasta = "C:\\pastaB" #pasta destino

if os.path.isdir(ParaPasta + "\\build"):
  os.rmdir(ParaPasta + "\\build")
  os.replace((DePasta + "\\build"), (ParaPasta + "\\build"))
else:
  os.replace((DePasta + "\\build"), (ParaPasta + "\\build"))
