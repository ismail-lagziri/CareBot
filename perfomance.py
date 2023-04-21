import matplotlib.pyplot as plt
import pickle

with open('hist.pkl', 'rb') as f:
    hist = pickle.load(f)

plt.plot(hist['accuracy'])
plt.title('Model Accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.show()

plt.plot(hist['loss'])
plt.title('Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.show()
