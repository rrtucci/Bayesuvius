from texnn import *

mosaic = [
    "__Q___",
    "__KA__",
    "__V___",
    "X____Y"
]

plateQKV = Plate(
    first_and_last_row=(0, 2),
    first_and_last_col=(2, 2),
    style_name="dashed",
    num_layers_str="10"
)

plateQKVA = Plate(
    first_and_last_row=(0, 2),
    first_and_last_col=(2, 3),
    margin=2.0,
    num_layers_str="20"
)

plates = [plateQKV, plateQKVA]

nodeQ = Node(
    name="Q",
    tile_ch='Q',
    parent_names=["X"],
    color="SkyBlue"
)
nodeK = Node(
    name="K",
    tile_ch='K',
    parent_names=["X"],
    color="SkyBlue"
)
nodeA = Node(
    name="A",
    tile_ch='A',
    parent_names=["Q", "K", "V"],
    color="SkyBlue"
)
nodeV = Node(
    name="V",
    tile_ch='V',
    parent_names=["X"],
    color="SkyBlue"
)
nodeX = Node(
    name="X",
    tile_ch='X',
    parent_names=[],
    color="pink"
)
nodeY = Node(
    name="Y",
    tile_ch='Y',
    parent_names=["X", "A"],
    color="pink"
)

nodes = [nodeQ, nodeK, nodeA, nodeV, nodeX, nodeY]

print("\nmosaic:", mosaic)
name = "rock_layers"
dag = DAG(name, mosaic, nodes, plates=plates)
dag.write_tex_file(
    underline=True,
    fig_caption="Rock Layers.",
    conditional_prob=True
)
