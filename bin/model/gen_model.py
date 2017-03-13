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
			None
		method:
			__init__ - Initial constructor
			gen_model - Generate module file with data model
	"""

	def __init__(self):
		ReadTemplate.__init__(self)
		WriteTemplate.__init__(self)

	def gen_model(self, model_name):
		"""
		:arg: model_name - Parameter name (class and file name)
		:type: str
		:return: Boolean status
		:rtype: bool
		"""
		status = False
		model_type = ModelSelector.choose_model()
		if model_type != ModelSelector.Cancel:
			model_content = self.read(model_type)
			if model_content:
				status = self.write(model_content, model_name)
		else:
			status = True
		return status
