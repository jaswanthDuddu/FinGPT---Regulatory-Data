from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
import numpy as np
import os

api_key = "3kdwhzd9I8MxqcElNqXxCnMKKn0yd0t9"
model = "mistral-large-latest"

client = MistralClient(api_key=api_key)

question="What does the following abbreviation stand for each in finance and business? Only provide the full form of the abbreviation.\n"

abbreviations = [
    "XSD", "ESRB", "UCITS", "EBA", "EIOPA", "TFEU", "IORP", "AIF", "AIFM", 
    "AIFMD", "CCP", "CSD", "CICI", "CT", "EMIR", "ESMA", "ETD", "FC", "FC+", 
    "FX", "MiFID", "MTF", "NCA", "NFC", "NFC+", "NFC-", "OTC", "Q&A", "RTS", 
    "SPV", "TR", "UTI", "DORA", "ESA", "TPP", "TPRM", "CSP", "CTPPs", "JOF", 
    "NIS2", "PSD2", "CSIRTs", "ENISA", "PSTN", "POTS", "TLPT", "G-SIIs", 
    "O-SIIs", "BIA", "JON", "EGBPI", "RSB", "SFD", "MFF", "OLAF", "CIISI-EU", 
    "CSIRTs", "T2S", "TIPS", "FMIs", "SSM", "TIBER-EU", "TCT", "DOI", 
    "DG AGRI", "EGTOP", "SCA", "INSEE", "RRF", "SDGs", "RP", "EMU", "CSOs", 
    "NRRPs", "OCS", "EPPO", "CPSR", "DCMA", "ACO", "CAR", "CAP"
]

full_question = question + ', '.join(abbreviations)

chat_response = client.chat(
    model=model,
    messages=[ChatMessage(role="user", content = full_question)]
)

"""


ESRB
"""

print(chat_response.choices[0].message.content)
