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
from app.error.lookup_error import AppError

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
			read - Read templates and return a string representations
	"""

	__TEMPLATE_DIR = "/../../conf/template"

	__TEMPLATES = {
		ModelSelector.Django : [
			"django.template", "django_base_model.template"
		],
		ModelSelector.Flask : [
			"flask.template", "flask_base_model.template"
		],
		ModelSelector.SQLAlchemy : [
			"sqlalchemy.template", "sqlalchemy_base_model.template"
		]
	}

	def __init__(self):
		local_dir = dirname(realpath(__file__))
		self.__template = "{0}{1}".format(
			local_dir, ReadTemplate.__TEMPLATE_DIR
		)

	def read(self, model_type):
		"""
		:param model_type: Chosen type of model (Django/Flask/SQLAlchemy)
		:type: int
		:return: Template contents (base data model and data model)
		:rtype: str or NoneType
		"""
		try:
			if model_type in ReadTemplate.__TEMPLATES.keys():
				templates = ReadTemplate.__TEMPLATES[model_type]
				template_file = "{0}/{1}".format(
					self.__template, templates[0]
				)
				template_base_file = "{0}/{1}".format(
					self.__template, templates[1]
				)
				model_file = open(template_file, "r")
				model_base_file = open(template_base_file, "r")
				model_content = model_file.read()
				model_base_content = model_base_file.read()
			else:
				raise AppError("wrong template type!")
		except IOError as e:
			print("I/O error({0}): {1}".format(e.errno, e.strerror))
		except AppError as e2:
			print("Error: ", e2)
		else:
			model_file.close()
			model_base_file.close()
			return model_content, model_base_content
		return None, None
