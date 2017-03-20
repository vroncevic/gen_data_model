# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

from model.read_template import ReadTemplate
from model.write_template import WriteTemplate
from model.model_selector import ModelSelector

class GenModel(ReadTemplate, WriteTemplate):
	"""
	Define class GenModel with attribute(s) and method(s).
	Generate data model by template and parameters.
	It defines:
		attribute:
			__status - Operation status
		method:
			__init__ - Initial constructor
			gen_model - Generate module file with data model
	"""

	def __init__(self):
		ReadTemplate.__init__(self)
		WriteTemplate.__init__(self)
		self.__status = False

	def gen_model(self, model_name):
		"""
		:param model_name: Parameter name (class and file name)
		:type: str
		:return: Boolean status
		:rtype: bool
		"""
		model_type = ModelSelector.choose_model()
		if model_type != ModelSelector.Cancel:
			model_content, model_base_content = self.read(model_type)
			if model_content and model_base_content:
				status_model = self.write(model_content, model_name)
				status_base_model = self.write(model_base_content, "base")
				if status_model and status_base_model:
					self.__status = True
		else:
			self.__status = True
		return self.__status
