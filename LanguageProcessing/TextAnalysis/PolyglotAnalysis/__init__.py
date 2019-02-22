import os
import polyglot

# change path
dir_path = os.path.dirname(os.path.realpath(__file__))
path=os.path.join(dir_path, 'data')
polyglot.polyglot_path = path

