from pymongo import MongoClient
from datetime import datetime
import subprocess
from status import server_status

server_status()

#conectar ao mongo
client = MongoClient("mongodb://localhost:27017")

#deletar database
# client.drop_database("your_database_name")

# #criar coleção
# # database.create_collection('criar_collection')

#conectar ao banco
db = client['banco_estudo']

#coletar a coleção
collection = db['connect_python']

# #insert um dado
# collection.insert_one({'nome':'Saulo'})

# insert vários dados
# data = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# dados = [
#     {'nome':'Melzinha','idade': 5, 'genero': 'F', 'data_criacao': data},
#     {'nome':'Luiz','idade': 68, 'genero': 'M', 'data_criacao': data},
#     {'nome':'Cícera','idade': 58, 'genero': 'F', 'data_criacao': data}
# ]
# collection.insert_many(dados)

# #deletar um dado
# print(collection.delete_one({'nome':'Saulo'}).deleted_count)

#encontrar e deletar dados
dado = collection.find().sort('nome', 1)
#usar sort pra ordenar, 1 para crescente e -1 para decrescente
for dados in dado:
    print(dados)
    try:
        nome = dados['nome']
        # if nome:
        #     print(collection.delete_many({'nome':nome}).deleted_count)
    except Exception as err:
        print(err)
        
# encontrar e atualizar dados ou collections
# dado = collection.find()
# for dados in dado:
#     try:
#         nome = dados['nome']
#         # try:
#         #     rg = dados['RG']
#         # except:
#         #     rg = False
#         # if rg != False:
#         if nome != 'Melzinha':
#             update = collection.update_one({'nome': nome}, {'$set': {'Morador':True}})
#             print(update.modified_count)
#             # print(collection.delete_many({'nome':nome}).deleted_count)
#         else:
#             update = collection.update_one({'nome': nome}, {'$set': {'Cachorro':True}})
#             print(update.modified_count)
#     except Exception as err:
#         print(err)

#deletar uma coleção
# collection.drop()



