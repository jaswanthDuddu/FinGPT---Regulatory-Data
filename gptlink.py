import openai

# Set up your OpenAI API key
openai.api_key = ''

# List of regulations and articles
regulations = [
    "(EU) 2019/834",
    "(EU) No 1095/2010",
    "(EU) No 1247/2012",
    "(EU) No 1248/2012",
    "(EU) No 1249/2012",
    "(EU) No 148/2013",
    "(EU) No 149/2013",
    "(EU) No 150/2013",
    "(EU) No 151/2013",
    "(EU) No 152/2013",
    "(EU) No 153/2013",
    "(EU) No 2015/2205",
    "(EU) No 2017/2155",
    "(EU) No 285/2014",
    "(EU) No 648/2012",
    "1 of EMIR",
    "11 of EMIR",
    "12 of the RTS on OTC derivatives",
    "12(4) of the RTS on OTC derivatives",
    "13 of the RTS on OTC derivatives",
    "14 of EMIR",
    "14 of EMIR 11(1) of RTS on CCP requirements",
    "14 of the RTS on OTC derivatives",
    "15 of the RTS on OTC derivatives",
    "16 of EMIR",
    "18 of EMIR",
    "2 of EMIR",
    "2 of RTS on IRS in G4 currencies",
    "2 of RTS on Third Country contracts",
    "2(10) and 89 of EMIR",
    "26 of EMIR",
    "28 of EMIR",
    "3, 4(2), 11(6) to 11(10) of EMIR",
    "35 of RTS on CCP requirement",
    "38 of EMIR",
    "39 of EMIR",
    "4 of EMIR",
    "41 of EMIR",
    "27(3) of RTS on CCP requirements",
    "42 of EMIR",
    "43(3) and 48(2) of EMIR",
    "45(4) of EMIR",
    "46 of EMIR",
    "37 of RTS on CCP requirements",
    "47 of EMIR",
    "48 of EMIR",
    "49 of EMIR",
    "4a and 10 of EMIR",
    "5 of the ITS on reporting to TR",
    "56 of EMIR",
    "6 of EMIR",
    "81 of EMIR",
    "9 of EMIR",
    "Art 2.1 of RTS on Third Country contracts",
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
    "Guideline and Recommendation 3(b)(v)"
]



# Function to retrieve links using GPT-4
def retrieve_links(law):
    models_list = ["gpt-4o", "gpt-4", "gpt-3.5-turbo"]
    prompt = f"Provide a link for {law}, please write in the format of \"Yes, (law) (LINK) or NO I am not able to provide a for the (law)\" (do not print any other format)"
    response = openai.ChatCompletion.create(
        model=models_list[2],
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=100
    )
    return response['choices'][0]['message']['content'].strip()

# Retrieve links for all regulations
f = open( "gptOutput.txt", "w")
for law in regulations:
    link = retrieve_links(law)
    f.write(f"Link for {law}: {link}\n")
    
f.close()
