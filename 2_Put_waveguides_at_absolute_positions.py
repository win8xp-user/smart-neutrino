import nazca as nd

nd.strt(length=5).put(0)
nd.strt(length=10, width=4).put(0, 10)
nd.bend(angle=90, radius=10).put(15, 10, -90)

nd.export_gds(filename='2_Put_waveguides_at_absolute_positions.gds')