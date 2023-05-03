import os
import openai
import argparse
import logging
import datetime

data_atual = datetime.datetime.today().strftime('%d/%m/%Y-%H:%M:%S')

# Configurar o registro para gravar em um arquivo
logging.basicConfig(filename='ask.log', level=logging.DEBUG)

parser = argparse.ArgumentParser(description='Parametros pela linha de comando')

parser.add_argument('--question', type=str, help='Pergunta a ser feita')

args = parser.parse_args() 

openai.api_key = os.getenv("OPENAI_API_KEY")

question = args.question  
if question != '':
    try:
        answer = openai.Completion.create(
                                model="text-davinci-003",
                                prompt=question,
                                max_tokens=2000,
                                temperature=0
                                    )
    except BaseException as exception:
        print(f"Exception Name: {type(exception).__name__}")
        print(f"Exception Desc: {exception}")
        logging.error('Erro na chamada da API da OpenAI')   

    r = answer.choices[0].text.strip()

    print(r)
    logging.info(data_atual + ": Pergunta: " + question + "\n" + "Resposta: " + r)
else:
    print('Pergunta não foi informada')