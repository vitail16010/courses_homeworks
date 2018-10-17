import os
file_name = os.path.basename(__file__)
with open(file=file_name, mode="r") as f:
    print(f.read())
