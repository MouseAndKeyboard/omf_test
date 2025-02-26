import pyvista as pv
import omfvista
from pyvista import examples
from pyvista.trame.ui import plotter_ui
from trame.app import get_server
from trame.ui.vuetify3 import SinglePageLayout

# Always set PyVista to plot off screen with Trame
pv.OFF_SCREEN = True

server = get_server()
state, ctrl = server.state, server.controller

mesh = examples.load_random_hills()


project = omfvista.load_project('./test_file.omf')

vol = project['Block Model']
assay = project['wolfpass_WP_assay']
topo = project['Topography']
dacite = project['Dacite']

# Create a plotting window
p = pv.Plotter(notebook=False)
# Add our datasets
p.add_mesh(topo, cmap='gist_earth', opacity=0.5)
p.add_mesh(assay, color='blue', line_width=3)
p.add_mesh(dacite, color='yellow', opacity=0.6)
# Add the volumetric dataset with a thresholding tool
p.add_mesh_threshold(vol)
# Add the bounds axis
p.show_bounds()

with SinglePageLayout(server) as layout:
    with layout.content:
        # Use PyVista's Trame UI helper method
        #  this will add UI controls
        view = plotter_ui(p)

server.start()


# mkdir omf_test
# cd omf_test
# python3 -m venv env 
# source env/bin/activate
# pip install pyvista omfvista trame trame-vtk trame-vuetify
# Download and move test_file.omf into this folder.
# python3 test_script.py
# should see result


