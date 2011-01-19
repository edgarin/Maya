import GlobalesI
########################################Creacion Menu Superior########################################################
from MayAPI.MayCBarraMenu import MayCBarraMenu

def CrearBarSup():
    Menu_Superior=MayCBarraMenu(GlobalesI.Pos_Surf1,GlobalesI.Tam_Surf1,'Horizontal',p_SubMenu=True)
    #Parametros a enviar para la creacion de los Botones del Menu Superior
    #Listas
    L_IDs_Botones=GlobalesI.Id_Btn_BarSu
    L_Imagenes=GlobalesI.Img_BarSu
    L_Mensajes=GlobalesI.Mnj_BarSu
    #Parametros Botones
    Tam_btnsu=GlobalesI.TamBtn_BarSu
    Pos_btnsu=GlobalesI.PosBtn_BarSu
            
    Menu_Superior.CreacionBotones(L_IDs_Botones,L_Imagenes,L_Mensajes,p_Posicion=Pos_btnsu,p_Tamano=Tam_btnsu,p_No_Menus=3)
    Menu_Superior.CColor(GlobalesI.Col_BarSu)        
    #Parametros a enviar para la creacion de los SubMenus del Menu Superior
    #Listas
    L_IdsBotones=GlobalesI.Id_BtnSubBarMen
    L_Imagenes=GlobalesI.Img_SubBarMen
    L_Mensajes=GlobalesI.Mnj_SubBarMen
    L_NoBotones=GlobalesI.Men_xSubBarMen
            
    Menu_Superior.CreacionSubBarraMenu(L_IdsBotones,L_Imagenes,L_Mensajes,L_NoBotones)
    return Menu_Superior

Menu_Superior=CrearBarSup()    