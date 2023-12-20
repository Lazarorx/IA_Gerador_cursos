import tensorflow as tf
from sklearn.model_selection import train_test_split

def definir_modelo(input_size, output_size):
    modelo = tf.keras.Sequential([
        tf.keras.layers.Dense(256, activation='relu', input_dim=input_size),
        tf.keras.layers.Dropout(0.5),  # Para prevenir overfitting
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(output_size, activation='softmax')  # Número de classes dinâmico
    ])
    
    # Compilar o modelo
    modelo.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    
    return modelo

def treinar_modelo(modelo, X_train, y_train, X_val, y_val, epochs=15):
    # Treinamento do modelo
    modelo.fit(X_train, y_train, epochs=epochs, validation_data=(X_val, y_val), verbose=0)

def avaliar_modelo(modelo, X_test, y_test):
    # Avaliação do modelo
    y_prob = modelo.predict(X_test)
    y_pred = tf.argmax(y_prob, axis=1).numpy()
    return y_pred

