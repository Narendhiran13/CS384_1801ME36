import os
import re

episode_padding = 2
season_padding = 2


def _zero_remove_fn(_string_):
    '''
    Function  to remove leading zero in numbers

    '''
    _string_ = _string_.strip()
    for i in range(len(_string_)):
        if _string_[i] != '0':
            return _string_[i:]


def rename_FIR(folder_name):
    # JOIning the required path where Subtitles & MP4 is Present
    path = os.path.join(os.getcwd(), os.path.join('Subtitles', folder_name))

    try:
        for file in os.listdir(path):  # Checking for Each & every file
            # As the Movie Name is present, before '-'.
            file_name = file.split('-')
            file_name = [i.strip() for i in file_name]

            FILE_type = file_name[-1].split('.')[-1]  # type of the file

            # To Extract the name of the Episode
            i = ''
            for s in file_name[1:]:
                if 'Episode' in s:
                    i = s
                    break
            episode = (episode_padding -
                       len(_zero_remove_fn(i.split()[1])))*'0' + _zero_remove_fn(i.split()[1])

            # To rename And delete the exisisting old file name.
            file_name_new = file_name[0] + \
                " Episode " + episode + "." + FILE_type
            file_name_old = os.path.join(path, file)
            file_name_new = os.path.join(path, file_name_new)
            try:
                os.rename(file_name_old, file_name_new)
            except:
                os.remove(file_name_old)

    # In case, renaming Fails...
    except:
        pass
    # rename Logic


def rename_Game_of_Thrones(folder_name):
    # JOIning the required path where Subtitles & MP4 is Present
    path = os.path.join(os.getcwd(), os.path.join('Subtitles', folder_name))

    for file in os.listdir(path):  # Checking for Each & every file

        try:
            # As the Movie Name is present, before '-'.
            file_name = file.split('-')
            file_name = [i.strip() for i in file_name]

            FILE_type = file_name[-1].split('.')[-1]  # type of the file

            # To Extract the name of the Episode
            season = (
                season_padding - len(_zero_remove_fn(file_name[1].split('x')[0])))*'0' + _zero_remove_fn(file_name[1].split('x')[0])
            episode = (
                episode_padding - len(_zero_remove_fn(file_name[1].split('x')[1])))*'0' + _zero_remove_fn(file_name[1].split('x')[1])
            episode_name = file_name[-1].split('.')[0].strip()

            # To rename And delete the exisisting old file name.
            file_name_new = file_name[0] + " - Season " + season + \
                " Episode " + episode + " - " + episode_name + "." + FILE_type
            file_name_old = os.path.join(path, file)
            file_name_new = os.path.join(path, file_name_new)
            try:
                os.rename(file_name_old, file_name_new)
            except:
                os.remove(file_name_old)

        # In case, renaming Fails...
        except:
            pass
    # rename Logic


def rename_Sherlock(folder_name):
    # JOIning the required path where Subtitles & MP4 is Present
    path = os.path.join(os.getcwd(), os.path.join('Subtitles', folder_name))

    for file in os.listdir(path):  # Checking for Each & every file

        try:
            # As the Movie Name is present, before '-'.
            file_name = file.split('.')
            file_name = [i.strip() for i in file_name]

            # To Extract the name of the Episode
            if 'E' not in file_name[1]:
                season = (season_padding -
                          len(_zero_remove_fn(file_name[1][1:])))*'0' + _zero_remove_fn(file_name[1][1:])
                episode = (episode_padding -
                           len(_zero_remove_fn(file_name[2][1:])))*'0' + _zero_remove_fn(file_name[2][1:])
            else:
                block = file_name[1].split("E")
                season = (
                    season_padding - len(_zero_remove_fn(block[0][1:])))*'0' + _zero_remove_fn(block[0][1:])
                episode = (episode_padding -
                           len(_zero_remove_fn(block[1])))*'0' + _zero_remove_fn(block[1])

            # To rename And delete the exisisting old file name.
            file_name_new = file_name[0] + " - Season " + season + \
                " Episode " + episode + "." + file_name[-1]
            file_name_new = os.path.join(path, file_name_new)
            file_name_old = os.path.join(path, file)

            try:
                os.rename(file_name_old, file_name_new)
            except:
                os.remove(file_name_old)
        # In case, renaming Fails...
        except:
            pass
    # rename Logic


def rename_Suits(folder_name):
    # JOIning the required path where Subtitles & MP4 is Present
    path = os.path.join(os.getcwd(), os.path.join('Subtitles', folder_name))

    # Checking for Each & every file
    for file in os.listdir(path):
        try:
            # As the Movie Name is present, before '-'.
            file_name = file.split('-')
            file_name = [i.strip() for i in file_name]

            FILE_type = file_name[-1].split('.')[-1]  # type of the file

            # To Extract the name of the Episode
            season = (
                season_padding - len(_zero_remove_fn(file_name[1].split('x')[0])))*'0' + _zero_remove_fn(file_name[1].split('x')[0])
            episode = (
                episode_padding - len(_zero_remove_fn(file_name[1].split('x')[1])))*'0' + _zero_remove_fn(file_name[1].split('x')[1])

            if len(file_name) == 3:
                episode_name = file_name[-1].split('.')[0].strip()
            else:
                episode_name = file_name[-2].split('.')[0].strip()

            # To rename And delete the exisisting old file name.
            file_name = file_name[0] + " - Season " + season + \
                " Episode " + episode + " - " + episode_name + "." + FILE_type
            file_name_old = os.path.join(path, file)
            file_name = os.path.join(path, file_name)
            try:
                os.rename(file_name_old, file_name)
            except:
                os.remove(file_name_old)

            # In case, renaming Fails...
        except:

            pass

    # rename Logic


def rename_How_I_Met_Your_Mother(folder_name):

    # JOIning the required path where Subtitles & MP4 is Present
    path = os.path.join(os.getcwd(), os.path.join('Subtitles', folder_name))

    for file in os.listdir(path):  # Checking for Each & every file

        try:
            # As the Movie Name is present, before '-'.
            file_name = file.split('-')
            file_name = [i.strip() for i in file_name]

            # To Extract the name of the Episode
            if len(file_name) == 3:
                EPISODE_name = file_name[-1].split('.')[0].strip()
            else:
                EPISODE_name = file_name[-2].split('.')[0].strip()

            file_TYPE = file_name[-1].split('.')[-1]  # type of the file

            # Extracting the season & Episode number
            season = (
                season_padding - len(_zero_remove_fn(file_name[1].split('x')[0])))*'0' + _zero_remove_fn(file_name[1].split('x')[0])

            episode = (
                episode_padding - len(_zero_remove_fn(file_name[1].split('x')[1])))*'0' + _zero_remove_fn(file_name[1].split('x')[1])

            # Naming the New file name
            file_name = file_name[0] + " - Season " + season + \
                " Episode " + episode + " - " + EPISODE_name + "." + file_TYPE

            # To rename And delete the exisisting old file name.
            old_file_name = os.path.join(path, file)
            file_name = os.path.join(path, file_name)
            try:
                os.rename(old_file_name, file_name)
            except:
                os.remove(old_file_name)

            # In case, renaming Fails...
        except:
            pass

    # rename Logic


rename_How_I_Met_Your_Mother("How I Met Your Mother")
rename_FIR("FIR")
rename_Game_of_Thrones("Game of Thrones")
rename_Sherlock("Sherlock")
rename_Suits("Suits")
