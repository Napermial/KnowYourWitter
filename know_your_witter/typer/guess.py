from tensorflow.keras import model as tf

from know_your_witter.apiaccess import api


def clean_tweet(tweet):
    tweet = re.sub("@[A-Za-z0-9]+", "", tweet)
    tweet = re.sub(r"(?:\@|http?\://|https?\://|www)\S+", "", tweet)
    tweet = " ".join(tweet.split())
    tweet = ''.join(c for c in tweet if c not in emoji.UNICODE_EMOJI)
    tweet = tweet.replace("#", "").replace("_", " ")
    tweet = " ".join(w for w in nltk.wordpunct_tokenize(tweet) if w.lower() in tweet or not w.isalpha())
    return tweet


def load_model_tokenizer(model_path):
    return BertTokenizerFast.from_pretrained(model_path), \
           BertForSequenceClassification.from_pretrained(model_path, num_labels=8).to("cpu")


class Guesser:
    def __init__(self):
        self.dom_model_path = "models/16personalities-dominant-function-bert-small-uncased"
        self.sec_model_path = "models/16personalities-secondary-function-bert-small-uncased"
        self.tweets = []
        self.dom_tokenizer, self.dom_model = load_model_tokenizer(self.dom_model_path)
        self.sec_tokenizer, self.sec_model = load_model_tokenizer(self.sec_model_path)
        self.max_length = 512
        self.predicted = self.predict_type()

    def prepare_tweets(self, tweets):
        for tweet in tweets:
            self.tweets.append(clean_tweet(tweet))

    def get_dom_prediction(self):
        inputs = self.dom_tokenizer(' '.join(self.tweets), padding=True, truncation=True, max_length=self.max_length,
                                    return_tensors="pt").to("cpu")
        outputs = self.dom_model(**inputs)
        probs = outputs[0].softmax(1)
        return probs.argmax().item()

    def get_sec_prediction(self):
        inputs = self.sec_tokenizer(' '.join(self.tweets), padding=True, truncation=True, max_length=self.max_length,
                                    return_tensors="pt").to("cpu")
        outputs = self.sec_model(**inputs)
        probs = outputs[0].softmax(1)
        return probs

    def predict_type(self):
        primary_function = self.get_dom_prediction()
        secondary = self.get_sec_prediction()
        if primary_function == 0:
            if secondary.item()[5] > secondary.item()[7]:
                return "ESFP"
            return "ESTP"
        elif primary_function == 1:
            if secondary.item()[4] > secondary.item()[6]:
                return "ISFJ"
            return "ISTJ"
        elif primary_function == 2:
            if secondary.item()[5] > secondary.item()[7]:
                return "ENFP"
            return "ENTP"
        elif primary_function == 3:
            if secondary.item()[4] > secondary.item()[6]:
                return "INFJ"
            return "INTJ"
        elif primary_function == 4:
            if secondary.item()[3] > secondary.item()[1]:
                return "ENFJ"
            return "ESFJ"
        elif primary_function == 5:
            if secondary.item()[0] > secondary.item()[2]:
                return "ISFP"
            return "INFP"
        elif primary_function == 6:
            if secondary.item()[3] > secondary.item()[1]:
                return "ENTJ"
            return "ESTJ"
        elif primary_function == 7:
            if secondary.item()[0] > secondary.item()[2]:
                return "ISTP"
            return "INTP"


def guess_personality(username):
    tweets = api.get_tweets(username)
    guesser = Guesser()
    guesser.prepare_tweets(tweets)
    return guesser.predicted


if __name__ == '__main__':
    guess_personality("")
