from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
import numpy as np
import os

api_key = "odOapYuOvNuGqkQ4fMlR2N4mn98mH3Mc"
model = "mistral-large-latest"

client = MistralClient(api_key=api_key)

question="What does the following abbreviation stand for each in US finance and regulation? Only provide the full form of the abbreviation.\n"

abbreviations = [
    "(AWC)",
    "(AUV)",
    "(AMT)",
    "(APY)",
    "(AML)",
    "(AUM)",
    "(AIR)",
    "(ADTV)",
    "(CAPM)",
    "(COD)",
    "(CAGR)",
    "(CPI)",
    "(CDSC)",
    "(CE)",
    "(CNS)",
    "(DVP), (RVP)",
    "(DMA)",
    "(DCF)",
    "(DDM)",
    "(DPS)",
    "(DBA)",
    "(DCA)",
    "(DK)",
    "(DUI), (DWI)",
    "(EED)",
    "(FMCE)",
    "(FFI)",
    "(GTC)",
    "(GSEs)",
    "(GDP), (GNP)",
    "(GARP)",
    "(GMIB, GMWB, GMAB)",
    "(IOI)",
    "(IT)",
    "(IRC)",
    "(LOA), (LOI)",
    "(LBO)",
    "(LIHTC)",
    "(MICR)",
    "(MPID)",
    "(MNPI)",
    "(M&A)",
    "(M&E)",
    "(NBBO), (NBB), (NBO)",
    "(NAV)",
    "(OBA)",
    "(OTC)",
    "(POD)",
    "(PCE)",
    "(PII)",
    "(PPI)",
    "(POP)",
    "(REMIC)",
    "(RSL)",
    "(RMD)",
    "(ROA)",
    "(SIE)",
    "(SCP)",
    "(TIF)",
    "(TBE), (TIC)",
    "(TBA)",
    "(TAM)",
    "(TOD)",
    "(VWAP)",
    "(WAM)",
    "(WKSI)",
    "(WORM)"
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


