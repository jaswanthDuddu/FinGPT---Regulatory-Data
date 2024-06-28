import openai

# Set your OpenAI API key
openai.api_key = "your-openai-api-key"

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
    {"role": "user", "content": full_question},
]

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=chat,
    max_tokens=100,
    temperature=0.6,
    top_p=0.9
)

print(response.choices[0].message['content'])
