from tensorflow.keras import model as tf

from know_your_witter.apiaccess import api


def generate_new_prediction(model):
    yield model.predict()


def clean_tweet(tweet):
    tweet = re.sub("@[A-Za-z0-9]+", "", tweet)
    tweet = re.sub(r"(?:\@|http?\://|https?\://|www)\S+", "", tweet)
    tweet = " ".join(tweet.split())
    tweet = ''.join(c for c in tweet if c not in emoji.UNICODE_EMOJI)
    tweet = tweet.replace("#", "").replace("_", " ")
    tweet = " ".join(w for w in nltk.wordpunct_tokenize(tweet) if w.lower() in words or not w.isalpha())
    return tweet


class Guesser:
    def __init__(self):
        self.dom_model_path = "know_your_witter/typer/models/16personalities-dominant-function-bert-small-uncased"
        self.sec_model_path = ""
        self.tweets = []
        self.dom_tokenizer, self.dom_model = self.load_model_tokenizer(self.dom_model_path)
        self.sec_tokenizer, self.sec_model = self.load_model_tokenizer(self.sec_model_path)
        self.max_length = 512

    def prepare_tweets(self, tweets):
        for tweet in tweets:
            self.tweets.append(clean_tweet(tweet))

    def load_model_tokenizer(self, model_path):
        return BertTokenizerFast.from_pretrained(model_path), \
               BertForSequenceClassification.from_pretrained(model_path, num_labels=8).to("cpu")

    def get_dom_prediction(self, text):
        inputs = self.dom_tokenizer(text, padding=True, truncation=True, max_length=self.max_length,
                                    return_tensors="pt").to("cpu")
        outputs = self.dom_model(**inputs)
        probs = outputs[0].softmax(1)
        return probs.argmax().item()

    def get_sec_prediction(self, text):
        inputs = self.sec_tokenizer(text, padding=True, truncation=True, max_length=self.max_length,
                                    return_tensors="pt").to("cpu")
        outputs = self.sec_model(**inputs)
        probs = outputs[0].softmax(1)
        return probs.argmax().item()

    def decode_prediction(self):


    def return_predicted(self):
        return


def guess_personality(username):
    #tweets = api.get_tweets(username)
    tweets = ['']
    guesser = Guesser()
    guesser.prepare_tweets(tweets)
    return "INTP"


if __name__ == '__main__':
    guess_personality("")
