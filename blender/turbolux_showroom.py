"""
Turbolux Paints showroom - procedural Blender scene
====================================================

Rebuilds the showroom interior from the reference render:
  - black marble brand wall with gold "Turbolux PAINTS" lettering
  - wood shelving column, curved white reception counter
  - two "Exterior finishes" display units (magazines, books, swatches, buckets)
  - concrete feature wall with floating shelves, paint cans and a TV
  - navy sofa, two round tulip tables with brown tulip chairs
  - glass shop front, recessed ceiling downlights

HOW TO RUN (Blender 3.6 / 4.x):
  1. Open Blender, switch to the "Scripting" workspace.
  2. Text > Open... and pick this file (or paste it into a new text block).
  3. Press "Run Script" (Alt+P). The current scene is cleared and rebuilt.
  4. Press F12 to render (Cycles). Camera and lights are set up already.

Units are metres. Room: x = left/right, y = depth (back wall at y = 4.9),
z = up (ceiling at 3.0). Tweak the constants below to change the layout.
"""

import math

import bmesh
import bpy
from mathutils import Vector

# ----------------------------------------------------------------------------
# Settings
# ----------------------------------------------------------------------------
ROOM_X0, ROOM_X1 = -4.2, 3.6      # left marble wall .. glass front
BACK_Y = 4.9                      # back wall
FRONT_Y = -1.6                    # behind the camera
CEIL_Z = 3.0

BRAND_LINE1 = "Turbolux"
BRAND_LINE2 = "PAINTS"
DISPLAY_TEXT = "Exterior finishes"

# Optional: path to a picture for the TV screen (e.g. "C:/images/city.jpg").
# Leave empty to use a purple night-sky gradient.
TV_IMAGE = ""

# Optional: path to a .ttf/.otf font for the brand lettering ("" = Blender font).
BRAND_FONT = ""

RENDER_SAMPLES = 128
RES_X, RES_Y = 1600, 824

rad = math.radians


# ----------------------------------------------------------------------------
# Scene reset
# ----------------------------------------------------------------------------
def clear_scene():
    for ob in list(bpy.data.objects):
        bpy.data.objects.remove(ob, do_unlink=True)
    for coll in (bpy.data.meshes, bpy.data.materials, bpy.data.curves,
                 bpy.data.lights, bpy.data.cameras):
        for block in list(coll):
            if block.users == 0:
                coll.remove(block)


# ----------------------------------------------------------------------------
# Materials
# ----------------------------------------------------------------------------
def hex_rgb(h):
    """'#RRGGBB' (sRGB) -> linear RGB tuple."""
    h = h.lstrip("#")
    out = []
    for i in (0, 2, 4):
        c = int(h[i:i + 2], 16) / 255.0
        out.append(c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4)
    return tuple(out)


def _inp(node, *names):
    for n in names:
        if n in node.inputs:
            return node.inputs[n]
    return None


def _new_mat(name):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    return m, m.node_tree.nodes, m.node_tree.links, m.node_tree.nodes["Principled BSDF"]


def mat_basic(name, color, rough=0.5, metal=0.0, transmission=0.0, ior=1.45):
    m, nodes, links, b = _new_mat(name)
    b.inputs["Base Color"].default_value = (*hex_rgb(color), 1)
    b.inputs["Roughness"].default_value = rough
    b.inputs["Metallic"].default_value = metal
    if transmission:
        t = _inp(b, "Transmission Weight", "Transmission")
        if t:
            t.default_value = transmission
        i = _inp(b, "IOR")
        if i:
            i.default_value = ior
    m.diffuse_color = (*hex_rgb(color), 1)
    return m


def mat_emit(name, color, strength):
    m, nodes, links, b = _new_mat(name)
    nodes.remove(b)
    em = nodes.new("ShaderNodeEmission")
    em.inputs["Color"].default_value = (*hex_rgb(color), 1)
    em.inputs["Strength"].default_value = strength
    links.new(em.outputs["Emission"], nodes["Material Output"].inputs["Surface"])
    return m


