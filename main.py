import tensorflow as tf

print("TensorFlow version:", tf.__version__)
gpus = tf.config.list_physical_devices('GPU')
print("GPU devices:", gpus)

if not gpus:
    print("⚠️ TensorFlow does NOT see your GPU.")
else:
    print("✅ GPU is visible to TensorFlow!")
