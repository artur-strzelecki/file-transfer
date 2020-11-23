import glob
import os
import time

# path
path_download = 'your_download_path'
path_doc = 'C:/Download/Documents/'
path_img = 'C:/Download/Images/'
path_exe = 'C:/Download/Exe/'
path_audio = 'C:/Download/Audio/'
path_video = 'C:/Download/Video/'
path_zip = 'C:/Download/Zip/'
path_cd_image = 'C:/Download/System images/'
path_script = 'C:/Download/Scripts/'

# extension 
type_doc = ['.TXT', '.DOC', '.DOCX', '.DOCM', '.ODT', '.PDF', '.CSV', '.XLS', '.XLSX', '.XLSM', '.ODS', '.PPS', '.PPT', '.PPSX', '.PPTX', '.POTX', '.ODP']
type_img = ['.JPEG', '.JPG', '.PNG', '.BMP', '.ICO', '.SVG', '.WEBP', '.GIF', '.PSD', '.HEIC', '.NEF', '.CRW', '.AI', '.ID']
type_audio = ['.MP3', '.WMA', '.WAV', '.FLAC', '.MIDI', '.OGG']
type_video = ['.AVI', '.DIVX', '.MOV', '.MP4', '.MPG', '.WMV']
type_exe = ['.EXE', '.LNK', '.BAT', '.COM', '.PS1', '.DLL', '.MSI']
type_zip = ['.ZIP', '.RAR', '.RAR5', '.7Z']
type_cd_image = ['.ISO', '.CUE', 'IMG']
type_script = ['.HTML', '.CSS', '.JS', '.PHP', '.EML', '.MSG']

def transfer_file(path_file, last_file):
    global count 
    if os.path.isfile(path_file) == 1:
        count += 1
        path = os.path.dirname(path_file) + '/'
        f_list = os.path.splitext(os.path.basename(last_file))
        file_name = f_list[0] + ' (' + (str(count)) + ')' + f_list[1]
        new_path_file = path + file_name
        transfer_file(new_path_file, last_file)
    else:
        os.rename(last_file, path_file)


while True:
    files = glob.glob(path_download) 
    if len(files) > 0:
        count = 0
        exists = 0
        try:
            last_file = max(files, key=os.path.getctime)
            file_found = 1
        except FileNotFoundError:
            file_found = 0

        if file_found == 1:
            typ = os.path.splitext(last_file)[1] 
            time.sleep(0.5)
            # doc
            if typ.upper() in type_doc:
                # check exists path
                if os.path.exists(path_doc) == 1:
                    exists = 1
                    os.startfile(path_doc)
                    path_file = path_doc + os.path.basename(last_file)

            if typ.upper() in type_img:
                # check exists path
                if os.path.exists(path_img) == 1:
                    exists = 1
                    os.startfile(path_img)
                    path_file = path_img + os.path.basename(last_file)

            if typ.upper() in type_audio:
                # check exists path
                if os.path.exists(path_audio) == 1:
                    exists = 1
                    os.startfile(path_audio)
                    path_file = path_audio + os.path.basename(last_file)

            if typ.upper() in type_video:
                # check exists path
                if os.path.exists(path_video) == 1:
                    exists = 1
                    os.startfile(path_video)
                    path_file = path_video + os.path.basename(last_file)     

            if typ.upper() in type_exe:
                # check exists path
                if os.path.exists(path_exe) == 1:
                    exists = 1
                    os.startfile(path_exe)
                    path_file = path_exe + os.path.basename(last_file)   

            if typ.upper() in type_zip:
                # check exists path
                if os.path.exists(path_zip) == 1:                
                    exists = 1
                    os.startfile(path_zip)
                    path_file = path_zip + os.path.basename(last_file)   

            if typ.upper() in type_cd_image:
                # check exists path
                if os.path.exists(path_cd_image) == 1:                  
                    exists = 1
                    os.startfile(path_cd_image)
                    path_file = path_cd_image + os.path.basename(last_file)  

            if typ.upper() in type_script:
                # check exists path
                if os.path.exists(path_script) == 1: 
                    exists = 1
                    os.startfile(path_script)
                    path_file = path_script + os.path.basename(last_file) 

            if exists == 1:
                transfer_file(path_file, last_file)