def mat_marble(name, base, vein, rough, scale):
    """Wave-texture marble: thin veins at the wave minima."""
    m, nodes, links, b = _new_mat(name)
    tc = nodes.new("ShaderNodeTexCoord")
    wave = nodes.new("ShaderNodeTexWave")
    wave.inputs["Scale"].default_value = scale
    wave.inputs["Distortion"].default_value = 14.0
    wave.inputs["Detail"].default_value = 8.0
    wave.inputs["Detail Scale"].default_value = 1.6
    ramp = nodes.new("ShaderNodeValToRGB")
    e = ramp.color_ramp.elements
    e[0].position, e[0].color = 0.0, (*hex_rgb(vein), 1)
    e[1].position, e[1].color = 0.07, (*hex_rgb(base), 1)
    links.new(tc.outputs["Object"], wave.inputs["Vector"])
    links.new(wave.outputs["Fac"], ramp.inputs["Fac"])
    links.new(ramp.outputs["Color"], b.inputs["Base Color"])
    b.inputs["Roughness"].default_value = rough
    m.diffuse_color = (*hex_rgb(base), 1)
    return m


def mat_wood(name, dark="#3b2516", light="#6b4a30"):
    m, nodes, links, b = _new_mat(name)
    tc = nodes.new("ShaderNodeTexCoord")
    mapping = nodes.new("ShaderNodeMapping")
    mapping.inputs["Scale"].default_value = (1.0, 1.0, 12.0)  # stretched grain
    wave = nodes.new("ShaderNodeTexWave")
    wave.wave_type = "BANDS"
    wave.inputs["Scale"].default_value = 3.0
    wave.inputs["Distortion"].default_value = 6.0
    wave.inputs["Detail"].default_value = 4.0
    ramp = nodes.new("ShaderNodeValToRGB")
    e = ramp.color_ramp.elements
    e[0].color = (*hex_rgb(dark), 1)
    e[1].color = (*hex_rgb(light), 1)
    links.new(tc.outputs["Object"], mapping.inputs["Vector"])
    links.new(mapping.outputs["Vector"], wave.inputs["Vector"])
    links.new(wave.outputs["Fac"], ramp.inputs["Fac"])
    links.new(ramp.outputs["Color"], b.inputs["Base Color"])
    b.inputs["Roughness"].default_value = 0.55
    m.diffuse_color = (*hex_rgb(light), 1)
    return m


def mat_concrete(name, base="#cfcac2"):
    m, nodes, links, b = _new_mat(name)
    tc = nodes.new("ShaderNodeTexCoord")
    noise = nodes.new("ShaderNodeTexNoise")
    noise.inputs["Scale"].default_value = 40.0
    noise.inputs["Detail"].default_value = 10.0
    ramp = nodes.new("ShaderNodeValToRGB")
    e = ramp.color_ramp.elements
    e[0].position, e[0].color = 0.35, (*hex_rgb("#a9a49c"), 1)
    e[1].position, e[1].color = 0.65, (*hex_rgb(base), 1)
    bump = nodes.new("ShaderNodeBump")
    bump.inputs["Strength"].default_value = 0.15
    links.new(tc.outputs["Object"], noise.inputs["Vector"])
    links.new(noise.outputs["Fac"], ramp.inputs["Fac"])
    links.new(ramp.outputs["Color"], b.inputs["Base Color"])
    links.new(noise.outputs["Fac"], bump.inputs["Height"])
    links.new(bump.outputs["Normal"], b.inputs["Normal"])
    b.inputs["Roughness"].default_value = 0.85
    m.diffuse_color = (*hex_rgb(base), 1)
    return m


def mat_tv_screen(name):
    m, nodes, links, b = _new_mat(name)
    nodes.remove(b)
    em = nodes.new("ShaderNodeEmission")
    em.inputs["Strength"].default_value = 1.6
    out = nodes["Material Output"]
    links.new(em.outputs["Emission"], out.inputs["Surface"])
    if TV_IMAGE:
        try:
            img = nodes.new("ShaderNodeTexImage")
            img.image = bpy.data.images.load(TV_IMAGE)
            links.new(img.outputs["Color"], em.inputs["Color"])
            return m
        except RuntimeError:
            print("TV_IMAGE could not be loaded, using gradient")
    tc = nodes.new("ShaderNodeTexCoord")
    sep = nodes.new("ShaderNodeSeparateXYZ")
    ramp = nodes.new("ShaderNodeValToRGB")
    e = ramp.color_ramp.elements
    e[0].position, e[0].color = 0.0, (*hex_rgb("#1a0b2e"), 1)
    mid = e.new(0.35)
    mid.color = (*hex_rgb("#7a3fa0"), 1)
    hz = e.new(0.5)
    hz.color = (*hex_rgb("#d77fd0"), 1)
    e[-1].position, e[-1].color = 1.0, (*hex_rgb("#2a1250"), 1)
    links.new(tc.outputs["Generated"], sep.inputs["Vector"])
    links.new(sep.outputs["Z"], ramp.inputs["Fac"])
    links.new(ramp.outputs["Color"], em.inputs["Color"])
    return m


