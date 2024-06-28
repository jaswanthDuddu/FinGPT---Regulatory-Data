import transformers
import torch

model_id = "meta-llama/Meta-Llama-3-70B-Instruct"

pipeline = transformers.pipeline(
    "text-generation",
    model=model_id,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device_map="auto",
)

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

messages = [
    {"role": "user", "content": full_question},
]

terminators = [
    pipeline.tokenizer.eos_token_id,
    pipeline.tokenizer.convert_tokens_to_ids("")
]

outputs = pipeline(
    messages,
    max_new_tokens=256,
    eos_token_id=terminators,
    do_sample=True,
    temperature=0.6,
    top_p=0.9,
)
print(outputs[0]["generated_text"][-1])
