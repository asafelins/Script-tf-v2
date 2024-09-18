from threading import Thread
import keyboard
import pyautogui
from time import sleep, time
import os
from datetime import datetime


class Automacao:
    def __init__(self, gui):
        self.executando = False
        self.contador = 0
        self.mechas = 0
        self.thread = None
        self.gui = gui 

    def iniciar_automacao(self):
        self.executando = True
        self.thread = Thread(target=self.automacao_loop)
        self.thread.start()

    def parar_automacao(self):
        self.gui.write("Script Finalizado...")
        self.executando = False
        self.gui.parar_automacao()
    
    
    def automacao_loop(self):

        def localizar_clicar_timeout(imagem, confidence=0.7, timeout=0.1, interval=0):
            tempo_inicio = time()

            while time() - tempo_inicio < timeout:
                posicao = pyautogui.locateCenterOnScreen(imagem, confidence=confidence)
                if posicao:
                    pyautogui.click(posicao)
                    braked = True
                    return True
                sleep(interval)




            
    

        def localizar_timeout(imagem, confidence=0.7, timeout=0.1, interval=0):
            tempo_inicio = time()

            while time() - tempo_inicio < timeout:
                posicao = pyautogui.locateCenterOnScreen(imagem, confidence=confidence)
                if posicao:
                    braked = True
                    return True
                sleep(interval)



        
        
        mechas_descartaveis = [
            "fotos/mecha80.png", "fotos/mecha100.png", 
            "fotos/mecha120.png", "fotos/mecha140.png", 
            "fotos/mecha160.png"
        ]

        
        mechas_aceitaveis = [
            "fotos/mecha180.png", "fotos/mecha200.png", 
            "fotos/mecha240.png", "fotos/mecha280.png", 
            "fotos/mecha315.png"
        ]

        braked = False
        contador = 0
        mechas = 0

        while self.executando:



            if keyboard.is_pressed('ctrl'):
                self.parar_automacao()

            braked = False
            contador += 1
            self.gui.write(f"Contador: {contador}")

            if contador == 3 and localizar_timeout("fotos/atualizar.png", confidence=0.7, timeout=0.1, interval=0):
                localizar_clicar_timeout("fotos/atualizar.png", confidence=0.7, timeout=0.1, interval=0)

            elif contador >= 7 and localizar_timeout("fotos/atualizar.png", confidence=0.7, timeout=0.1, interval=0) :
                localizar_clicar_timeout("fotos/atualizar.png", confidence=0.7, timeout=0.1, interval=0)
                pyautogui.moveTo(pyautogui.locateCenterOnScreen("fotos/center.png", confidence=0.7))
                sleep(0.5)
                pyautogui.scroll(-200)
                sleep(1)
                contador = 0

            elif contador >= 25:
                localizar_clicar_timeout("fotos/voltar2.png", confidence=0.7, timeout=0.1, interval=0)
                contador = 0

        
            elif localizar_timeout("fotos/recompensa.png", confidence=0.7, timeout=0.1, interval=0):
                self.gui.write("Coletando recompenca")
                localizar_clicar_timeout("fotos/recompensa.png", confidence=0.7, timeout=5, interval=0)
                localizar_clicar_timeout("fotos/botrec.png", confidence=0.6, timeout=5, interval=0)
                localizar_clicar_timeout("fotos/coletar.png", confidence=0.7, timeout=5, interval=0)
                braked = True

            elif localizar_timeout("fotos/ag.png", confidence=0.7, timeout=0.1, interval=0):
                localizar_clicar_timeout("fotos/ag.png", confidence=0.7, timeout=5, interval=0)             

                if localizar_timeout("fotos/erro.png", confidence=0.8, timeout=5, interval=0):
                    self.gui.write("Encontrei um erro e estou voltando")
                    localizar_clicar_timeout("fotos/voltar.png", confidence=0.7, timeout=5, interval=0)
                    braked = True
                
                elif localizar_timeout("fotos/atqgratis.png", confidence=0.6, timeout=5, interval=0):

                    if localizar_timeout("fotos/louva.png", confidence=0.7, timeout=1, interval=0): #verde 
                        self.gui.write("Verde")

                        if any(localizar_timeout(img, confidence=0.7, timeout=1, interval=0) for img in mechas_descartaveis):
                            self.gui.write("Mecha descartavel")
                            localizar_clicar_timeout("fotos/voltar.png", confidence=0.7, timeout=0.1, interval=0)
                            localizar_clicar_timeout("fotos/atualizar.png", confidence=0.7, timeout=0.1, interval=0) 

                            

                        
                        elif any(localizar_timeout(img, confidence=0.7, timeout=1, interval=0) for img in mechas_aceitaveis):
                            self.gui.write("Mecha aceitavel")
                            sleep(0.3)
                            localizar_clicar_timeout("fotos/atqgratis.png", confidence=0.6, timeout=1, interval=0)
                            localizar_clicar_timeout("fotos/equipe.png", confidence=0.7, timeout=1, interval=0)

                            if localizar_timeout("fotos/b2.png", confidence=0.8, timeout=1, interval=0):
                                localizar_clicar_timeout("fotos/b2.png", confidence=0.8, timeout=1, interval=0)
                                localizar_clicar_timeout("fotos/lutar.png", confidence=0.7, timeout=1, interval=0)
                                if localizar_timeout("fotos/erro2.png", confidence=0.8, timeout=1, interval=0):
                                    localizar_clicar_timeout("fotos/continuar2.png", confidence=0.7, timeout=1, interval=0)
                                    braked = True

                                else:
                                    localizar_clicar_timeout("fotos/skip.png", confidence=0.7, timeout=7, interval=0.2)
                                    localizar_clicar_timeout("fotos/continuar.png", confidence=0.6, timeout=1, interval=0)
                                    if localizar_timeout("fotos/botrec.png", confidence=0.6, timeout=1, interval=0):
                                        localizar_clicar_timeout("fotos/botrec.png", confidence=0.6, timeout=1, interval=0)
                                        localizar_clicar_timeout("fotos/coletar.png", confidence=0.7, timeout=1, interval=0)
                                        mechas += 1
                                        self.gui.write(f"Mecha:{mechas}")
                                        sleep(0.5)
                                        braked = True
                                    else:
                                        localizar_clicar_timeout("fotos/voltar.png", confidence=0.7, timeout=1, interval=0)
                                        mechas += 1
                                        self.gui.write(f"Mecha:{mechas}")
                                        sleep(0.5)
                                        braked = True

                            if localizar_timeout("fotos/b22.png", confidence=0.8, timeout=1, interval=0):
                                localizar_clicar_timeout("fotos/b22.png", confidence=0.8, timeout=1, interval=0)
                                localizar_clicar_timeout("fotos/lutar.png", confidence=0.7, timeout=1, interval=0)
                                if localizar_timeout("fotos/erro2.png", confidence=0.8, timeout=1, interval=0):
                                    localizar_clicar_timeout("fotos/continuar2.png", confidence=0.7, timeout=1, interval=0)
                                    braked = True

                                else:
                                    localizar_clicar_timeout("fotos/skip.png", confidence=0.7, timeout=7, interval=0.2)
                                    localizar_clicar_timeout("fotos/continuar.png", confidence=0.6, timeout=1, interval=0)
                                    if localizar_timeout("fotos/botrec.png", confidence=0.6, timeout=1, interval=0):
                                        localizar_clicar_timeout("fotos/botrec.png", confidence=0.6, timeout=1, interval=0)
                                        localizar_clicar_timeout("fotos/coletar.png", confidence=0.7, timeout=1, interval=0)
                                        mechas += 1
                                        self.gui.write(f"Mecha:{mechas}")
                                        sleep(0.5)
                                        braked = True
                                    else:
                                        localizar_clicar_timeout("fotos/voltar.png", confidence=0.7, timeout=1, interval=0)
                                        mechas += 1
                                        self.gui.write(f"Mecha:{mechas}")
                                        sleep(0.5)
                                        braked = True



                    elif localizar_timeout("fotos/kodiak.png", confidence=0.7, timeout=0.1, interval=0): #vermelho 
                        self.gui.write("Vermelho")

                        if any(localizar_timeout(img, confidence=0.7, timeout=0.1, interval=0) for img in mechas_descartaveis):
                            self.gui.write("Mecha descartavel")
                            localizar_clicar_timeout("fotos/voltar.png", confidence=0.7, timeout=0.1, interval=0)
                            localizar_clicar_timeout("fotos/atualizar.png", confidence=0.7, timeout=0.1, interval=0) 
                            

                        
                        elif any(localizar_timeout(img, confidence=0.7, timeout=0.1, interval=0) for img in mechas_aceitaveis):
                            self.gui.write("Mecha aceitavel")
                            sleep(0.3)
                            localizar_clicar_timeout("fotos/atqgratis.png", confidence=0.6, timeout=1, interval=0)
                            localizar_clicar_timeout("fotos/equipe.png", confidence=0.7, timeout=1, interval=0)

                            if localizar_timeout("fotos/b3.png", confidence=0.9, timeout=1, interval=0):
                                localizar_clicar_timeout("fotos/b3.png", confidence=0.9, timeout=1, interval=0)
                                localizar_clicar_timeout("fotos/lutar.png", confidence=0.7, timeout=1, interval=0)
                                if localizar_timeout("fotos/erro2.png", confidence=0.8, timeout=1, interval=0):
                                    localizar_clicar_timeout("fotos/continuar2.png", confidence=0.7, timeout=1, interval=0)
                                    braked = True

                                else:
                                    localizar_clicar_timeout("fotos/skip.png", confidence=0.7, timeout=7, interval=0.2)
                                    localizar_clicar_timeout("fotos/continuar.png", confidence=0.6, timeout=1, interval=0)
                                    if localizar_timeout("fotos/botrec.png", confidence=0.6, timeout=1, interval=0):
                                        localizar_clicar_timeout("fotos/botrec.png", confidence=0.6, timeout=1, interval=0)
                                        localizar_clicar_timeout("fotos/coletar.png", confidence=0.7, timeout=1, interval=0)
                                        mechas += 1
                                        self.gui.write(f"Mecha:{mechas}")
                                        sleep(0.5)
                                        braked = True
                                    else:
                                        localizar_clicar_timeout("fotos/voltar.png", confidence=0.7, timeout=1, interval=0)
                                        mechas += 1
                                        self.gui.write(f"Mecha:{mechas}")
                                        sleep(0.5)
                                        braked = True

                            if localizar_timeout("fotos/b33.png", confidence=0.9, timeout=1, interval=0):
                                localizar_clicar_timeout("fotos/b33.png", confidence=0.9, timeout=1, interval=0)
                                localizar_clicar_timeout("fotos/lutar.png", confidence=0.7, timeout=1, interval=0)
                                if localizar_timeout("fotos/erro2.png", confidence=0.8, timeout=1, interval=0):
                                    localizar_clicar_timeout("fotos/continuar2.png", confidence=0.7, timeout=1, interval=0)
                                    braked = True

                                else:
                                    localizar_clicar_timeout("fotos/skip.png", confidence=0.7, timeout=7, interval=0.2)
                                    localizar_clicar_timeout("fotos/continuar.png", confidence=0.6, timeout=1, interval=0)
                                    if localizar_timeout("fotos/botrec.png", confidence=0.6, timeout=1, interval=0):
                                        localizar_clicar_timeout("fotos/botrec.png", confidence=0.6, timeout=1, interval=0)
                                        localizar_clicar_timeout("fotos/coletar.png", confidence=0.7, timeout=1, interval=0)
                                        mechas += 1
                                        self.gui.write(f"Mecha:{mechas}")
                                        sleep(0.5)
                                        braked = True
                                    else:
                                        localizar_clicar_timeout("fotos/voltar.png", confidence=0.7, timeout=1, interval=0)
                                        mechas += 1
                                        self.gui.write(f"Mecha:{mechas}")
                                        sleep(0.5)
                                        braked = True


                        elif pyautogui.locateCenterOnScreen("fotos/mecha280.png", confidence=0.7) or pyautogui.locateCenterOnScreen("fotos/mecha315.png", confidence=0.7):
                            self.gui.write("Mecha aceitavel")
                            sleep(0.3)
                            localizar_clicar_timeout("fotos/atqgratis.png", confidence=0.6, timeout=1, interval=0)
                            localizar_clicar_timeout("fotos/equipe.png", confidence=0.7, timeout=1, interval=0)

                            if localizar_timeout("fotos/b5.png", confidence=0.9, timeout=1, interval=0):
                                localizar_clicar_timeout("fotos/b5.png", confidence=0.9, timeout=1, interval=0)
                                localizar_clicar_timeout("fotos/lutar.png", confidence=0.7, timeout=1, interval=0)
                                if localizar_timeout("fotos/erro2.png", confidence=0.8, timeout=1, interval=0):
                                    localizar_clicar_timeout("fotos/continuar2.png", confidence=0.7, timeout=1, interval=0)
                                    braked = True

                                else:
                                    localizar_clicar_timeout("fotos/skip.png", confidence=0.7, timeout=7, interval=0.2)
                                    localizar_clicar_timeout("fotos/continuar.png", confidence=0.6, timeout=1, interval=0)
                                    if localizar_timeout("fotos/botrec.png", confidence=0.6, timeout=1, interval=0):
                                        localizar_clicar_timeout("fotos/botrec.png", confidence=0.6, timeout=1, interval=0)
                                        localizar_clicar_timeout("fotos/coletar.png", confidence=0.7, timeout=1, interval=0)
                                        mechas += 1
                                        self.gui.write(f"Mecha:{mechas}")
                                        sleep(0.5)
                                        braked = True
                                    else:
                                        localizar_clicar_timeout("fotos/voltar.png", confidence=0.7, timeout=1, interval=0)
                                        mechas += 1
                                        self.gui.write(f"Mecha:{mechas}")
                                        sleep(0.5)
                                        braked = True

                            if localizar_timeout("fotos/b55.png", confidence=0.9, timeout=1, interval=0):
                                localizar_clicar_timeout("fotos/b55.png", confidence=0.9, timeout=1, interval=0)
                                localizar_clicar_timeout("fotos/lutar.png", confidence=0.7, timeout=1, interval=0)
                                if localizar_timeout("fotos/erro2.png", confidence=0.8, timeout=1, interval=0):
                                    localizar_clicar_timeout("fotos/continuar2.png", confidence=0.7, timeout=1, interval=0)
                                    braked = True

                                else:
                                    localizar_clicar_timeout("fotos/skip.png", confidence=0.7, timeout=7, interval=0.2)
                                    localizar_clicar_timeout("fotos/continuar.png", confidence=0.6, timeout=1, interval=0)
                                    if localizar_timeout("fotos/botrec.png", confidence=0.6, timeout=1, interval=0):
                                        localizar_clicar_timeout("fotos/botrec.png", confidence=0.6, timeout=1, interval=0)
                                        localizar_clicar_timeout("fotos/coletar.png", confidence=0.7, timeout=1, interval=0)
                                        mechas += 1
                                        self.gui.write(f"Mecha:{mechas}")
                                        sleep(0.5)
                                        braked = True
                                    else:
                                        localizar_clicar_timeout("fotos/voltar.png", confidence=0.7, timeout=1, interval=0)
                                        mechas += 1
                                        self.gui.write(f"Mecha:{mechas}")
                                        sleep(0.5)
                                        braked = True



                    elif localizar_timeout("fotos/simios.png", confidence=0.7, timeout=0.1, interval=0): #amarelo
                        self.gui.write("Amarelo")


                        if any(localizar_timeout(img, confidence=0.7, timeout=0.1, interval=0) for img in mechas_descartaveis):
                            self.gui.write("Mecha descartavel")
                            localizar_clicar_timeout("fotos/voltar.png", confidence=0.7, timeout=0.1, interval=0)
                            localizar_clicar_timeout("fotos/atualizar.png", confidence=0.7, timeout=0.1, interval=0) 
                            

                        
                        elif any(localizar_timeout(img, confidence=0.7, timeout=0.1, interval=0) for img in mechas_aceitaveis):
                            self.gui.write("Mecha aceitavel")
                            sleep(0.3)
                            localizar_clicar_timeout("fotos/atqgratis.png", confidence=0.6, timeout=1, interval=0)
                            localizar_clicar_timeout("fotos/equipe.png", confidence=0.7, timeout=1, interval=0)

                            if localizar_timeout("fotos/b3.png", confidence=0.9, timeout=1, interval=0):
                                localizar_clicar_timeout("fotos/b3.png", confidence=0.9, timeout=1, interval=0)
                                localizar_clicar_timeout("fotos/lutar.png", confidence=0.7, timeout=1, interval=0)
                                if localizar_timeout("fotos/erro2.png", confidence=0.8, timeout=1, interval=0):
                                    localizar_clicar_timeout("fotos/continuar2.png", confidence=0.7, timeout=1, interval=0)
                                    braked = True

                                else:
                                    localizar_clicar_timeout("fotos/skip.png", confidence=0.7, timeout=7, interval=0.2)
                                    localizar_clicar_timeout("fotos/continuar.png", confidence=0.6, timeout=1, interval=0)
                                    if localizar_timeout("fotos/botrec.png", confidence=0.6, timeout=1, interval=0):
                                        localizar_clicar_timeout("fotos/botrec.png", confidence=0.6, timeout=1, interval=0)
                                        localizar_clicar_timeout("fotos/coletar.png", confidence=0.7, timeout=1, interval=0)
                                        mechas += 1
                                        self.gui.write(f"Mecha:{mechas}")
                                        sleep(0.5)
                                        braked = True
                                    else:
                                        localizar_clicar_timeout("fotos/voltar.png", confidence=0.7, timeout=1, interval=0)
                                        mechas += 1
                                        self.gui.write(f"Mecha:{mechas}")
                                        sleep(0.5)
                                        braked = True

                            if localizar_timeout("fotos/b33.png", confidence=0.9, timeout=1, interval=0):
                                localizar_clicar_timeout("fotos/b33.png", confidence=0.9, timeout=1, interval=0)
                                localizar_clicar_timeout("fotos/lutar.png", confidence=0.7, timeout=1, interval=0)
                                if localizar_timeout("fotos/erro2.png", confidence=0.8, timeout=1, interval=0):
                                    localizar_clicar_timeout("fotos/continuar2.png", confidence=0.7, timeout=1, interval=0)
                                    braked = True

                                else:
                                    localizar_clicar_timeout("fotos/skip.png", confidence=0.7, timeout=7, interval=0.2)
                                    localizar_clicar_timeout("fotos/continuar.png", confidence=0.6, timeout=1, interval=0)
                                    if localizar_timeout("fotos/botrec.png", confidence=0.6, timeout=1, interval=0):
                                        localizar_clicar_timeout("fotos/botrec.png", confidence=0.6, timeout=1, interval=0)
                                        localizar_clicar_timeout("fotos/coletar.png", confidence=0.7, timeout=1, interval=0)
                                        mechas += 1
                                        self.gui.write(f"Mecha:{mechas}")
                                        sleep(0.5)
                                        braked = True
                                    else:
                                        localizar_clicar_timeout("fotos/voltar.png", confidence=0.7, timeout=1, interval=0)
                                        mechas += 1
                                        self.gui.write(f"Mecha:{mechas}")
                                        sleep(0.5)
                                        braked = True







                    elif localizar_timeout("fotos/grou.png", confidence=0.7, timeout=0.1, interval=0): #azul
                        self.gui.write("Azul") 


                        if any(localizar_timeout(img, confidence=0.7, timeout=0.1, interval=0) for img in mechas_descartaveis):
                            self.gui.write("Mecha descartavel")
                            localizar_clicar_timeout("fotos/voltar.png", confidence=0.7, timeout=0.1, interval=0)
                            localizar_clicar_timeout("fotos/atualizar.png", confidence=0.7, timeout=0.1, interval=0) 
                            

                        
                        elif any(localizar_timeout(img, confidence=0.7, timeout=0.1, interval=0) for img in mechas_aceitaveis):
                            self.gui.write("Mecha aceitavel")
                            sleep(0.3)
                            localizar_clicar_timeout("fotos/atqgratis.png", confidence=0.6, timeout=1, interval=0)
                            localizar_clicar_timeout("fotos/equipe.png", confidence=0.7, timeout=1, interval=0)

                            if localizar_timeout("fotos/b1.png", confidence=0.8, timeout=1, interval=0):
                                localizar_clicar_timeout("fotos/b1.png", confidence=0.8, timeout=1, interval=0)
                                localizar_clicar_timeout("fotos/lutar.png", confidence=0.7, timeout=1, interval=0)
                                if localizar_timeout("fotos/erro2.png", confidence=0.8, timeout=1, interval=0):
                                    localizar_clicar_timeout("fotos/continuar2.png", confidence=0.7, timeout=1, interval=0)
                                    braked = True

                                else:
                                    localizar_clicar_timeout("fotos/skip.png", confidence=0.7, timeout=7, interval=0.2)
                                    localizar_clicar_timeout("fotos/continuar.png", confidence=0.6, timeout=1, interval=0)
                                    if localizar_timeout("fotos/botrec.png", confidence=0.6, timeout=1, interval=0):
                                        localizar_clicar_timeout("fotos/botrec.png", confidence=0.6, timeout=1, interval=0)
                                        localizar_clicar_timeout("fotos/coletar.png", confidence=0.7, timeout=1, interval=0)
                                        mechas += 1
                                        self.gui.write(f"Mecha:{mechas}")
                                        sleep(0.5)
                                        braked = True
                                    else:
                                        localizar_clicar_timeout("fotos/voltar.png", confidence=0.7, timeout=1, interval=0)
                                        mechas += 1
                                        self.gui.write(f"Mecha:{mechas}")
                                        sleep(0.5)
                                        braked = True

                            if localizar_timeout("fotos/b11.png", confidence=0.8, timeout=1, interval=0):
                                localizar_clicar_timeout("fotos/b11.png", confidence=0.8, timeout=1, interval=0)
                                localizar_clicar_timeout("fotos/lutar.png", confidence=0.7, timeout=1, interval=0)
                                if localizar_timeout("fotos/erro2.png", confidence=0.8, timeout=1, interval=0):
                                    localizar_clicar_timeout("fotos/continuar2.png", confidence=0.7, timeout=1, interval=0)
                                    braked = True

                                else:
                                    localizar_clicar_timeout("fotos/skip.png", confidence=0.7, timeout=7, interval=0.2)
                                    localizar_clicar_timeout("fotos/continuar.png", confidence=0.6, timeout=1, interval=0)
                                    if localizar_timeout("fotos/botrec.png", confidence=0.6, timeout=1, interval=0):
                                        localizar_clicar_timeout("fotos/botrec.png", confidence=0.6, timeout=1, interval=0)
                                        localizar_clicar_timeout("fotos/coletar.png", confidence=0.7, timeout=1, interval=0)
                                        mechas += 1
                                        self.gui.write(f"Mecha:{mechas}")
                                        sleep(0.5)
                                        braked = True
                                    else:
                                        localizar_clicar_timeout("fotos/voltar.png", confidence=0.7, timeout=1, interval=0)
                                        mechas += 1
                                        self.gui.write(f"Mecha:{mechas}")
                                        sleep(0.5)
                                        braked = True





                    elif localizar_timeout("fotos/serpente.png", confidence=0.7, timeout=0.1, interval=0): #roxo 
                        self.gui.write("Roxo")

                        if any(localizar_timeout(img, confidence=0.7, timeout=0.1, interval=0) for img in mechas_descartaveis):
                            self.gui.write("Mecha descartavel")
                            localizar_clicar_timeout("fotos/voltar.png", confidence=0.7, timeout=0.1, interval=0)
                            localizar_clicar_timeout("fotos/atualizar.png", confidence=0.7, timeout=0.1, interval=0) 
                            

                        
                        elif any(localizar_timeout(img, confidence=0.7, timeout=0.1, interval=0) for img in mechas_aceitaveis):
                            self.gui.write("Mecha aceitavel")
                            sleep(0.3)
                            localizar_clicar_timeout("fotos/atqgratis.png", confidence=0.6, timeout=1, interval=0)
                            localizar_clicar_timeout("fotos/equipe.png", confidence=0.7, timeout=1, interval=0)
                            
                            if localizar_timeout("fotos/b3.png", confidence=0.9, timeout=1, interval=0):
                                localizar_clicar_timeout("fotos/b3.png", confidence=0.9, timeout=1, interval=0)
                                localizar_clicar_timeout("fotos/lutar.png", confidence=0.7, timeout=1, interval=0)
                                if localizar_timeout("fotos/erro2.png", confidence=0.8, timeout=1, interval=0):
                                    localizar_clicar_timeout("fotos/continuar2.png", confidence=0.7, timeout=1, interval=0)
                                    braked = True

                                else:
                                    localizar_clicar_timeout("fotos/skip.png", confidence=0.7, timeout=7, interval=0.2)
                                    localizar_clicar_timeout("fotos/continuar.png", confidence=0.6, timeout=1, interval=0)
                                    if localizar_timeout("fotos/botrec.png", confidence=0.6, timeout=1, interval=0):
                                        localizar_clicar_timeout("fotos/botrec.png", confidence=0.6, timeout=1, interval=0)
                                        localizar_clicar_timeout("fotos/coletar.png", confidence=0.7, timeout=1, interval=0)
                                        mechas += 1
                                        self.gui.write(f"Mecha:{mechas}")
                                        sleep(0.5)
                                        braked = True
                                    else:
                                        localizar_clicar_timeout("fotos/voltar.png", confidence=0.7, timeout=1, interval=0)
                                        mechas += 1
                                        self.gui.write(f"Mecha:{mechas}")
                                        sleep(0.5)
                                        braked = True

                            if localizar_timeout("fotos/b33.png", confidence=0.9, timeout=1, interval=0):
                                localizar_clicar_timeout("fotos/b33.png", confidence=0.9, timeout=1, interval=0)
                                localizar_clicar_timeout("fotos/lutar.png", confidence=0.7, timeout=1, interval=0)
                                if localizar_timeout("fotos/erro2.png", confidence=0.8, timeout=1, interval=0):
                                    localizar_clicar_timeout("fotos/continuar2.png", confidence=0.7, timeout=1, interval=0)
                                    braked = True

                                else:
                                    localizar_clicar_timeout("fotos/skip.png", confidence=0.7, timeout=7, interval=0.2)
                                    localizar_clicar_timeout("fotos/continuar.png", confidence=0.6, timeout=1, interval=0)
                                    if localizar_timeout("fotos/botrec.png", confidence=0.6, timeout=1, interval=0):
                                        localizar_clicar_timeout("fotos/botrec.png", confidence=0.6, timeout=1, interval=0)
                                        localizar_clicar_timeout("fotos/coletar.png", confidence=0.7, timeout=1, interval=0)
                                        mechas += 1
                                        self.gui.write(f"Mecha:{mechas}")
                                        sleep(0.5)
                                        braked = True
                                    else:
                                        localizar_clicar_timeout("fotos/voltar.png", confidence=0.7, timeout=1, interval=0)
                                        mechas += 1
                                        self.gui.write(f"Mecha:{mechas}")
                                        sleep(0.5)
                                        braked = True





                    elif localizar_timeout("fotos/grifo.png", confidence=0.7, timeout=0.1, interval=0): #cinza 
                        self.gui.write("Cinza")

                        if any(localizar_timeout(img, confidence=0.7, timeout=0.1, interval=0) for img in mechas_descartaveis):
                            self.gui.write("Mecha descartavel")
                            localizar_clicar_timeout("fotos/voltar.png", confidence=0.7, timeout=0.1, interval=0)
                            localizar_clicar_timeout("fotos/atualizar.png", confidence=0.7, timeout=0.1, interval=0) 
                            

                        
                        elif any(localizar_timeout(img, confidence=0.7, timeout=0.1, interval=0) for img in mechas_aceitaveis):
                            self.gui.write("Mecha aceitavel")
                            sleep(0.3)
                            localizar_clicar_timeout("fotos/atqgratis.png", confidence=0.6, timeout=1, interval=0)
                            localizar_clicar_timeout("fotos/equipe.png", confidence=0.7, timeout=1, interval=0)

                            if localizar_timeout("fotos/b3.png", confidence=0.9, timeout=1, interval=0):
                                localizar_clicar_timeout("fotos/b3.png", confidence=0.9, timeout=1, interval=0)
                                localizar_clicar_timeout("fotos/lutar.png", confidence=0.7, timeout=1, interval=0)
                                if localizar_timeout("fotos/erro2.png", confidence=0.8, timeout=1, interval=0):
                                    localizar_clicar_timeout("fotos/continuar2.png", confidence=0.7, timeout=1, interval=0)
                                    braked = True

                                else:
                                    localizar_clicar_timeout("fotos/skip.png", confidence=0.7, timeout=7, interval=0.2)
                                    localizar_clicar_timeout("fotos/continuar.png", confidence=0.6, timeout=1, interval=0)
                                    if localizar_timeout("fotos/botrec.png", confidence=0.6, timeout=1, interval=0):
                                        localizar_clicar_timeout("fotos/botrec.png", confidence=0.6, timeout=1, interval=0)
                                        localizar_clicar_timeout("fotos/coletar.png", confidence=0.7, timeout=1, interval=0)
                                        mechas += 1
                                        self.gui.write(f"Mecha:{mechas}")
                                        sleep(0.5)
                                        braked = True
                                    else:
                                        localizar_clicar_timeout("fotos/voltar.png", confidence=0.7, timeout=1, interval=0)
                                        mechas += 1
                                        self.gui.write(f"Mecha:{mechas}")
                                        sleep(0.5)
                                        braked = True

                            if localizar_timeout("fotos/b33.png", confidence=0.9, timeout=1, interval=0):
                                localizar_clicar_timeout("fotos/b33.png", confidence=0.9, timeout=1, interval=0)
                                localizar_clicar_timeout("fotos/lutar.png", confidence=0.7, timeout=1, interval=0)
                                if localizar_timeout("fotos/erro2.png", confidence=0.8, timeout=1, interval=0):
                                    localizar_clicar_timeout("fotos/continuar2.png", confidence=0.7, timeout=1, interval=0)
                                    braked = True

                                else:
                                    localizar_clicar_timeout("fotos/skip.png", confidence=0.7, timeout=7, interval=0.2)
                                    localizar_clicar_timeout("fotos/continuar.png", confidence=0.6, timeout=1, interval=0)
                                    if localizar_timeout("fotos/botrec.png", confidence=0.6, timeout=1, interval=0):
                                        localizar_clicar_timeout("fotos/botrec.png", confidence=0.6, timeout=1, interval=0)
                                        localizar_clicar_timeout("fotos/coletar.png", confidence=0.7, timeout=1, interval=0)
                                        mechas += 1
                                        self.gui.write(f"Mecha:{mechas}")
                                        sleep(0.5)
                                        braked = True
                                    else:
                                        localizar_clicar_timeout("fotos/voltar.png", confidence=0.7, timeout=1, interval=0)
                                        mechas += 1
                                        self.gui.write(f"Mecha:{mechas}")
                                        sleep(0.5)
                                        braked = True


            elif localizar_timeout("fotos/erro3.png", confidence=0.7, timeout=0.1, interval=0):
                self.gui.write("erro 3")
                localizar_clicar_timeout("fotos/voltar.png", confidence=0.7, timeout=5, interval=0)
                braked = True

            elif localizar_timeout("fotos/erro4.png", confidence=0.7, timeout=0.1, interval=0):
                self.gui.write("erro 5")
                localizar_clicar_timeout("fotos/voltar.png", confidence=0.7, timeout=5, interval=0)
                braked = True

            elif localizar_timeout("fotos/erro5.png", confidence=0.7, timeout=0.1, interval=0):
                self.gui.write("erro 4")
                localizar_clicar_timeout("fotos/voltar.png", confidence=0.7, timeout=5, interval=0)
                braked = True

            elif localizar_timeout("fotos/erro6.png", confidence=0.7, timeout=0.1, interval=0):
                self.gui.write("erro 6")
                localizar_clicar_timeout("fotos/evento2.png", confidence=0.7, timeout=5, interval=0) 
                localizar_clicar_timeout("fotos/evento1.png", confidence=0.7, timeout=5, interval=0) 
                localizar_clicar_timeout("fotos/mechachefe.png", confidence=0.7, timeout=5, interval=0)
                braked = True

            elif localizar_timeout("fotos/win.png", confidence=0.7, timeout=0.1, interval=0) or localizar_timeout("fotos/lose.png", confidence=0.7, timeout=0.1, interval=0):
                self.gui.write("win or lose")
                localizar_clicar_timeout("fotos/continuar.png", confidence=0.7, timeout=5, interval=0) 
                braked = True

            elif localizar_timeout("fotos/clubeinicial.png", confidence=0.8, timeout=0.1, interval=0):
                self.gui.write("tela inicial")
                localizar_clicar_timeout("fotos/clubeinicial.png", confidence=0.8, timeout=5, interval=0)
                localizar_clicar_timeout("fotos/evento2.png", confidence=0.7, timeout=5, interval=0)
                braked = True

            elif localizar_clicar_timeout("fotos/reconectar.png", confidence=0.7, timeout=0.1, interval=0):
                self.gui.write("reconectando")
                sleep(2)
                braked = True

            elif localizar_clicar_timeout("fotos/botrec.png", confidence=0.6, timeout=0.1, interval=0):
                self.gui.write("recompensa bugada")
                braked = True

            elif localizar_clicar_timeout("fotos/erro7.png", confidence=0.7, timeout=0.1, interval=0):
                self.gui.write("reconectando")
                sleep(2)
                braked = True

            elif localizar_timeout("fotos/mechalocal.png", confidence=0.7, timeout=0.1, interval=0):
                self.gui.write("mecha local")
                localizar_clicar_timeout("fotos/mechachefe.png", confidence=0.7, timeout=5, interval=0.0)
                braked = True