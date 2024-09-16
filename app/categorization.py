from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

# Load the trained image model
model = load_model('models/image_model.h5')

def categorize_complaint(image_data):
    # Preprocess the image
    img = image.load_img(image_data, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)

    # Predict the category
    prediction = model.predict(img_array)
    categories = ['Cleanliness', 'Damage', 'Staff Behavior']
    return categories[np.argmax(prediction)]
