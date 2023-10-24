import nazca as nd
import nazca.demofab as demo

mmi1 = demo.mmi1x2_sh().put()
demo.shallow.strt(length=50).put(mmi1.pin['a0'])
demo.shallow.sbend(offset=20).put(mmi1.pin['b0'])
demo.shallow.sbend(offset=-20).put(mmi1.pin['b1'])

nd.export_gds(filename='3_Using_a_PDK.gds')