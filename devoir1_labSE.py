"""
Le premier prgramme en Python
* utilisation des arguments de la lignne de commande
* les listes et la fonction map
* les threads
* le logger
@author Dragos STOICA
@version 0.4
@date 16.feb.2014
"""

import sys, threading, logging, os

class Bonjour(threading.Thread):
    def __init__(self, personne):
        threading.Thread.__init__(self)
        self.personne = personne
    def run(self):
        #Fonction polie - saluer une personne
        print "Bonjour %(personne)s!\n" % \
          {"personne":self.personne},
        logging.info("Bonjour : %(personne)s" %{"personne":self.personne})
   
def utilisation():
    #Affichage mode d'utilisation
    print """
          Le programme doit etre appelle avec minimum 1 argument:
          python bonjour_listes.py Dragos
          """

def main(argv=None):
    working_dir = os.path.dirname(os.path.abspath(__file__)) + os.path.sep
    #Configurez le logging pour ecrire dans un fichier texte
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                        filename = working_dir + 'bonjour.log',
                        level=logging.INFO)    
    logging.info("Main start")
    
    #La boucle principale
    if argv is None:
        argv = sys.argv

    if len(argv) == 1:
        utilisation()
    else:
        #Argument 1 est le nom de fichier avec un noms per ligne
        mmeThread = []
        mThread = []
        mlleThread = []
        with open(working_dir + argv[1],'r') as f:
            #Dites bonjour a chaque personne de fichier
            for ligne in f:
                if ligne[0:2] == "M.":
                    mThread.append(Bonjour(ligne.strip(' \r\n')))
                else:
                    if ligne[0:4] == "Mme.":
                        mme_local = Bonjour(ligne.strip(' \r\n'))
                        mmeThread.append(mme_local)
                        #mme_local.start()
                    else:
                         mlle_local = Bonjour(ligne.strip(' \r\n'))
                         mlleThread.append(mlle_local) 
        for mlle in mlleThread:
            mlle.start()
            mlle.join()
        for mme in mmeThread:
            mme.start()
            mme.join()
        for m in mThread:
            m.start()
            m.join()
    logging.info("Main stop")                
    return 0

if __name__ == "__main__":
    #Simplifiez la logique de la fonction principale
    sys.exit(main())
