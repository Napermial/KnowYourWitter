import tensorflow.keras as tf


class Guesser():
    def structure_data():
        pass

    def create_model(inputs, outputs):
        return tf.Model(inputs=inputs, outputs=outputs)

    def generate_new_prediction(self, model):
        yield model.predict()


if __name__ == '__main__':
    g = Guesser()
