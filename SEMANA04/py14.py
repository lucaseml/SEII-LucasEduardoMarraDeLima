#Lucas Eduardo Marra de Lima

import os

os.chdir('/home/lucas/Documents/SEII-LucasEduardoMarraDeLima/SEMANA04')

for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    print(file_name, file_ext)
    print( file_name.split('y'))