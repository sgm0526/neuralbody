import argparse
import os
import numpy as np
import subprocess
from PIL import Image
import rembg



if __name__=="__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument('data_dir', type=str, )
    args = parser.parse_args()

    if not os.path.isdir(os.path.join(args.data_dir,'image/')):
        raise FileExistsError
    output_dir = os.path.join(args.data_dir, 'image_wobg')
    subprocess.call(['rembg', '-p', os.path.join(args.data_dir,'image/'), output_dir])
    output_fore_list = os.listdir(output_dir)
    mask_dir = os.path.join(args.data_dir,'mask_255')
    os.makedirs(mask_dir, exist_ok=True)

    for fore in output_fore_list:
        fore_img = Image.open(os.path.join(output_dir, fore))
        Image.fromarray(np.array(fore_img)[:, :, 3]).save(os.path.join(mask_dir, fore))
