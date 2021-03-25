from render import mosaic
import os





def main():
    rootpath = os.getcwd()
    nomdossier = os.path.join("download")
    image_name = "test.jpg"

    folder_path = os.path.join(rootpath,nomdossier)

    image_path = os.path.join(rootpath,image_name)
    
    #nombre de carreau
    image_carreaux = 200
    #taille du carreau
    carreau_size = 30

    mosaic(folder_path,image_path,image_carreaux,carreau_size)

    

main()

