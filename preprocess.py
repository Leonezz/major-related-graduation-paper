#coding=utf-8
#!/bin/python3

import pathlib
md_file_list = list(pathlib.Path("./src").glob('./*.md'))

if len(md_file_list) != 0:
    list_after_sort = sorted(md_file_list)
    content = ""
    for md_file in list_after_sort:
        with open(md_file, 'r', encoding='UTF-8') as f:
            if str(md_file).find("input.md") == -1:
                content += f.read().replace(
                    ("---\n"
                     "bibliography: [../ref.bib]\n"
                     "fignos-cleveref: True\n"
                     "fignos-caption-name: 图\n"
                     "tablenos-cleveref: True\n"
                     "tablenos-caption-name: 表\n"
                     "---"), "\n").replace("---\nbibliography: [../ref.bib]\n---", "\n")

    result_file = open("./src/input.md", 'w', encoding='UTF-8')
    result_file.write("---\n"
                      "bibliography: [../ref.bib]\n"
                      "fignos-cleveref: True\n"
                      "fignos-caption-name: 图\n"
                      "tablenos-cleveref: True\n"
                      "tablenos-caption-name: 表\n"
                      "---\n")
    result_file.write(content)
    result_file.close()
