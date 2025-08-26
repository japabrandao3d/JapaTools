import bpy

class OBJECT_OT_select_empty_meshes(bpy.types.Operator):
    bl_idname = "object.select_empty_meshes"
    bl_label = "Select Empty Meshes"
    bl_description = "Selects mesh objects that have no vertices"

    def execute(self, context):
        bpy.ops.object.select_all(action='DESELECT')
        for obj in context.scene.objects:
            if obj.type == 'MESH' and len(obj.data.vertices) == 0:
                obj.select_set(True)
        self.report({'INFO'}, "Empty meshes selected.")
        return {'FINISHED'}
