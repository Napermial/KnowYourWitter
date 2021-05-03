# import tensorflow.keras as tf

from know_your_witter.apiaccess import api


def generate_new_prediction(model):
    yield model.predict()


class Guesser:
    def __init__(self):
        self.model = self.load_model("this", "that")

    def structure_data(self):
        pass

    def load_model(self, inputs, outputs):
        return tf.Model(inputs=inputs, outputs=outputs)

    def return_predicted(self):
        return


def guess_personality(username):
    api.get_tweets(username)
    guesser = Guesser()
    guesser.structure_data()
    return "INTP"


if __name__ == '__main__':
    guess_personality("jani")
