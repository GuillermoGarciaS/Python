import tensorflow as tf
from tensorflow.keras import datasets, layers, models

#Cargamos el dataset CIFAR10
(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()

#Normalizamos el valor de los pixeles entre 0 & 1
train_images, test_images = train_images / 255.0, test_images / 255.0

#Definimos el modelo de arquitectura
model = models.Sequential()
model.add(layers.Conv2D(64, (3, 3), activation = 'relu', input_shape = (32, 32, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation = 'relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation = 'relu'))
model.add(layers.Flatten())
model.add(layers.Dense(256, activation = 'relu'))
model.add(layers.Dense(128, activation = 'relu'))
model.add(layers.Dense(10, activation = 'relu'))

#Pasamos a agregar capas densas encima
model.add(layers.Flatten())
model.add(layers.Dense(64, activation = 'relu'))
model.add(layers.Dense(10))

#Ahora compilaremos y entrenaremos al modelo
model.compile(optimizer = tf.keras.optimizers.Adam(learning_rate = 0.0001), 
              loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits = True),
              metrics = ['accuracy'])

history = model.fit(train_images, train_labels, epochs = 10,
                    validation_data = (test_images, test_labels))

#Evaluaremos el modelo
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose = 2)

print('\nTest acurracy: ', test_acc)