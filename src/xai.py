import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

@tf.custom_gradient
def guidedRelu(x):
  def grad(dy):
    return tf.cast(dy>0,"float32") * tf.cast(x>0, "float32") * dy
  return tf.nn.relu(x), grad

def visualize(model, input_img, layer_name):

  gb_model = tf.keras.models.Model(
      inputs = [model.inputs],    
      outputs = [model.get_layer(layer_name).output]
  )
  layer_dict = [layer for layer in gb_model.layers[1:] if hasattr(layer,'activation')]

  for layer in layer_dict:
    if layer.activation == tf.keras.activations.relu:
      layer.activation = guidedRelu

  with tf.GradientTape() as tape:
      inputs = tf.expand_dims(input_img, axis=0)
      tape.watch(inputs)
      outputs = gb_model(inputs)[0]
  grads = tape.gradient(outputs, inputs)[0]

  # Calculate GradCAM
  weights = tf.reduce_mean(grads, axis=(0, 1))
  grad_cam = np.ones(outputs.shape[0: 2], dtype = np.float32)
  for i, w in enumerate(weights):
      grad_cam += w * outputs[:, :, i]

  # GradCAM
  grad_cam_img = cv2.resize(grad_cam.numpy(), (224, 224))
  grad_cam_img = np.maximum(grad_cam_img, 0)
  heatmap = (grad_cam_img - grad_cam_img.min()) / (grad_cam_img.max() - grad_cam_img.min())
  grad_cam_img = cv2.applyColorMap(np.uint8(255*heatmap), cv2.COLORMAP_JET)
  output_image = cv2.addWeighted(cv2.cvtColor(input_img.numpy().astype('uint8'), cv2.COLOR_RGB2BGR), 0.5, grad_cam_img, 1, 0)

  # Guided Backpropagation
  guided_back_prop = grads
  gb_viz = np.dstack((
              guided_back_prop[:, :, 0],
              guided_back_prop[:, :, 1],
              guided_back_prop[:, :, 2],
          ))       
  gb_viz -= np.min(gb_viz)
  gb_viz /= gb_viz.max()

  return output_image, gb_viz