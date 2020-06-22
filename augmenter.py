# Importing necessary library
import Augmentor
# Passing the path of the image directory
path_to_data = "C:\\Users\\ASUS\\Documents\\project object detect\\sample"
p = Augmentor.Pipeline(path_to_data)

# Defining augmentation parameters and generating 5 samples
p.flip_left_right(1)
p.black_and_white(1)
p.rotate(0.3, 10, 10)
p.skew(0.4, 0.5)
p.zoom(probability = 1, min_factor = 1.1, max_factor = 1.5)
p.sample(8)
