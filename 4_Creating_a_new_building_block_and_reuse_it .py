import nazca as nd
import nazca.demofab as demo

with nd.Cell(name='myMMI') as mmi:
    mmi1 = demo.mmi1x2_sh().put()
    demo.shallow.strt(length=50).put(mmi1.pin['a0'])
    demo.shallow.sbend(offset=20).put(mmi1.pin['b0'])
    demo.shallow.sbend(offset=-20).put(mmi1.pin['b1'])

mmi.put(0)
mmi.put(0, 100)
mmi.put(300, 50)

nd.export_gds(filename='4_Creating_a_new_building_block_and_reuse_it.gds')