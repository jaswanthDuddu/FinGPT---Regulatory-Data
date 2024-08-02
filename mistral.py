from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
import numpy as np
import os

api_key = "API_KEY"
model = "mistral-large-latest"

client = MistralClient(api_key=api_key)

question= f"Provide a link for the following laws, please write in the format of \"Yes, (law) (LINK) or NO I am not able to provide a for the (law)\" (do not print any other format)"



abbreviations = [
    "Article 10 of EMIR",
    "Article 16 of the ESMA Regulation",
    "Article 19(6) of Directive 2004/39/EC",
    "Article 2(3)(g) of AIFMD",
    "Article 2(7) of EMIR",
    "Article 2(8) of EMIR",
    "Article 29(2) of the ESMA Regulation",
    "Article 2a of EMIR",
    "Article 3(2) of the AIFMD",
    "Article 4(1)(14) of Directive 2004/39/EC",
    "Article 4(1)(b)(ii) of EMIR",
    "Article 4(2)(b) of RTS 2017/2155 amending RTS 149/2013",
    "Article 4(3) of EMIR",
    "Article 4(4) of EMIR and Article 2 RTS on OTC derivatives",
    "Article 4(9) of MiFID",
    "Article 42 of the AIFMD",
    "Article 4a(2) and Article10(2) for FCs and NFCs",
    "Article 4a(3) and Article 10(3) of EMIR",
    "Article 61(3) of AIFMD",
    "Article 61(4) of AIFMD",
    "Article 9(1) of EMIR",
    "Articles 9(1b) to (1d) EMIR",
    "Directive 2006/48/EC",
    "Directive 2006/49/EC",
    "Directive 2011/61/EU",
    "Directive 83/349/EEC",
    "European Commission FAQ no. 14",
    "Guideline and Recommendation 3(b)(v)",
    "Article 1(c) of the Commission Delegated Regulation",
    "article 13(2) of EMIR",
    "article 16b(5) of the ESMA Regulation",
    "EMIR Article 11(2)",
    "Article 4(1)(b)(ii) of EMIR",
    "Article 4(2)(b) of RTS 2017/2155",
    "Article 4(4)(b) of the Indirect Clearing RTS",
    "(EU) No 285/2014",
    "Article 46(1) of EMIR",
    "Articles 48(5) of EMIR",
    "Articles 48(6) of EMIR",
    "Article 39(7) of EMIR",
    "Article 47(3) of EMIR",
    "Settlement Finality Directive (98/26/EC)",
    "Article 47 Model Validation (of the Commission delegated Regulation",
    "Commission Delegated Regulation No 2013/153",
    "Recital 13 of Commission Delegated Regulation No 2013/153",
    "Commission Regulation (EC) No 1126/2008"
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







