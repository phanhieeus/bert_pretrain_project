from datasets import load_dataset
from transformer import BertTokenizerFast
import config



def load_and_preprocess_data():
    dataset = load_dataset("wikitext", "wikitext-2-raw-v1")
    tokenizer = BertTokenizerFast.from_pretrained(config.Config.MODEL_NAME)

    def tokenize_function(examples):
        return tokenizer(examples["text"], truncation=True, max_length=config.Config.MAX_SEQ_LENGTH)
    