# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

from datetime import date
from os import getcwd, chmod
from string import Template
from model.model_selector import ModelSelector
from app.error.lookup_error import AppError

class WriteTemplate(object):
	"""
	Define class WriteTemplate with attribute(s) and method(s).
	Write a template content with parameters to a file.
	It defines:
		attribute:
			__status - Operation status
		method:
			__init__ - Initial constructor
			write - Write a template content with parameters to a file
	"""

	def __init__(self):
		self.__status = False

	def write(self, model_content, model_name):
		"""
		:param model_content: Template content for model
		:type: str
		:param model_name: Parameter model name
		:type: str
		:return: Boolean status
		:rtype: bool
		"""
		try:
			file_name = ModelSelector.format_name(model_name)
			if file_name:
				current_dir = getcwd()
				module_file = "{0}/{1}".format(current_dir, file_name)
				model_params = {
					"mod": "{0}".format(model_name),
					"modlc": "{0}".format(model_name.lower()),
					"date": "{0}".format(date.today()),
					"year": "{0}".format(date.today().year)
				}
				template = Template(model_content)
				model_file = open(module_file, "w")
				model_file.write(template.substitute(model_params))
			else:
				raise AppError("missing module name!")
		except (IOError, KeyError, ValueError) as e:
			print("I/O error({0}): {1}".format(e.errno, e.strerror))
		except AppError as e2:
			print("Error: ", e2)
		else:
			model_file.close()
			chmod(module_file, 0o666)
			self.__status = True
		return self.__status
