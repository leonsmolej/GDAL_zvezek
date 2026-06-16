
import os

input_dir = r"E:\SLRM_normalised"

output_dir=r"X:\SLRM_ADAF_TRENING"

command_string = r'python C:\Users\Leon\anaconda3\envs\gdal\Scripts\gdal_calc.py -A {input} --outfile={output} --calc="numpy.nan_to_num(A, nan=0)" --NoDataValue=0'
for file in os.listdir(input_dir):
  if file.endswith('.tif'):
    input = os.path.join(input_dir, file)
    filename = os.path.splitext(os.path.basename(file))[0]+"_NaN_0" #split text ti loči ime od končnice, in pol z [0] zberemo ime iz lista. Tle sem dodal nan_0 ker sem nazadnje za to uporabil skript.
    output =  os.path.join(output_dir, filename + '.tif')
    command = command_string.format(input=input, output=output)
    print('Running ->', command)
    print(f"Input: {input}")
    print(f"Output:{output}")
    os.system(command) # s tem se zaštarta komanda