def build_materials():
    M = {}
    M["marble_black"] = mat_marble("Marble Black", "#0d0d0f", "#b9b6b0", 0.12, 1.2)
    M["marble_floor"] = mat_marble("Marble Floor", "#e6e3de", "#a8a49d", 0.08, 0.6)
    M["marble_top"] = mat_marble("Marble Table", "#f2f2f0", "#c9c7c2", 0.1, 3.0)
    M["wood"] = mat_wood("Walnut")
    M["concrete"] = mat_concrete("Concrete")
    M["ceiling"] = mat_basic("Ceiling", "#d9d3c9", 0.9)
    M["white"] = mat_basic("Gloss White", "#e9e7e3", 0.25)
    M["grey_unit"] = mat_basic("Display Grey", "#b8b4ad", 0.6)
    M["gold"] = mat_basic("Gold", "#c9a24a", 0.25, 1.0)
    M["black"] = mat_basic("Black", "#0b0b0b", 0.4)
    M["black_metal"] = mat_basic("Black Metal", "#151515", 0.35, 1.0)
    M["glass"] = mat_basic("Glass", "#e8f0f0", 0.02, 0.0, transmission=1.0)
    M["sofa"] = mat_basic("Navy Velvet", "#1e2b44", 0.85)
    M["chair"] = mat_basic("Chair Brown", "#7a4a1d", 0.6)
    M["chair_seat"] = mat_basic("Chair Seat", "#5a3414", 0.8)
    M["text_dark"] = mat_basic("Text Dark", "#2b2b2b", 0.5)
    M["can"] = mat_basic("Paint Can", "#ecebe8", 0.3)
    M["bucket_green"] = mat_basic("Bucket Green", "#1f5a3a", 0.4)
    M["lid_orange"] = mat_basic("Lid Orange", "#e07a1f", 0.4)
    M["led"] = mat_emit("LED Warm", "#ffd9a0", 12.0)
    M["downlight"] = mat_emit("Downlight", "#fff1dc", 40.0)
    M["tv"] = mat_tv_screen("TV Screen")
    M["outside"] = mat_emit("Night Street", "#2c3240", 0.6)
    M["street"] = mat_basic("Street", "#4a4a4a", 0.7)
    return M


_color_cache = {}


def color_mat(hexcol, rough=0.5):
    key = (hexcol, rough)
    if key not in _color_cache:
        _color_cache[key] = mat_basic("Col " + hexcol, hexcol, rough)
    return _color_cache[key]


# ----------------------------------------------------------------------------
# Geometry helpers
# ----------------------------------------------------------------------------
def to_obj(name, bm, loc=(0, 0, 0), rot=(0, 0, 0), mat=None, parent=None, smooth=False):
    me = bpy.data.meshes.new(name)
    bm.to_mesh(me)
    bm.free()
    ob = bpy.data.objects.new(name, me)
    bpy.context.scene.collection.objects.link(ob)
    ob.location = loc
    ob.rotation_euler = rot
    if mat:
        me.materials.append(mat)
    if smooth:
        for p in me.polygons:
            p.use_smooth = abs(p.normal.z) < 0.5   # smooth sides, keep caps flat
    if parent:
        ob.parent = parent
    return ob


def box(name, size, loc, mat=None, rot=(0, 0, 0), bevel=0.0, parent=None):
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    bmesh.ops.scale(bm, vec=Vector(size), verts=bm.verts)
    ob = to_obj(name, bm, loc, rot, mat, parent)
    if bevel > 0:
        mod = ob.modifiers.new("Bevel", "BEVEL")
        mod.width = bevel
        mod.segments = 3
    return ob


def cyl(name, r, h, loc, mat=None, rot=(0, 0, 0), r2=None, seg=40, parent=None):
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, cap_tris=False, segments=seg,
                          radius1=r, radius2=r if r2 is None else r2, depth=h)
    return to_obj(name, bm, loc, rot, mat, parent, smooth=True)


