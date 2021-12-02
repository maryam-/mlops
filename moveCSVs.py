import os
from glob import glob
data_dirs = ["Training_Batch_Files","Prediction_Batch_files"]
for data_dir in data_dirs:
    files = glob(data_dir + r"/*.csv")
    for filePath in files:
        os.system(f"dvc add {filePath}")
print("\n #### all files added to dvc ####\n")