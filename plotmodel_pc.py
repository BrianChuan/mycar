from tensorflow.keras.utils import plot_model
from tensorflow.keras.models import load_model
from PIL import Image 
model = load_model('base_linear.h5',compile=False)
#pip3 install pydot-ng與graphviz
#win10要裝stable_windows_10_cmake_Release_x64_graphviz-install-2.46.0-win64.exe
#從https://graphviz.org/download/
plot_model(
    model,
    to_file="model.png",
    show_shapes=False,
    show_layer_names=True
)
pil_im = Image.open('model.png', 'r')
pil_im.show()