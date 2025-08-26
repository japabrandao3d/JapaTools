import bpy

def add_scene_properties():
    bpy.types.Scene.source_object = bpy.props.PointerProperty(
        name="Source Object",
        type=bpy.types.Object,
        description="Object from which data will be transferred"
    )

    bpy.types.Scene.gap_threshold = bpy.props.FloatProperty(
        name="Gap Threshold",
        default=0.01,
        min=0.0,
        description="Distance threshold to detect gaps between vertices"
    )

    bpy.types.Scene.apply_first_vertex_group = bpy.props.BoolProperty(
        name="Apply First Vertex Group",
        default=False,
        description="Use the first vertex group of each object for the Data Transfer modifier"
    )

def remove_scene_properties():
    del bpy.types.Scene.source_object
    del bpy.types.Scene.gap_threshold
    del bpy.types.Scene.apply_first_vertex_group
