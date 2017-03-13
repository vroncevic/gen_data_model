# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

class ModelSelector(object):
	"""
	Define class ModelSelector with attribute(s) and method(s).
	Selecting data model type for generating process.
	It defines:
		attribute:
			Django - 0 (Django type model)
			Flask - 1 (Flask type model)
			SQLAlchemy - 2 (SQLAlchemy type model)
			Cancel - 3 (Cancel option)
			__MODELS - Dictionary with option/description
		method:
			choose_model - Selecting type of model for generating process
			format_name - Formatting name for file module
	"""

	Django, Flask, SQLAlchemy, Cancel = range(4)

	__MODELS = {
		Django : "Django model",
		Flask : "Flask model",
		SQLAlchemy : "SQLAlchemy model",
		Cancel : "Cancel"
	}

	@classmethod
	def choose_model(cls):
		"""
		:return: Type of data model
		:rtype: int
		"""
		print("\n model option list:")
		for key in sorted(ModelSelector.__MODELS):
			print("  {0} {1}".format(key, ModelSelector.__MODELS[key]))
		while True:
			model_type = input(" Select model: ")
			if model_type not in ModelSelector.__MODELS.keys():
				print(" Not an appropriate choice.")
			else:
				break
		return model_type

	@classmethod
	def format_name(cls, model_name):
		"""
		:arg: model_name - Postfix name for data model file
		:type:
		:return: File name with extension (lower case)
		:rtype: str or NoneType
		"""
		if model_name:
			file_name = "{0}{1}".format("model_", model_name.lower())
		else:
			return None
		return "{0}{1}".format(file_name, ".py")
