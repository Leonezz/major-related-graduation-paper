"""
由 pandoc 提供了 pandocfilters 模块, 方便用户编写过滤器.
"""

from pandocfilters import toJSONFilter, Str, Para, Image, attributes, \
    get_value, RawBlock

"""
针对目标格式为 pdf 的过滤函数
"""
def latex(x):
    return RawBlock('latex', x)


"""
针对目标格式为 html 的过滤函数
"""
def html(x):
    return RawBlock('html', x)

"""
过滤函数. 关于目标格式为 docx 的过滤在此过滤函数中.
"""
def dzfimglink(key, value, fmt, meta):
    if key == 'CodeBlock':
        [[ident, classes, keyvals], code] = value
        if 'dzfimg' in classes:
            path, val = get_value(keyvals, 'path', '')
            title, val = get_value(val, 'title', '')

            if 'latex' == fmt:
                return ([latex('\\begin{center}')]  +
                        [latex('\\includegraphics{' + path + '}')] +
                        [latex(title)] +
                        [latex('\\end{center}')])
            if 'html' == fmt:
                link = '<center><img src=' + path \
                    + '><br>' + title + '</center>'
                return ([html(link)])
            if 'docx' == fmt:
                image = Image(attributes({}), [], [path, title])
                return (Para([image, Str('\n' + title)]))


"""
call dzfimglink
"""
if __name__ == "__main__":
    toJSONFilter(dzfimglink)