import numpy as np
import pycolmap


reconstruction = pycolmap.Reconstruction("data/79/00010c81/sparse/0")

images_by_name = sorted(reconstruction.images.items(), 
                        key=lambda x: x[1].name)

# Filter: keep every other image by name
images_to_remove = []
for idx, (img_id, img) in enumerate(images_by_name):
    if idx % 2 == 1:  # Remove odd indices when sorted by name
        images_to_remove.append(img_id)
        print(f"Removing: {img.name}")

# Remove images
for img_id in images_to_remove:
    reconstruction.deregister_image(img_id)

# Write filtered reconstruction
reconstruction.write("data/79_decimate/00010c81/sparse/0")

