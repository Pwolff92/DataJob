import streamlit as st
import numpy as np

st.sidebar.title("DataJob :chart_with_downwards_trend:")
st.sidebar.subheader("Menu") 
pages =["Exploration","Preprocessing","Visualisation","Modelisation", "Conclusion","Test"]
page = st.sidebar.radio("",options = pages)
st.sidebar.info(
    "Projet Datajob - Promotion Bootcamp mars 2023"
    "\n\n"
    "Participants:"
    "\n\n"
    "David DUBOIS ()"
    "\n\n"
    "Pauline WOLFF\n(https://www.linkedin.com/in/pauline-wolff-27b003100/) "
    "\n\n"
    "Sophie LAUSSEL\n() "
    )


if page == pages[0]:  
    st.title(':orange[Exploration] :mag_right:')
    st.header("Description")
    st.markdown('''<div style="text-align: justify;">
                L’objectif de ce projet est de comprendre à l’aide des données les différents profils techniques qui se sont créés dans l’industrie de la Data. 
                Plus exactement, nous mènerons une analyse poussée des tâches effectuées ainsi que des outils utilisés pour chaque poste afin d’établir des 
                ensembles de compétences et outils correspondant à chaque poste du monde de la Data.
                Ce projet s’intègre parfaitement dans notre projet professionnel. Il nous permet d’analyser, à l’aide de ce jeu de données, 
                les différents métiers de la data à travers les logiciels utilisés, les études des différents profils etc. 
                </div>''', unsafe_allow_html=True)

    st.header("Objectifs")
    st.markdown('''<div style="text-align: justify;">
                Les principaux objectifs qui ressortent à travers ce sondages sont :
                analyser les profils des utilisateurs de Kaggle au regard de leur métier ;
                élaborer un modèle permettant d’identifier le métier data le plus adapté, en fonction des compétences des personnes souhaitant intégrer le domaine de la data.
                </div>''', unsafe_allow_html=True)    

    st.header("Cadre")
    st.markdown('''<div style="text-align: justify;">
                Le jeu de données sur lequel nous allons travailler provient d’un sondage créé et lancé en 2020 sur 171 pays. Il était destiné aux personnes inscrites sur le site Kaggle (plateforme web interactive qui propose des compétitions d'apprentissage automatique en science des données). Au total, 20 000 personnes ont été sondées. L’étude est essentiellement centrée sur le Machine Learning.
                Nous procédons à une première analyse visuelle sur le jeu de données (à l’aide de la méthode info de pandas). Ainsi le jeu de données se décompose de la manière suivante : 355 colonnes, l’intégralité des données sont de type objet donc qualitatives, il y a 20 037 entrées.
                D’un point de vue technique, toutes les données étant de type qualitatif, nous aurons un important travail d’encodage à faire pour pouvoir traiter la donnée. 
                </div>''', unsafe_allow_html=True) 
    
    st.header("Variable cible :dart:")
    st.markdown('''<div style="text-align: justify;">
                La variable cible de notre projet correspond aux métiers de la data dans le jeu de données, cette variable se nomme “titre’, que nous appellerons Métier, terme plus explicite. Nous étudierons les 4 métiers : 
                Data Scientest
                Data Analyst
                Machine Learning Engineer
                Data Engineer 
                </div>''', unsafe_allow_html=True) 
    '\n\n'
    st.image('Remarques.png')

if page == pages[1]: 
    st.title(':orange[Preprocessing]')    
    st.image('Preprocessing.png')

if page == pages[2]: 
    st.title(':orange[Visualisation]')
    #st.header("Titre")
    #st.write("write")
    #st.markdown("Markdown")
    tab1, tab2 = st.tabs(["📈 Chart 1", ":round_pushpin: Chart 2"])
    tab1.subheader("Répartition des métiers de la Data")
    tab1.image("Piechart.png")
    tab1.info("Nous constatons une forte concentration des Data Scientist (47%).") 
    #tab2.subheader("A tab with the data")

if page == pages[3]: 
    st.title(':orange[Modélisation]')
    option = st.selectbox(
        'Quel modèle choississez vous?',
        ('SVM', 'KNN','Arbre de décision', 'RandomForest', 'Regression logistique'))
    st.write('Vous avez choisi:', option)

    st.image("modèles.png")
    st.header("Choix des modèles")

    #st.write("write")
    #st.markdown("Markdown")

if page == pages[4]: 
    st.title(':orange[Conclusion]')
    #st.header("Titre")
    #st.write("write")
    #st.markdown("Markdown")

    st.header("Ouvertures")

    col1, col2 = st.columns(2)

    with col1:
        st.write('Prise en compte de tous les métiers de la data')

    with col2:
        st.write('Elargissement du modèle aux non informaticiens')

if page == pages[5]: 
    st.text('Fixed width text')
    st.markdown('_Markdown_') # see *
    st.caption('Balloons. Hundreds of them...')
    st.latex(r''' e^{i\pi} + 1 = 0 ''')
    st.write('Most objects') # df, err, func, keras!
    st.write(['st', 'is <', 3]) # see *
    st.title('My title')
    st.header('My header')
    st.subheader('My sub')
    st.code('for i in range(8): foo()')
    st.button('Hit me')
    st.checkbox('Check me out')
    st.radio('Radio', [1,2,3])
    st.selectbox('Select', [1,2,3])
    st.multiselect('Multiselect', [1,2,3])
    st.slider('Slide me', min_value=0, max_value=10)
    st.select_slider('Slide to select', options=[1,'2'])
    st.text_input('Enter some text')
    st.number_input('Enter a number')
    st.text_area('Area for textual entry')
    st.date_input('Date input')
    st.time_input('Time entry')
    st.file_uploader('File uploader')
    st.camera_input("一二三,茄子!")
    st.color_picker('Pick a color')