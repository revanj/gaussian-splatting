import matplotlib.pyplot as plt
from PIL import Image

# Load images
img1 = Image.open('data/79_recolmap/00010c81/output/test/ours_30000/gt/00000.png')
img2 = Image.open('data/79_recolmap/00010c81/output/test/ours_30000/renders/00000.png')
img3 = Image.open('data/79_recolmap_interp/00010c81/output/test/ours_30000/renders/00000.png')

# Create figure
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Display
axes[0].imshow(img1)
axes[0].set_title('GT')
axes[0].axis('off')

axes[1].imshow(img2)
axes[1].set_title('Without Interpolation')
axes[1].axis('off')

axes[2].imshow(img3)
axes[2].set_title('With Interpolation')
axes[2].axis('off')

plt.tight_layout()
plt.savefig('comparison.png', dpi=150, bbox_inches='tight')
plt.show()
