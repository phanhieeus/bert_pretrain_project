# BERT Pretraining with Hugging Face

This project focuses on pretraining a BERT model using Hugging Face's `transformers` and `datasets` libraries. The training process follows the Masked Language Modeling (MLM) objective on a large text dataset.

## 📂 Project Structure
```
bert_pretrain_project/
│── data/                         # Contains datasets
│   ├── raw/                      # Raw downloaded data
│   ├── processed/                 # Processed and tokenized data
│── models/                        # Directory for trained models
│   ├── bert-pretrained/           # Saved pretrained model
│── src/                           # Source code
│   ├── dataset.py                 # Data processing scripts
│   ├── model.py                   # Model definition
│   ├── train.py                   # Training script
│   ├── evaluate.py                # Model evaluation
│   ├── config.py                  # Configuration settings
│── scripts/                        # Shell scripts for automation
│   ├── run_training.sh             # Script to launch training
│── notebooks/                      # Jupyter notebooks for data exploration
│── requirements.txt                # Required dependencies
│── README.md                       # Project documentation
```

## 🚀 Installation
Ensure you have Python 3.8+ and install dependencies:
```bash
pip install -r requirements.txt
```

## 📜 Data Preparation
Download and preprocess the dataset:
```bash
python src/dataset.py
```

## 🏋️ Training the Model
To start pretraining the BERT model, run:
```bash
python src/train.py
```

## 📊 Evaluating the Model
Evaluate the pretrained model:
```bash
python src/evaluate.py
```

## 🛠 Configuration
Modify `src/config.py` to adjust hyperparameters such as batch size, learning rate, and number of epochs.

## 💾 Saving and Loading the Model
The trained model is saved in `models/bert-pretrained/`. To load the model:
```python
from transformers import BertForMaskedLM
model = BertForMaskedLM.from_pretrained("models/bert-pretrained/")
```

## 📌 Notes
- The dataset used is Wikipedia.
- You can adjust hyperparameters in `config.py`.

## 📜 License
This project is licensed under the MIT License.

