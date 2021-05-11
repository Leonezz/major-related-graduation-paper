#!/bin/python3

import pathlib
md_file_list  =list(pathlib.Path("./src").glob('./*.md'))

if len(md_file_list) != 0:
    list_after_sort = sorted(md_file_list)
    content = ""
    for md_file in list_after_sort:
        with open(md_file, 'r', encoding='UTF-8') as f:
            content+=f.read().replace("---\nbibliography: [../ref.bib]\n---", "\n")
    result_file = open("./input.md", 'w', encoding='UTF-8')
    result_file.write("---\nbibliography: [./ref.bib]\n---\n")
    result_file.write(content)
    result_file.close()