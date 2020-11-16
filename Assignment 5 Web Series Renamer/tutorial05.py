import os
import re

episode_padding = 2
season_padding = 2


def rm_zero(s):
    '''
    Fn to remove leading zero in numbers
    '''
    s = s.strip()
    for i in range(len(s)):
        if s[i] != '0':
            return s[i:]


def rename_FIR(folder_name):
    pass
    # rename Logic


def rename_Game_of_Thrones(folder_name):
    pass
    # rename Logic


def rename_Sherlock(folder_name):
    pass
    # rename Logic


def rename_Suits(folder_name):
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
                season_padding - len(rm_zero(file_name[1].split('x')[0])))*'0' + rm_zero(file_name[1].split('x')[0])

            episode = (
                episode_padding - len(rm_zero(file_name[1].split('x')[1])))*'0' + rm_zero(file_name[1].split('x')[1])

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
