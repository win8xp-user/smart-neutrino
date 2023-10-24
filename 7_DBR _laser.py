import nazca as nd
import nazca.demofab as demo

print(nd.__version__)

laser1 = demo.dbr_laser(Lsoa=1500)
laser2 = demo.dbr_laser(Lsoa=1000)
laser3 = demo.dbr_laser(Lsoa=500, Ldbr1=20, Ldbr2=800, Lpm=150)
laserBBs = [laser1, laser2, laser3]

for j, laser in enumerate(laserBBs):
    demo.shallow.strt(length=100).put(0, 800*j)
    las = laser.put()
    demo.shallow.strt(length=200).put()

    for i, pinname in enumerate(['c0', 'c1', 'c2', 'c3']):
        pad = demo.pad_dc().put(las.pin['a0'].move(-i*250-150, -600, -90))
        demo.metaldc.sbend_p2p(las.pin[pinname], pad.pin['c0'], Lstart=(i+1)*75).put()

nd.export_gds(filename='7B_DBR_laser.gds')