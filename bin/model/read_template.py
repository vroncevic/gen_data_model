# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

from os.path import dirname, realpath
from model.model_selector import ModelSelector

class ReadTemplate(object):
	"""
	Define class ReadTemplate with attribute(s) and method(s).
	Read a model template file and return a content.
	It defines:
		attribute:
			__TEMPLATE_DIR - Prefix path to templates
			__TEMPLATES - Models (python module templates)
			__template - Absolute file path of template
		method:
			__init__ - Initial constructor
			read - Read a template and return a string representation
	"""

	__TEMPLATE_DIR = "/../../conf/template"

	__TEMPLATES = {
		ModelSelector.Django : "django.template",
		ModelSelector.Flask : "flask.template",
		ModelSelector.SQLAlchemy : "sqlalchemy.template"
	}

	def __init__(self):
		current_dir = dirname(realpath(__file__))
		self.__template = "{0}{1}".format(
			current_dir, ReadTemplate.__TEMPLATE_DIR
		)

	def read(self, model_type):
		"""
		:arg: model_type - Chosen type of model (Django/Flask/SQLAlchemy)
		:return: Template content
		:rtype: str or NoneType
		"""
		try:
			template_file = "{0}/{1}".format(
				self.__template, ReadTemplate.__TEMPLATES[model_type]
			)
			model_file = open(template_file, "r")
			model_content = model_file.read()
		except IOError as e:
			print("I/O error({0}): {1}".format(e.errno, e.strerror))
			model_file.close()
		else:
			model_file.close()
			return model_content
		return None
