# load the main Nacza-Design module and initialize logging.
import nazca as nd
nd.logfile(name=__file__, stdout=False)

# load PDK for the Smart Photonics MPW process and switch on logging
import sp_HS28PC as sp

# load packaging templates
from nazca.demopackager.packages import Package1

# switch on pin2pin DRC
nd.pin2pin_drc_on()

nd.strt(length=20).put()
nd.bend(angle=90).put()
nd.bend(angle=-180).put()
nd.strt(length=10).put()

sp.nazca_logo()
sp.copysign(1.0, -0.0)

# nd.export_gds(filename='1B_Import_nazca_draw_waveguides.gds')
nd.export_gds(filename=__file__)