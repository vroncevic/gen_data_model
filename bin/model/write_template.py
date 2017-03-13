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

class WriteTemplate(object):
	"""
	Define class WriteTemplate with attribute(s) and method(s).
	Write a template content with parameters to a file.
	It defines:
		attribute:
			None
		method:
			__init__ - Initial constructor
			write - Write a template content with parameters to a file
	"""

	def __init__(self):
		pass

	def write(self, model_content, model_name):
		"""
		:arg: model_content - Template content for model
		:type: str
		:arg: model_name - Parameter model name
		:type: str
		:return: Boolean status
		:rtype: bool
		"""
		current_dir = getcwd()
		file_name = ModelSelector.format_name(model_name)
		module_file = "{0}/{1}".format(current_dir, file_name)
		model = {
			"mod" : "{0}".format(model_name),
			"modlc": "{0}".format(model_name.lower()),
			"date" : "{0}".format(date.today()),
			"year" : "{0}".format(date.today().year)
		}
		try:
			template = Template(model_content)
			model_file = open(module_file, "w")
			model_file.write(template.substitute(model))
		except (IOError, KeyError, ValueError) as e:
			print("I/O error({0}): {1}".format(e.errno, e.strerror))
			model_file.close()
		else:
			model_file.close()
			chmod(module_file, 0o666)
			return True
		return False
