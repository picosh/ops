import sys
import glob
from PIL import Image
from transformers import pipeline
import torch

CGREEN = '\033[92m'
CYELLOW = '\033[93m'
CRED = '\033[91m'
CEND = '\033[0m'

def images(root_dir):
    count = 0
    for filename in glob.iglob(root_dir + '**/*.jpg', recursive=True):
        #if count == 10:
        #    return
        try:
            img = Image.open(filename)
            yield img, filename
        except Exception as err:
            print("failed to open file", err)
        count += 1
    print(f"scanned {count} images")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise Exception(f"{CRED}error!: please provide root image folder{CEND}")
    root_dir = sys.argv[1]
    print(f"root_dir {root_dir}")
    threshold = 0.6

    print(f"failure threshold is set to {threshold:.4f}")

    print("loading model")
    device = 'cuda:0' if torch.cuda.is_available() else 'cpu'
    classify = pipeline(
        "image-classification",
        model="Falconsai/nsfw_image_detection",
        device=device,
    )

    print("scanning images")
    for img, filename in images(root_dir):
        result = None
        try:
            result = classify(img)
        except Exception as err:
            # print(f"{CYELLOW}err{CEND} (score:n/a) {filename} {err}")
            continue

        nsfw_score = result[1]["score"]
        score_read = '%.4f' % nsfw_score
        if nsfw_score > threshold:
            print(f"{CRED}failed{CEND} (score:{score_read}) {filename}")
        else:
            # print(f"{CGREEN}passed{CEND} (score:{score_read}) {filename}")
            pass