def arc_solid(name, r_in, r_out, a0, a1, z0, z1, loc, mat=None, seg=48, parent=None, rot=(0, 0, 0)):
    """Curved wall segment between angles a0..a1 (radians) around loc."""
    bm = bmesh.new()
    rings = []
    for i in range(seg + 1):
        a = a0 + (a1 - a0) * i / seg
        c, s = math.cos(a), math.sin(a)
        rings.append([bm.verts.new((r * c, r * s, z))
                      for r, z in ((r_in, z0), (r_out, z0), (r_out, z1), (r_in, z1))])
    for i in range(seg):
        A, B = rings[i], rings[i + 1]
        for k in range(4):
            bm.faces.new((A[k], B[k], B[(k + 1) % 4], A[(k + 1) % 4]))
    bm.faces.new(rings[0][::-1])
    bm.faces.new(rings[-1])
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    ob = to_obj(name, bm, loc, rot, mat, parent)
    for p in ob.data.polygons:
        p.use_smooth = abs(p.normal.z) < 0.5
    return ob


def text(body, loc, rot, size, mat, extrude=0.005, align="LEFT", font_path=""):
    cu = bpy.data.curves.new(name="Text", type="FONT")
    cu.body = body
    cu.size = size
    cu.extrude = extrude
    cu.align_x = align
    cu.space_line = 0.85
    if font_path:
        try:
            cu.font = bpy.data.fonts.load(font_path)
        except RuntimeError:
            print("Font could not be loaded:", font_path)
    ob = bpy.data.objects.new("Text " + body.split("\n")[0], cu)
    bpy.context.scene.collection.objects.link(ob)
    ob.location = loc
    ob.rotation_euler = rot
    cu.materials.append(mat)
    return ob


def empty(name, loc, rot_z=0.0):
    ob = bpy.data.objects.new(name, None)
    bpy.context.scene.collection.objects.link(ob)
    ob.location = loc
    ob.rotation_euler = (0, 0, rot_z)
    return ob


# ----------------------------------------------------------------------------
# Room shell
# ----------------------------------------------------------------------------
def build_room(M):
    w = ROOM_X1 - ROOM_X0
    d = BACK_Y - FRONT_Y
    cx = (ROOM_X0 + ROOM_X1) / 2
    cy = (BACK_Y + FRONT_Y) / 2
    # floor + ceiling
    box("Floor", (w, d, 0.1), (cx, cy, -0.05), M["marble_floor"])
    box("Ceiling", (w, d, 0.1), (cx, cy, CEIL_Z + 0.05), M["ceiling"])
    # small ceiling step above the seating area, like the reference
    box("Ceiling Step", (3.4, 3.2, 0.08), (2.0, 3.2, CEIL_Z - 0.04), M["ceiling"])
    # back wall (concrete)
    box("Back Wall", (w, 0.1, CEIL_Z), (cx, BACK_Y + 0.05, CEIL_Z / 2), M["concrete"])

    # left: black marble brand wall with gold vertical inlays
    box("Marble Wall", (0.1, d, CEIL_Z), (ROOM_X0 - 0.05, cy, CEIL_Z / 2), M["marble_black"])
    y = FRONT_Y + 0.4
    while y < BACK_Y - 0.3:
        box("Gold Inlay", (0.012, 0.012, CEIL_Z), (ROOM_X0 + 0.006, y, CEIL_Z / 2), M["gold"])
        y += 0.55
    # warm LED cove along the top of the marble wall
    box("Marble LED", (0.02, d, 0.02), (ROOM_X0 + 0.03, cy, CEIL_Z - 0.03), M["led"])

    # brand lettering facing into the room (+X), reading toward the back
    text(f"{BRAND_LINE1}\n{BRAND_LINE2}", (ROOM_X0 + 0.04, 0.0, 2.25),
         (rad(90), 0, rad(90)), 0.6, M["gold"], extrude=0.03, font_path=BRAND_FONT)

    # right: glass shop front with black mullions
    gx = ROOM_X1
    box("Glass Front", (0.02, d, CEIL_Z), (gx, cy, CEIL_Z / 2), M["glass"])
    y = FRONT_Y
    while y <= BACK_Y + 0.01:
        box("Mullion", (0.06, 0.06, CEIL_Z), (gx, y, CEIL_Z / 2), M["black_metal"])
        y += 1.6
    box("Glass Head", (0.08, d, 0.1), (gx, cy, CEIL_Z - 0.05), M["black_metal"])
    # concrete column between back wall and glass
    box("Column", (0.4, 0.4, CEIL_Z), (gx - 0.2, BACK_Y - 0.2, CEIL_Z / 2), M["concrete"])

    # outside: street + dim night backdrop
    box("Street", (8, 14, 0.1), (gx + 4, cy, -0.1), M["street"])
    box("Night Backdrop", (0.1, 14, 8), (gx + 7, cy, 3), M["outside"])
    # neighbouring shop block seen through the glass
    box("Neighbour", (2.0, 0.3, 3.4), (gx + 2.5, BACK_Y + 0.6, 1.7), M["concrete"])


