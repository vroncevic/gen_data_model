# -*- coding: utf-8 -*-

import os
import sys

sys.path.insert(0, os.path.abspath('../../'))

project = u'gen_data_model'
copyright = u'2017, Vladimir Roncevic <elektron.ronca@gmail.com>'
author = u'Vladimir Roncevic <elektron.ronca@gmail.com>'
version = u'2.2.2'
release = u'https://github.com/vroncevic/gen_data_model/releases'
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode']
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
language = None
exclude_patterns = []
pygments_style = None
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
htmlhelp_basename = 'gen_data_modeldoc'
latex_elements = {}
latex_documents = [(
    master_doc, 'gen_data_model.tex', u'gen\\_data\\_model Documentation',
    u'Vladimir Roncevic \\textless{}elektron.ronca@gmail.com\\textgreater{}',
    'manual'
)]
man_pages = [(
    master_doc, 'gen_data_model', u'gen_data_model Documentation', [author], 1
)]
texinfo_documents = [(
    master_doc, 'gen_data_model', u'gen_data_model Documentation',
    author, 'gen_data_model', 'One line description of project.',
    'Miscellaneous'
)]
epub_title = project
epub_exclude_files = ['search.html']
