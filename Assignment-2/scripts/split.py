import os
import shutil
import random

# ===== CONFIG =====
SOURCE_DIR = "F:/CSE/4-2/DL/Assignments/Assignment-2/dataset/Five_Faces"
DEST_DIR = "F:/CSE/4-2/DL/Assignments/Assignment-2/dataset/Five_faces_split"

TRAIN_RATIO = 0.7
VAL_RATIO = 0.15
TEST_RATIO = 0.15

RANDOM_SEED = 42

# ==================

random.seed(RANDOM_SEED)

def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def split_dataset():
    classes = os.listdir(SOURCE_DIR)

    for cls in classes:
        class_path = os.path.join(SOURCE_DIR, cls)

        if not os.path.isdir(class_path):
            continue

        images = os.listdir(class_path)
        images = [img for img in images if img.lower().endswith(('.png', '.jpg', '.jpeg'))]

        random.shuffle(images)

        total = len(images)
        train_end = int(TRAIN_RATIO * total)
        val_end = train_end + int(VAL_RATIO * total)

        train_imgs = images[:train_end]
        val_imgs = images[train_end:val_end]
        test_imgs = images[val_end:]

        # Create directories
        for split in ['train', 'val', 'test']:
            create_dir(os.path.join(DEST_DIR, split, cls))

        # Copy files
        for img in train_imgs:
            shutil.copy(
                os.path.join(class_path, img),
                os.path.join(DEST_DIR, 'train', cls, img)
            )

        for img in val_imgs:
            shutil.copy(
                os.path.join(class_path, img),
                os.path.join(DEST_DIR, 'val', cls, img)
            )

        for img in test_imgs:
            shutil.copy(
                os.path.join(class_path, img),
                os.path.join(DEST_DIR, 'test', cls, img)
            )

        print(f"{cls}: {len(train_imgs)} train, {len(val_imgs)} val, {len(test_imgs)} test")

if __name__ == "__main__":
    split_dataset()
    print("✅ Dataset split complete!")