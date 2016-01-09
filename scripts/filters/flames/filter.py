import os
from common import FilterParameter, CustomFilterBase

class Filter(CustomFilterBase):

	def __init__(self):
		CustomFilterBase.__init__(self, os.path.dirname(__file__))
		self.name = "Flames"
		self.group = "Old"

		visible_tag = self.dull['visual'].find(".//*[@id='visible1']")
		turbulence_tag = self.dull['filter'].find(".//*[@id='feTurbulence1']")
		blur_tag = self.dull['filter'].find(".//*[@id='feGaussianBlur1']")

		self.param['scale'] = FilterParameter(visible_tag, 'transform', 'scale\((.+?)\) ', 'scale(%.2f) ')
		self.param['octaves'] = FilterParameter(turbulence_tag, 'numOctaves', '(.+)', '%d')
		self.param['blur'] = FilterParameter(blur_tag, 'stdDeviation', '(.+)', '%.1f')
		self.param['frequency_x'] = FilterParameter(turbulence_tag, 'baseFrequency', '(.+?) ', '%.2f ')
		self.param['frequency_y'] = FilterParameter(turbulence_tag, 'baseFrequency', ' (.+)', ' %.2f')

		gui_elements = ("window", "scale", "octaves", "frequency_x", "frequency_y", "blur")

		self.on_scale_changed = self.build_plain_handler('scale')
		self.on_blur_changed = self.build_plain_handler('blur')
		self.on_frequency_x_changed = self.build_plain_handler('frequency_x')
		self.on_frequency_y_changed = self.build_plain_handler('frequency_y')
		self.on_octaves_changed = self.build_plain_handler('octaves', translate=int)

		self.gui_load(gui_elements)
		self.gui_setup()

	def gui_setup(self):
		self.gui_settler_plain('scale', 'frequency_x', 'frequency_y', 'blur')
		self.gui_settler_plain('octaves', translate=int)
