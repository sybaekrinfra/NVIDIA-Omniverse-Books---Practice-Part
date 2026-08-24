import asyncio
import os
import random
import carb.settings
import omni.replicator.core as rep
import omni.usd

OUTPUT_DIR = os.path.join(os.path.expanduser("~"), 
"_out_basic_writer_rand")
NUM_FRAMES = 20
SEED = 42
RT_SUBFRAMES = 4

def randomize_location(prim):
    position = (
        random.uniform(-1.0, 1.0),
        random.uniform(-1.0, 1.0),
        random.uniform(-1.0, 1.0),
    )
    rep.functional.modify.position(prim, position)

async def run_example_async():
    rep.orchestrator.stop()
    omni.usd.get_context().new_stage()
    rep.orchestrator.set_capture_on_play(False)
    random.seed(SEED)
    rep.set_global_seed(SEED)
    carb.settings.get_settings().set("/rtx/post/dlss/execMode", 2)
    rep.functional.create.xform(name="World")
    cube = rep.functional.create.cube(parent="/World", name="Cube")
    rep.functional.modify.semantics(cube, {"class": "box"}, mode="add")
    with rep.trigger.on_custom_event(event_name="randomize_dome_light_color"):
        rep.create.light(
            light_type="Dome",
            color=rep.distribution.uniform((0.2, 0.2, 0.2), (1.0, 1.0, 1.0)),
            intensity=1200,
        )
    camera = rep.functional.create.camera(
        position=(5.0, 5.0, 5.0),
        look_at=(0.0, 0.0, 0.0),
        parent="/World",
        name="Camera",
    )

    render_product = rep.create.render_product(camera, (640, 480))
    backend = rep.backends.get("DiskBackend")
    backend.initialize(output_dir=OUTPUT_DIR)
    writer = rep.writers.get("BasicWriter")

    writer.initialize(
        backend=backend,
        rgb=True,
        bounding_box_2d_tight=True,
        semantic_segmentation=True,
        colorize_semantic_segmentation=True,
        semantic_filter_predicate="class:box",
    )
    writer.attach(render_product)

    try:
        for frame_index in range(NUM_FRAMES):
            randomize_location(cube)

            rep.utils.send_og_event(event_name="randomize_dome_light_color")
            await rep.orchestrator.step_async(rt_subframes=RT_SUBFRAMES)
            print(f"Captured {frame_index + 1}/{NUM_FRAMES}")

        await rep.orchestrator.wait_until_complete_async()
        print(f"Output directory: {OUTPUT_DIR}")

    finally:
        writer.detach()
        render_product.destroy()

previous_task = globals().get("_replicator_dataset_task")
if previous_task is not None and not previous_task.done():
    print("Dataset generation is already running. Wait for completion.")
else:
    _replicator_dataset_task = asyncio.ensure_future(run_example_async())
