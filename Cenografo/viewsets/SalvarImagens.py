import threading
import cv2
import numpy as np
from PIL import Image
import redis
from django.conf import settings
import sys, os


class SalvarImagens(threading.Thread):

    def __init__(self,chave_,host_,porta_):
        self.lista_de_cartas = []
        self.chave = chave_
        self.redis_conectado = redis.Redis(host=host_, port=porta_)
        threading.Thread.__init__(self)

    def run(self):
        self.registrar()

    def registrar(self): 
        index = 0
        while index <= 10:
            if self.redis_conectado.llen(self.chave) > 0:
                imagem_dict = self.redis_conectado.lpop(self.chave)
                if(imagem_dict):
                    imagem_dict = eval(imagem_dict)
                    imagem = imagem_dict['imagem']
                    imagem_caminho = "".join([ settings.MEDIA_URL,imagem_dict['data_dia']])
                    imagem_nome = "".join([imagem_dict['data_hora'],'.jpg'])
                    self.criar_pastas(imagem_caminho)
                    self.salvar_imagem(imagem,imagem_caminho,imagem_nome)
                    print('--',self.redis_conectado.llen(self.chave))
                    index = 0
            index += 1
        print('fim da tread: SalvarImagens')

    def criar_pastas(self,caminho):
        try:
            os.makedirs("".join([sys.path[0],caminho]))
        except OSError:
            pass

    def salvar_imagem(self,imagem,caminho,nome):
        caminho_imagem = "".join([sys.path[0],caminho,'/',nome])
        decoded = cv2.imdecode(np.frombuffer(imagem, np.uint8), 1)
        Image.fromarray(decoded).save(caminho_imagem)

    
        
