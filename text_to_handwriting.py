# text to handwriting 
# py.whattkit module of python is used

import pywhatkit as pw

txt = """ A lot and 
			lots of texts """

pw.text_to_handwriting(txt,"demo1.png",[0,0,138]) # by default .png is format in blue color. This will create a file adjacent to the code file.

print("END")

