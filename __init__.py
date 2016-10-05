import os
from cudatext import *
from .css_toc_definitions import *


def get_info():
    x0, y0, x1, y1 = ed.get_carets()[0]
    x0 = 0 #trunc before line start
    cnt = ed.get_text_substr(0, 0, x0, y0)
    sel = ed.get_text_sel()
    line = '' #ed.get_text_line(y0)
    return (cnt, sel, line, y0)
    

class Command:
    def _section(self, func):
        cnt, sel, line, y0 = get_info()
        text = func(cnt, sel, line)
        if not text: return
        ed.insert(0, y0, text+'\n')
        ed.set_caret(0, y0+1)
        msg_status('Inserted section')

    def do_section(self):
        self._section(get_section)
    
    def do_section_sub(self):
        self._section(get_subsection)
        
    def do_section_sub_sub(self):
        self._section(get_subsubsection)
        
    def do_toc(self):
        text = get_toc(ed.get_text_all())
        if not text: return
        ed.insert(0, 0, text)
        ed.set_caret(0, 0)
        msg_status('Inserted TOC')
