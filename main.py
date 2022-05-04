try:
    import os, shutil
    import time
    from pathlib import Path
    from tkinter import filedialog
    from tkinter import *
except Exception:
    try:
        os.system('pip install -r requirements.txt')
        from tkinter import filedialog
        from tkinter import *
    except Exception:
        print('Issue with requirements file')

try:
    root = Tk()
    root.withdraw()
    storage_directory = os.path.join(Path.home(), 'Documents')
    directory = filedialog.askdirectory()
except Exception:
    print('Module tkinter not installed')
    quit()


for i in os.walk(directory):
    # print('dir',i[0])
    # print(any([end_path.startswith('.') for end_path in i[0].split('/')]))
    if any([end_path.startswith('.') for end_path in i[0].split('/')]) == False:
        for file in i[2]:
            # print(file)
            directory_file = i[0]
            extension = file.split('.')[1]
            # print('new', extension)
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
        

print(f'{directory} contents has been sorted into different folders based on their extension type. check documents folder')