import gradio as gr
import torch
from PIL import Image
from torchvision import transforms
import sys
import os

# Pix2Pix klasörünü yol olarak ekle
sys.path.append('./pytorch-CycleGAN-and-pix2pix')

from models import create_model
from util.util import tensor2im
from types import SimpleNamespace

# Opt ayarlarını elle oluşturuyoruz
opt = SimpleNamespace(
    dataroot='./demo_inputs',
    name='veriface_pix2pix',
    model='pix2pix',
    direction='AtoB',
    epoch='60',
    no_dropout=True,
    serial_batches=True,
    num_threads=0,
    batch_size=1,
    load_size=256,
    crop_size=256,
    preprocess='resize_and_crop',
    input_nc=3,
    output_nc=3,
    isTrain=False,
    checkpoints_dir='./checkpoints',
    results_dir='./results',
    netG='unet_256',
    netD='basic',
    norm='batch',
    init_type='normal',
    init_gain=0.02,
    verbose=False,
    ngf=64,
    ndf=64,
    load_iter=0,
    gpu_ids=[0]
)

# Modeli oluştur ve yükle
model = create_model(opt)
model.setup(opt)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Görsel tahmin fonksiyonu
def predict(sketch):
    sketch = sketch.convert("RGB").resize((256, 256))
    transform = transforms.ToTensor()
    sketch_tensor = transform(sketch).unsqueeze(0) * 2 - 1
    model.set_input({
    'A': sketch_tensor.to(device),
    'B': sketch_tensor.to(device),
    'A_paths': ['dummy_path']  # <-- HATA BURADAN GELİYORDU
})

    model.test()
    visuals = model.get_current_visuals()
    fake_B = tensor2im(visuals['fake_B'])
    return Image.fromarray(fake_B)

# Gradio arayüzü
demo = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil", label="🖊️ Eskiz Yükle"),
    outputs=gr.Image(type="pil", label="🧠 Üretilen Yüz"),
    title="🎨 VeriFace - Sketch2Face AI",
    description="Pix2Pix tabanlı model ile yüklediğiniz çizimden gerçekçi bir yüz oluşturun."
)

if __name__ == "__main__":
    demo.launch()
