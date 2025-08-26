import bpy

class OBJECT_OT_batch_rename_selected(bpy.types.Operator):
    bl_idname = "object.batch_rename_selected"
    bl_label = "Batch Rename Selected"
    bl_description = "Renames selected mesh objects with a numbered suffix and matches their data name"

    def execute(self, context):
        name_count = {}
        for obj in context.selected_objects:
            if obj.type == 'MESH':
                base_name = obj.name.split('_')[0]
                name_count[base_name] = name_count.get(base_name, 0) + 1
                new_name = f"{base_name}_{name_count[base_name]:03d}"
                obj.name = obj.data.name = new_name
        self.report({'INFO'}, "Batch rename completed.")
        return {'FINISHED'}