# ----------------------------------------------------------------------------
# Reception + wood shelving column
# ----------------------------------------------------------------------------
def build_reception(M):
    c = (-3.7, 2.45, 0)
    arc_solid("Counter Body", 1.55, 1.7, rad(-130), rad(5), 0.0, 1.02, c, M["white"])
    arc_solid("Counter Top", 1.5, 1.76, rad(-130), rad(5), 1.02, 1.07, c, M["white"])
    arc_solid("Counter Desk", 1.1, 1.5, rad(-130), rad(5), 0.72, 0.75, c, M["white"])
    arc_solid("Counter Plinth", 1.6, 1.65, rad(-130), rad(5), 0.0, 0.06, c, M["black"])

    # receptionist chair (white back peeking over the counter)
    ch = empty("Reception Chair", (-3.75, 1.85, 0), rad(-90))
    cyl("Chair Base", 0.28, 0.04, (0, 0, 0.02), M["black_metal"], parent=ch)
    cyl("Chair Stem", 0.03, 0.45, (0, 0, 0.25), M["black_metal"], parent=ch)
    box("Chair Seat", (0.48, 0.48, 0.08), (0, 0, 0.5), M["white"], bevel=0.03, parent=ch)
    box("Chair Back", (0.08, 0.5, 0.65), (-0.24, 0, 0.9), M["white"], bevel=0.035, parent=ch)


def build_wood_column(M):
    # slatted walnut panel in the back-left corner
    x0, x1 = ROOM_X0, -3.25
    box("Wood Panel", (x1 - x0, 0.06, CEIL_Z), ((x0 + x1) / 2, BACK_Y - 0.03, CEIL_Z / 2), M["wood"])
    x = x0 + 0.08
    while x < x1:
        box("Wood Slat", (0.025, 0.03, CEIL_Z), (x, BACK_Y - 0.075, CEIL_Z / 2), M["wood"])
        x += 0.1

    # open walnut shelf column
    sx0, sx1, depth = -3.25, -2.65, 0.42
    scx = (sx0 + sx1) / 2
    sy = BACK_Y - depth / 2
    box("Shelf Side L", (0.04, depth, CEIL_Z), (sx0, sy, CEIL_Z / 2), M["wood"])
    box("Shelf Side R", (0.04, depth, CEIL_Z), (sx1, sy, CEIL_Z / 2), M["wood"])
    box("Shelf Back", (sx1 - sx0, 0.02, CEIL_Z), (scx, BACK_Y - 0.01, CEIL_Z / 2), M["wood"])
    box("Shelf LED", (0.015, 0.015, CEIL_Z - 0.1), (sx1 - 0.03, sy - depth / 2 + 0.02, CEIL_Z / 2), M["led"])
    levels = [0.05, 0.45, 0.85, 1.25, 1.65, 2.05, 2.45, 2.85]
    for i, z in enumerate(levels):
        box("Shelf", (sx1 - sx0, depth, 0.035), (scx, sy, z), M["wood"])
        if 1 <= i <= 6 and i % 2 == 1:
            cyl("Shelf Can", 0.085, 0.2, (scx - 0.1, sy, z + 0.12), M["can"])
            cyl("Shelf Can", 0.085, 0.2, (scx + 0.12, sy, z + 0.12), M["can"])
        elif i == 4:
            cyl("Shelf Can", 0.1, 0.24, (scx, sy, z + 0.14), M["can"])


# ----------------------------------------------------------------------------
# "Exterior finishes" display units
# ----------------------------------------------------------------------------
SWATCHES = [
    ["#d88a7a", "#b3271f", "#7a3b1f", "#e2b42b", "#1d2433", "#ece6d6"],
    ["#5b8fbf", "#d9cbb0", "#7a4a1f", "#e0b52c", "#b3271f", "#2e6b3e"],
]
BOOKS = [
    ["#5a1e1e", "#2e6b52", "#1d6e66", "#e5dccb", "#c46a2a", "#1d2433"],
    ["#5a1e1e", "#8a2a2a", "#e5dccb", "#d1a24a", "#1d6e66", "#c9c3b5"],
]
DOT_COLORS = ["#7b3fa0", "#3f7fbf", "#e2b42b", "#c0282a"]
MAG_COLORS = ["#2f6fb0", "#e0a020", "#3b8f5a", "#c9452f", "#5aa0d0"]


