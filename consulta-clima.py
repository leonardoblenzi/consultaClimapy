import requests
import json
from translate import Translator
cidade = input('Informe sua cidade: ')
#instanciando Translator e definindo como portugues
translator = Translator(to_lang="pt")
#fazendo a requisicao
req = requests.get('https://api.openweathermap.org/data/2.5/weather?q=' + cidade + '&appid=85740a2a5759559ee646b8bc120df7dc')
#convertendo texto para dicionario
dicionario = json.loads(req.text)
#passando valor do tempo e traduzindo
traducao = translator.translate(dicionario['weather'][0]['main'])
print(traducao)

temperatura = dicionario['main']['temp'] - 273
#formatando para 2 casas decimais
print('Temperatura: {:.2f}'.format(temperatura), 'ºC')
