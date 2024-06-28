import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

device = "cuda" # or "cpu"
model_path = "ibm-granite/granite-34b-code-instruct"
tokenizer = AutoTokenizer.from_pretrained(model_path)
# drop device_map if running on CPU
model = AutoModelForCausalLM.from_pretrained(model_path, device_map=device)
model.eval()

question = "What be the followin' in finance and business? Abbreviations: "
list_of_abb = [
    "EMIR", "SFTR", "RTS on reporting", "ITS on reporting", "RTS on registration",
    "RTS on data quality", "RTS on data access", "RTS on organisation requirements",
    "CFI code", "CM", "CP", "CP on RTS/ITS", "FR on RTS/ITS", "CPMI", "EC", "ECB",
    "EEA", "ERR", "ESCB", "EU", "FIRDS", "FSB", "IOSCO", "ISIN", "LEI", "ISO", "MIC",
    "NCA", "OJ", "RSE", "SWIFT", "TR", "UTI", "XML", "XSD", "ESRB", "UCITS", "EBA",
    "EIOPA", "TFEU", "IORP", "AIF", "AIFM", "AIFMD", "CCP", "CSD", "CICI", "CT",
    "EMIR", "ESMA", "ETD", "FC", "FC+", "FX", "MiFID", "MTF", "NCA", "NFC", "NFC+",
    "NFC-", "OTC", "Q&A", "RTS", "SPV", "TR", "UTI", "DORA", "ESA", "TPP", "TPRM",
    "CSP", "CTPPs", "JOF", "NIS2", "PSD2", "CSIRTs", "ENISA", "PSTN", "POTS", "TLPT",
    "G-SIIs", "O-SIIs", "BIA", "JON", "EGBPI", "RSB", "SFD", "MFF", "OLAF", "CIISI-EU",
    "CSIRTS", "T2S", "TIPS", "FMIs", "SSM", "TIBER-EU", "TCT", "DOI", "DG AGRI",
    "EGTOP", "SCA", "INSEE", "RRF", "SDGs", "RP", "EMU", "CSOs", "NRRPs", "OCS",
    "EPPO", "CPSR", "DCMA", "ACO", "CAR", "CAP"
]

full_question = question + ', '.join(list_of_abb)

chat = [
    { "role": "user", "content": full_question },
]
chat = tokenizer.apply_chat_template(chat, tokenize=False, add_generation_prompt=True)

# tokenize the text
input_tokens = tokenizer(chat, return_tensors="pt")

# transfer tokenized inputs to the device
for i in input_tokens:
    input_tokens[i] = input_tokens[i].to(device)

# generate output tokens
output = model.generate(**input_tokens, max_new_tokens=100)

# decode output tokens into text
output = tokenizer.batch_decode(output)

# loop over the batch to print, in this example the batch size is 1
for i in output:
    print(i)
