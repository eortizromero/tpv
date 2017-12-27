# -*- coding: utf-8 -*-

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

try:
	_fromUtf8 = QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s

def uppercase(text):
	if not isinstance(text, str):
		raise TypeError("Type text must be a String type(str), not %s" % type(text))
	return text.upper()

class TPV(QMainWindow):
	def __init__(self):
		super(TPV, self).__init__()
		self.setWindowTitle(uppercase('Terminal Punto de Venta'))
		# self.setMinimumSize(1200, 600)
		self.setGeometry(500, 100, 720, 400)
		self.load_panels()
		self.initial_panels()

		button = QPushButton(self.menu_panel)
		button.setGeometry(0, 30, 120, 40)
		button.setText(_fromUtf8('Configuración'))

		button.clicked.connect(self.stack.setPage1)
		# self.bt2.clicked.connect(stack.setPage2)

	def load_panels(self):
		self.menu_panel = QWidget(self)
		self.menu_panel.setObjectName('window')

		# self.content_panel = QWidget(self)
		self.stack = StackedWidget(self)
		self.stack.setObjectName('content_panel')

	def initial_panels(self):
		self.width_first_menu = 120
		self.height_first_menu = 400
		self.menu_panel.setGeometry(0, 0, self.width_first_menu, self.height_first_menu)
		self.width_content = (self.width() - self.width_first_menu) 
		self.stack.setGeometry(self.width_first_menu + 10, 0, self.width_content, self.height_first_menu)

	def responsive_menu_panel(self, width, height):
		self.menu_panel.setStyleSheet('background: lightgreen;')
		if not hasattr(self.menu_panel, '_noresponsive'):
			setattr(self.menu_panel, '_noresponsive', None)

		if self.menu_panel._noresponsive is None:
			self.menu_panel.setGeometry(0, 0, width, height)
		print "width: ", width, "Height:", height

	def responsive_content_panel(self, width, height):
		self.stack.setGeometry(self.width_first_menu + 10, 0, width, height)

		self.content_panel = QWidget(self)
		self.content_panel.setGeometry(0, 0, width, height)
		self.content_panel.setStyleSheet('background: #EEE;')

		label_setting = QLabel(self.content_panel)
		label_setting.setText(_fromUtf8('Configuración (Sólo Administrador)'))
		label_setting.setGeometry(30, 10, width, 40)
		label_setting.setObjectName('label_setting')

		label_server = QLabel(self.content_panel)
		label_server.setText(_fromUtf8('Servidor ERP'))
		label_server.setGeometry(30, 60, width, 40)
		label_server.setObjectName('label_server')

		combo_protocol = QComboBox(self.content_panel)
		combo_protocol.setGeometry(30, 110, 120, 40)
		combo_protocol.addItem('http')
		combo_protocol.addItem('https')

		self.add_page(self.stack, self.content_panel)



	def add_page(self, stack, widget):
		stack.addWidget(widget)

	def resizeEvent(self, evt):
		width = self.width()
		height = self.height()
		self.responsive_content_panel(width, height)
		width_menu = self.width_first_menu
		if width >= 900:
			width_menu = 250
		self.responsive_menu_panel(width_menu, height)
		


class FaderWidget(QWidget):

	def __init__(self, old_widget, new_widget):
	
		QWidget.__init__(self, new_widget)
		
		self.old_pixmap = QPixmap(new_widget.size())
		old_widget.render(self.old_pixmap)
		self.pixmap_opacity = 1.0
		
		self.timeline = QTimeLine()
		self.timeline.valueChanged.connect(self.animate)
		self.timeline.finished.connect(self.close)
		self.timeline.setDuration(333)
		self.timeline.start()
		
		self.resize(new_widget.size())
		self.show()
	
	def paintEvent(self, event):
	
		painter = QPainter()
		painter.begin(self)
		painter.setOpacity(self.pixmap_opacity)
		painter.drawPixmap(0, 0, self.old_pixmap)
		painter.end()
	
	def animate(self, value):
	
		self.pixmap_opacity = 1.0 - value
		self.repaint()

class StackedWidget(QStackedWidget):

	def __init__(self, parent = None):
		QStackedWidget.__init__(self, parent)
	
	def setCurrentIndex(self, index):
		self.fader_widget = FaderWidget(self.currentWidget(), self.widget(index))
		QStackedWidget.setCurrentIndex(self, index)
	
	def setPage1(self):
		self.setCurrentIndex(0)
	
	def setPage2(self):
		self.setCurrentIndex(1)


tpv = TPV