def build_display_unit(M, cx, idx):
    W, D = 1.3, 0.45
    back = BACK_Y
    fy = back - D                       # front plane
    cy = back - D / 2
    g = M["grey_unit"]

    box("Unit Back", (W, 0.04, CEIL_Z), (cx, back - 0.02, CEIL_Z / 2), g)
    for s in (-1, 1):
        box("Unit Side", (0.03, D, 2.25), (cx + s * (W / 2 - 0.015), cy, 1.125), g)
    # header with title + colour dots
    box("Unit Header", (W, 0.06, CEIL_Z - 2.22), (cx, fy + 0.03, (CEIL_Z + 2.22) / 2), g)
    box("Header Lip", (W, D, 0.04), (cx, cy, 2.2), g)
    dot_x = cx - W / 2 + 0.1 if idx == 0 else cx + W / 2 - 0.1
    text_x = cx - W / 2 + 0.2 if idx == 0 else cx - W / 2 + 0.08
    text(DISPLAY_TEXT, (text_x, fy - 0.002, 2.48), (rad(90), 0, 0), 0.105, M["text_dark"])
    for k, col in enumerate(DOT_COLORS):
        cyl("Dot", 0.035, 0.01, (dot_x, fy - 0.004, 2.68 - k * 0.085),
            color_mat(col, 0.4), rot=(rad(90), 0, 0))

    # magazine shelf
    box("Mag Shelf", (W - 0.06, D, 0.03), (cx, cy, 1.78), g)
    for k in range(5):
        mx = cx - W / 2 + 0.17 + k * 0.24
        box("Magazine", (0.2, 0.28, 0.012), (mx, cy - 0.02, 1.81),
            color_mat(MAG_COLORS[(k + idx) % len(MAG_COLORS)], 0.3), rot=(rad(-12), 0, 0))

    # books (left half) + swatch board (right half)
    box("Mid Shelf", (W - 0.06, D, 0.03), (cx, cy, 1.15), g)
    bx = cx - W / 2 + 0.08
    for k, col in enumerate(BOOKS[idx]):
        wdt = 0.07 if k % 2 else 0.09
        box("Book", (wdt, 0.3, 0.6), (bx + wdt / 2, cy, 1.165 + 0.3), color_mat(col, 0.45))
        bx += wdt + 0.01
    sw0x = cx + 0.12
    box("Swatch Board", (0.5, 0.02, 0.6), (sw0x + 0.2, back - 0.1, 1.465), M["white"])
    for k, col in enumerate(SWATCHES[idx]):
        r, c = divmod(k, 2)
        box("Swatch", (0.16, 0.012, 0.15),
            (sw0x + 0.08 + c * 0.24, back - 0.115, 1.68 - r * 0.2), color_mat(col, 0.35))

    # sloped lower front panel
    box("Slope Panel", (W - 0.06, 0.03, 0.42), (cx, fy + 0.12, 0.93), g, rot=(rad(-25), 0, 0))

    # green bucket shelf
    box("Bucket Shelf", (W - 0.06, D, 0.03), (cx, cy, 0.6), g)
    for k in range(6):
        bxx = cx - W / 2 + 0.14 + k * 0.205
        cyl("Green Bucket", 0.07, 0.15, (bxx, cy - 0.04, 0.69), M["bucket_green"], r2=0.08)
        cyl("Bucket Rim", 0.082, 0.012, (bxx, cy - 0.04, 0.77), M["bucket_green"])

    # bottom shelf with white buckets + orange lids
    box("Bottom Shelf", (W - 0.06, D, 0.03), (cx, cy, 0.08), g)
    box("Kick", (W, 0.03, 0.08), (cx, fy + 0.015, 0.04), g)
    for k in range(4):
        bxx = cx - W / 2 + 0.18 + k * 0.31
        cyl("White Bucket", 0.085, 0.2, (bxx, cy - 0.03, 0.195), M["can"], r2=0.095)
        cyl("Orange Lid", 0.1, 0.025, (bxx, cy - 0.03, 0.31), M["lid_orange"])


