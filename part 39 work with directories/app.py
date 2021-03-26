from pathlib import Path

path = Path()

# To create a path or folder use:
path.mkdir()

# To remove or delete a path use:
path.rmdir()

# To check a path is exists or not use:
path.exists()

# To browse all the files in path use:
for file in path.glob('*.py'):
  print(file)