import codecs


def delete_html_tags(html_file, result_file='cleaned.txt'):
    work_lst = []
    html_hh = codecs.open(html_file, 'r', 'utf-8').read()
    for el in html_hh:
        work_lst.append(el)
    while work_lst.count('<'):
        if '<' or '>' in work_lst:
            z = work_lst.index('<')
            t = work_lst.index('>')
            del work_lst[z:t + 1]
            continue
        if '<' or '>' not in work_lst:
            break

    work_lst = ''.join(work_lst).split('  ')
    work_lst = [txt for txt in work_lst if txt.strip()]

    html_hh = codecs.open(result_file, 'w', 'utf-8')
    for txt in work_lst:
        html_hh.write(txt)
    html_hh.close()
    return result_file


delete_html_tags("draft.html")
