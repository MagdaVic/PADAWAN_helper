from sort import *

# def validate_correct_path(func):
#     def wrapper(output_list, address_book):
#         try:
#             rootdir, *other = output_list
#         except ValueError:
#             print('Write path')
#         else:
#             rootdir = " ".join(output_list[:])
#             if not os.path.exists(rootdir):
#                 print('Uknown directory, write correct path and directory')
#             else:
#                 return func(output_list, address_book)
#     return wrapper

# @validate_correct_path
# def sort(output_list, address_book: AddressBook):
#     dict_extentions = {'archives': ['ZIP', 'GZ', 'TAR'], 'video': ['AVI', 'MP4', 'MOV', 'MKV'], 'audio': ['MP3', 'OGG', 'WAV', 'AMR'],
#                        'documents': ['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX'], 'images': ['JPEG', 'PNG', 'JPG', 'SVG']}

#     dict_fact_files = {'archives': [], 'video': [], 'audio': [],
#                        'documents': [], 'images': [], 'uknown_extension': []}

#     dict_known_unknown_extentions = {
#         'known extensions': set(), 'unknown extensions': set()}
#     rootdir=" ".join(output_list[:])
#     lst_all_files = []
#     lst_all_files = list_all_files_in_rootdir(rootdir, lst_all_files)
#     create_new_folders_in_rootdir(rootdir, dict_extentions)
#     move_and_normalize_and_unarchieve_files_into_correct_folders(
#         rootdir, dict_extentions, lst_all_files, dict_fact_files)
#     normalize_all_files_and_folders_in_archieve(
#         os.path.join(rootdir, 'archives'))
#     remove_all_unnecessary_folders(rootdir,dict_extentions)
#     print_out_in_console(dict_fact_files, dict_known_unknown_extentions)