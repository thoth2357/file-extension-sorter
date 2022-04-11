import os, shutil
from pathlib import Path
import time

storage_directory = os.path.join(Path.home(), 'Documents')
directory = "/home/pirate/Documents/Test_folder"
# print(os.walk(directory)
for i in os.walk(directory):
    # print(i[0])
    for file in i[2]:
        directory_file = i[0]
        extension = file.split('.')[1]
        try:
            # print(file)

            extension_folder = os.path.join(storage_directory, f'arranged_folder/{extension}')
            try:
                os.makedirs(extension_folder)
            except FileExistsError:
                if Path(os.path.join(extension_folder, file)).is_file():
                    duplicate_folder = os.path.join(extension_folder, 'Duplicates')
                    try:
                        os.makedirs(duplicate_folder)
                        shutil.move(os.path.join(directory_file, file), duplicate_folder)
                    except FileExistsError:
                        try:
                            shutil.move(os.path.join(directory_file, file), duplicate_folder)
                        except Exception:
                            time_ = time.time()
                            os.rename(os.path.join(directory_file, file), os.path.join(directory_file, f"{file}__{time_}"))
                            shutil.move(os.path.join(directory_file, f"{file}__{time_}"), duplicate_folder)

                else:
                    shutil.move(os.path.join(directory_file, file), extension_folder)
        except FileExistsError:
            if Path(os.path.join(extension_folder, file)).is_file():
                duplicate_folder = os.path.join(extension_folder, 'Duplicates')
                try:
                    os.makedirs(duplicate_folder)
                    shutil.move(os.path.join(directory_file, file), duplicate_folder)
                except FileExistsError:
                    try:
                        shutil.move(os.path.join(directory_file, file), duplicate_folder)
                    except Exception:
                        time_ = time.time()
                        os.rename(os.path.join(directory_file, file), os.path.join(directory_file, f"{file}__{time_}"))
                        shutil.move(os.path.join(directory_file, f"{file}__{time_}"), duplicate_folder)
            else:
                shutil.move(os.path.join(directory_file, file), extension_folder)
            

            