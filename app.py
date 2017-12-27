# -*- coding: utf-8 -*-

from PyQt4.QtGui import QApplication
import sys
from views import tpv

def create_app():
	main_tpv = QApplication(sys.argv)
	init_view = tpv()
	init_view.show()
	with open('static/css/style.css', 'r') as t:
		style = t.read()
	main_tpv.setStyleSheet(style)
	sys.exit(main_tpv.exec_())

if __name__ == '__main__':
	create_app()