# ----------------------------------------------------------------------------
# Feature wall: floating shelves, cans, TV
# ----------------------------------------------------------------------------
def build_feature_wall(M):
    x0, x1 = 0.35, 3.15
    cx = (x0 + x1) / 2
    depth = 0.24
    sy = BACK_Y - depth / 2
    shelves = [(1.98, 0), (2.38, 5), (2.78, 4)]   # (height, number of cans)
    for z, n in shelves:
        box("Floating Shelf", (x1 - x0, depth, 0.05), (cx, sy, z), M["wood"])
        box("Shelf LED", (x1 - x0 - 0.1, 0.02, 0.01), (cx, sy - 0.05, z - 0.03), M["led"])
        for k in range(n):
            px = x0 + (x1 - x0) * (k + 0.5) / n
            cyl("Can", 0.09, 0.24, (px, sy + 0.02, z + 0.145), M["can"])
            cyl("Can Lid", 0.091, 0.01, (px, sy + 0.02, z + 0.27), M["white"])

    # TV
    tv_x, tv_z = 1.75, 1.38
    box("TV Frame", (1.46, 0.05, 0.84), (tv_x, BACK_Y - 0.03, tv_z), M["black"])
    box("TV Screen", (1.42, 0.004, 0.8), (tv_x, BACK_Y - 0.057, tv_z), M["tv"])


# ----------------------------------------------------------------------------
# Furniture: sofa, tables, tulip chairs
# ----------------------------------------------------------------------------
def build_sofa(M):
    s = empty("Sofa", (1.25, 4.15, 0))
    m = M["sofa"]
    box("Sofa Base", (1.9, 0.78, 0.22), (0, 0, 0.32), m, bevel=0.04, parent=s)
    box("Sofa Cushion", (1.62, 0.6, 0.14), (0, -0.04, 0.5), m, bevel=0.05, parent=s)
    # channel-tufted back: a row of vertical pillows
    for k in range(9):
        x = -0.8 + k * 0.2
        box("Sofa Back Channel", (0.19, 0.16, 0.5), (x, 0.31, 0.7), m, bevel=0.06, parent=s)
    for sx in (-1, 1):
        box("Sofa Arm", (0.16, 0.76, 0.34), (sx * 0.9, 0.0, 0.55), m, bevel=0.07, parent=s)
        for sy in (-1, 1):
            leg = cyl("Sofa Leg", 0.022, 0.24, (sx * 0.85, sy * 0.3, 0.11), M["black_metal"],
                      r2=0.012, parent=s)
            leg.rotation_euler = (rad(-12 * sy), rad(12 * sx), 0)


def build_table(M, x, y):
    t = empty("Table", (x, y, 0))
    cyl("Table Top", 0.46, 0.03, (0, 0, 0.745), M["marble_top"], parent=t, seg=64)
    cyl("Table Stem", 0.035, 0.66, (0, 0, 0.4), M["white"], parent=t)
    cyl("Table Flare", 0.26, 0.1, (0, 0, 0.07), M["white"], r2=0.05, parent=t, seg=48)
    cyl("Table Foot", 0.27, 0.02, (0, 0, 0.01), M["white"], parent=t, seg=48)
    # a couple of brochures on top
    box("Brochure", (0.22, 0.3, 0.006), (-0.1, 0.05, 0.765), color_mat("#5aa0d0", 0.3),
        rot=(0, 0, rad(25)), parent=t)
    box("Brochure", (0.22, 0.3, 0.006), (0.12, -0.08, 0.765), color_mat("#ffffff", 0.3),
        rot=(0, 0, rad(-15)), parent=t)
    return t


def build_tulip_chair(M, x, y, face_to):
    ang = math.atan2(face_to[1] - y, face_to[0] - x)
    c = empty("Tulip Chair", (x, y, 0), ang)
    # local +X faces the table, the shell wraps around the back (-X)
    cyl("Chair Foot", 0.23, 0.02, (0, 0, 0.01), M["white"], parent=c, seg=40)
    cyl("Chair Flare", 0.22, 0.08, (0, 0, 0.06), M["white"], r2=0.04, parent=c)
    cyl("Chair Stem", 0.03, 0.32, (0, 0, 0.26), M["white"], parent=c)
    cyl("Chair Cup", 0.06, 0.06, (0, 0, 0.43), M["chair"], r2=0.24, parent=c)
    cyl("Chair Seat", 0.245, 0.06, (0, 0, 0.49), M["chair_seat"], parent=c)
    shell = arc_solid("Chair Shell", 0.23, 0.265, rad(70), rad(290), 0.44, 0.88, (0, 0, 0),
                      M["chair"], seg=40, parent=c)
    # flare the top of the shell outward a little
    for v in shell.data.vertices:
        if v.co.z > 0.6:
            f = 1.0 + (v.co.z - 0.6) * 0.35
            v.co.x *= f
            v.co.y *= f
    return c


