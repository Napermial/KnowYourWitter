from tensorflow.keras import model as tf

from know_your_witter.apiaccess import api


def load_model_tokenizer(model_path):
    logging.info( f"model from {model_path} loaded")
    return BertTokenizerFast.from_pretrained(model_path), \
           BertForSequenceClassification.from_pretrained(model_path, num_labels=8).to("cpu")


class Guesser:
    def __init__(self):
        self.dom_model_path = os.path.abspath('../typer/models/16personalities-dominant-function-bert-small-uncased')
        self.sec_model_path = os.path.abspath('../typer/models/16personalities-secondary-function-bert-small-uncased')
        self.tweets = []
        self.dom_tokenizer, self.dom_model = load_model_tokenizer(self.dom_model_path)
        self.sec_tokenizer, self.sec_model = load_model_tokenizer(self.sec_model_path)
        self.max_length = 512
        self.predicted = self.predict_type()

    def prepare_tweets(self, tweets):
        logging.info( "Preparing tweets...")
        for tweet in tweets:
            tweet = p.clean(tweet)
            self.tweets.append(tweet)

    def get_dom_prediction(self):
        logging.info( "dominant function input is being tokenized")
        inputs = self.dom_tokenizer(' '.join(self.tweets), padding=True, truncation=True, max_length=self.max_length,
                                    return_tensors="pt").to("cpu")
        logging.info("dominant function is being predicted")
        outputs = self.dom_model(**inputs)
        probs = outputs[0].softmax(1)
        return probs.argmax().item()

    def get_sec_prediction(self):
        logging.info("secondary function input is being tokenized")
        inputs = self.sec_tokenizer(' '.join(self.tweets), padding=True, truncation=True, max_length=self.max_length,
                                    return_tensors="pt").to("cpu")
        outputs = self.sec_model(**inputs)
        logging.info( "dominant function is being predicted")
        probs = outputs[0].softmax(1)
        return probs

    def predict_type(self):
        primary_function = self.get_dom_prediction()
        logging.info( f"User is a {primary_function} primary function user")
        secondary = self.get_sec_prediction()[0]
        logging.info(f"User is a {secondary} secondary function user")
        if primary_function == 0:
            if secondary[5] > secondary[7]:
                return "ESFP"
            return "ESTP"
        elif primary_function == 1:
            if secondary[4] > secondary[6]:
                return "ISFJ"
            return "ISTJ"
        elif primary_function == 2:
            if secondary[5] > secondary[7]:
                return "ENFP"
            return "ENTP"
        elif primary_function == 3:
            if secondary[4] > secondary[6]:
                return "INFJ"
            return "INTJ"
        elif primary_function == 4:
            if secondary[3] > secondary[1]:
                return "ENFJ"
            return "ESFJ"
        elif primary_function == 5:
            if secondary[0] > secondary[2]:
                return "ISFP"
            return "INFP"
        elif primary_function == 6:
            if secondary[3] > secondary[1]:
                return "ENTJ"
            return "ESTJ"
        elif primary_function == 7:
            if secondary[0] > secondary[2]:
                return "ISTP"
            return "INTP"


def guess_personality(username):
    tweets = api.get_tweets(username)
    guesser = Guesser()
    guesser.prepare_tweets(tweets)
    return guesser.predicted
