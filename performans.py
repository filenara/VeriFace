import os
import cv2
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import peak_signal_noise_ratio as psnr
from tqdm import tqdm

real_dir = './results/veriface_pix2pix/test_20/images/'
fake_dir = './results/veriface_pix2pix/test_20/images/'

# Real ve fake eşleşmelerini bul
pairs = [(f, f.replace('real_B', 'fake_B')) for f in os.listdir(real_dir) if 'real_B' in f]

ssim_scores = []
psnr_scores = []

for real_name, fake_name in tqdm(pairs):
    real_path = os.path.join(real_dir, real_name)
    fake_path = os.path.join(fake_dir, fake_name)

    real = cv2.imread(real_path)
    fake = cv2.imread(fake_path)

    if real is None or fake is None:
        continue

    real = cv2.resize(real, (256, 256))
    fake = cv2.resize(fake, (256, 256))

    real_gray = cv2.cvtColor(real, cv2.COLOR_BGR2GRAY)
    fake_gray = cv2.cvtColor(fake, cv2.COLOR_BGR2GRAY)

    ssim_score = ssim(real_gray, fake_gray, data_range=255)
    psnr_score = psnr(real_gray, fake_gray, data_range=255)

    ssim_scores.append(ssim_score)
    psnr_scores.append(psnr_score)

print(f"🧾 Ortalama SSIM: {sum(ssim_scores)/len(ssim_scores):.4f}")
print(f"🧾 Ortalama PSNR: {sum(psnr_scores)/len(psnr_scores):.2f} dB")