def build_seating(M):
    build_sofa(M)
    tables = [(1.15, 2.95), (2.7, 2.7)]
    for tx, ty in tables:
        build_table(M, tx, ty)
    chairs = {
        0: [200, 300, 30],
        1: [140, 230, 320, 40],
    }
    for ti, angles in chairs.items():
        tx, ty = tables[ti]
        for a in angles:
            cx = tx + 0.68 * math.cos(rad(a))
            cy = ty + 0.68 * math.sin(rad(a))
            if cx < ROOM_X1 - 0.3:
                build_tulip_chair(M, cx, cy, (tx, ty))


# ----------------------------------------------------------------------------
# Lighting, camera, render
# ----------------------------------------------------------------------------
def build_lights(M):
    xs = [-3.3, -1.95, -0.6, 0.75, 2.1, 3.1]
    ys = [-0.6, 0.8, 2.2, 3.6, 4.4]
    for x in xs:
        for y in ys:
            if y == 4.4 and x > 0.2:
                continue
            cyl("Downlight Ring", 0.1, 0.012, (x, y, CEIL_Z - 0.006), M["black"], seg=32)
            cyl("Downlight", 0.07, 0.004, (x, y, CEIL_Z - 0.013), M["downlight"], seg=32)
            ld = bpy.data.lights.new("Spot", "SPOT")
            ld.energy = 70
            ld.spot_size = rad(110)
            ld.spot_blend = 0.6
            ld.color = (1.0, 0.93, 0.84)
            ld.shadow_soft_size = 0.05
            ob = bpy.data.objects.new("Spot", ld)
            bpy.context.scene.collection.objects.link(ob)
            ob.location = (x, y, CEIL_Z - 0.03)

    # soft fill so shadows are not too dark
    fill = bpy.data.lights.new("Fill", "AREA")
    fill.energy = 250
    fill.shape = "RECTANGLE"
    fill.size, fill.size_y = 6.0, 4.0
    fill.color = (1.0, 0.95, 0.9)
    ob = bpy.data.objects.new("Fill", fill)
    bpy.context.scene.collection.objects.link(ob)
    ob.location = (0, 1.5, CEIL_Z - 0.1)

    # warm grazing light on the marble wall and lettering
    graze = bpy.data.lights.new("Marble Graze", "AREA")
    graze.energy = 120
    graze.shape = "RECTANGLE"
    graze.size, graze.size_y = 0.1, 5.0
    graze.color = (1.0, 0.85, 0.6)
    ob = bpy.data.objects.new("Marble Graze", graze)
    bpy.context.scene.collection.objects.link(ob)
    ob.location = (ROOM_X0 + 0.4, 1.6, CEIL_Z - 0.1)
    ob.rotation_euler = (0, rad(-30), 0)

    world = bpy.context.scene.world or bpy.data.worlds.new("World")
    bpy.context.scene.world = world
    world.use_nodes = True
    bg = world.node_tree.nodes.get("Background")
    if bg:
        bg.inputs["Color"].default_value = (0.05, 0.055, 0.07, 1)
        bg.inputs["Strength"].default_value = 0.4


def build_camera():
    cam = bpy.data.cameras.new("Camera")
    cam.lens = 17
    cam.sensor_width = 36
    cam.clip_end = 100
    ob = bpy.data.objects.new("Camera", cam)
    bpy.context.scene.collection.objects.link(ob)
    ob.location = (-0.3, -1.35, 1.45)
    ob.rotation_euler = (rad(90), 0, 0)
    bpy.context.scene.camera = ob


def setup_render():
    sc = bpy.context.scene
    sc.render.engine = "CYCLES"
    sc.cycles.samples = RENDER_SAMPLES
    sc.cycles.use_denoising = True
    sc.render.resolution_x = RES_X
    sc.render.resolution_y = RES_Y
    sc.render.resolution_percentage = 100
    for vt in ("AgX", "Filmic"):
        try:
            sc.view_settings.view_transform = vt
            break
        except TypeError:
            continue
    sc.view_settings.exposure = 0.3


# ----------------------------------------------------------------------------
def main():
    clear_scene()
    M = build_materials()
    build_room(M)
    build_reception(M)
    build_wood_column(M)
    build_display_unit(M, -1.95, 0)
    build_display_unit(M, -0.65, 1)
    build_feature_wall(M)
    build_seating(M)
    build_lights(M)
    build_camera()
    setup_render()
    print("Turbolux showroom built: press F12 to render.")


if __name__ == "__main__":
    main()
