import streamlit as st
import numpy as np
import pandas as pd

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
    '\n'

    st.header("Objectifs")
    st.markdown(
                """
                Les principaux objectifs qui ressortent à travers ce sondages sont :
                - analyser les profils des utilisateurs de Kaggle au regard de leur métier
                - élaborer un modèle permettant d’identifier le métier data le plus adapté, en fonction des compétences des personnes souhaitant intégrer le domaine de la data.
                """
                )    
    '\n'

    st.header("Cadre")
    st.markdown('''<div style="text-align: justify;">
                Le jeu de données sur lequel nous allons travailler provient d’un sondage créé et lancé en 2020 sur 171 pays. Il était destiné aux personnes inscrites sur le site Kaggle (plateforme web interactive qui propose des compétitions d'apprentissage automatique en science des données). Au total, 20 000 personnes ont été sondées. L’étude est essentiellement centrée sur le Machine Learning.
                Nous procédons à une première analyse visuelle sur le jeu de données (à l’aide de la méthode info de pandas). 
                </div>''', unsafe_allow_html=True)
     
    st.markdown('''<div style="text-align: justify;">
                Ainsi le jeu de données se décompose de la manière suivante :
                </div>''', unsafe_allow_html=True)
    st.markdown("- 355 colonnes,")
    st.markdown("- l’intégralité des données sont de type objet donc qualitatives, il y a 20 037 entrées.")
    st.markdown(''' <style> [data-testid="stMarkdownContainer"] ul{list-style-position: inside;}</style>    ''', unsafe_allow_html=True)

    st.markdown('''<div style="text-align: justify;">
                D’un point de vue technique, toutes les données étant de type qualitatif, nous aurons un important travail d’encodage à faire pour pouvoir traiter la donnée. 
                </div>''', unsafe_allow_html=True) 
    '\n'
    
    st.header("Variable cible :dart:")
    st.markdown('''<div style="text-align: justify;">
                La variable cible de notre projet correspond aux métiers de la data dans le jeu de données, cette variable se nomme “titre’, que nous appellerons Métier, terme plus explicite. Nous étudierons les 4 métiers : 
                Data Scientest
                Data Analyst
                Machine Learning Engineer
                Data Engineer 
                </div>''', unsafe_allow_html=True) 
    '\n'
    
    st.header("Remarques sur le dataset")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader(':red[Difficultés]')
        st.write(
            '''
            - les questions à choix multiples génèrent une colonne distincte dans le dataset : **355** colonnes pour **39** questions
            - une grande quantité d’intervalles et de bornes : catégorie “objet” par défaut
            - certaines questions réservées aux étudiants et aux employés
            - des questions ne sont débloquées qu'en fonction de la réponse à une question en amont -> beaucoup de “**NaN**” générés artificiellement
            - nous identifions des “**None**” et “**other**” qui seront à analyser par la suite
            - doublons à analyser et corriger
            '''
        )

    with col2:
        st.subheader(':green[Points positifs]')
        st.write(
            '''
            - aucune zone de texte libre 
            - ensemble des réponses normalisé
            - pas de différences entre majuscules ou minuscules par exemple
            - pas de nettoyage à faire sur la police ou la casse
            ''')


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
    st.title(':orange[Modélisation ]	:sparkles:')
    options = ['','SVM', 'KNN','Arbre de décision', 'RandomForest', 'Regression logistique']
    st.header("Sélection d'un modèle")
    selected = st.selectbox('Quel modèle choississez vous?',
                            options = options)
    st.write('Vous avez choisi:', selected)

    if selected == '':
        st.write("")
    elif selected == 'SVM':
        st.image('SVM.png')
        st.info(":red[Accuracy à **0,56** après optimisation et mauvaise détection de la classe 3.] \n\n Bien que nous ayons amélioré l'accuracy, nous avons perdu en qualité sur la détection de la classe 3. \n\n :point_right: **Modèle non sélectionné**")
        code = st.checkbox('Voir code')
        if code :
            st.code(
                '''
                from sklearn.multiclass import OneVsRestClassifier
                ovr2=OneVsRestClassifier(SVC())
                ovr2.fit(X_train,y_train)
                ''')    
    elif selected == 'KNN' :
        st.image('KNN.png')
        st.info(":red[Accuracy à **0,45** après optimisation et mauvaise détection de la classe 3.] \n\n Nous n'avons pas amélioré ce modèle. \n\n :point_right: **Modèle non sélectionné**")   
        code = st.checkbox('Voir code')
        if code :
            st.code(
                '''
                knn = neighbors.KNeighborsClassifier()
                parametres = {'n_neighbors': range(2,50)}
                grid_knn = model_selection.GridSearchCV(estimator=knn, param_grid=parametres)
                grid_knn.fit(X_train, y_train)
                grid_knn.best_params_
                grid_knn.score(X_test, y_test)
                ''')
    elif selected == 'Arbre de décision' :
        st.image('ADD.png')
        st.info(":red[Accuracy à **0,44** après rééquilibrage.] \n\n Le rééquilibrage des classes a permis de détecter la 3ème classe, mais la détection des classes 0 et 1 a baissé. \n\n :point_right: **Modèle non sélectionné**")   
    elif selected == 'RandomForest' :
        st.image('RF.png')
        st.info(":red[Accuracy à **0,57** avant optimisation, et 0,55 après optimisation] \n\n L'amélioration du modèle n'a pas permis d'améliorer le score et détecte très mal la classe 3, le seul avantage est qu'il évite un overfitting. \n\n :point_right: **Modèle sélectionné !**")    
    else :
        st.image('RL.png')
        st.info(":red[Accuracy à 0,56 avant optimisation, **0,57** après optimisation et mauvaise détection de la classe 3] \n\n Pas d'amélioration de modèle. \n\n :point_right: **Modèle non sélectionné**")    

    code = st.checkbox('Voir le comparatif')
    if code :
        st.subheader("Coefficient avant optimisation")
        df = pd.read_csv("RecapML_1.csv", sep=';')
        st.dataframe(df.style.highlight_max(axis=0))

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
    st.write("The following list won’t indent no matter what I try:")
    st.markdown("- Item 1")
    st.markdown("- Item 2")
    st.markdown("- Item 3")

    st.markdown('''
    <style>
    [data-testid="stMarkdownContainer"] ul{
    list-style-position: inside;
    }
    </style>
    ''', unsafe_allow_html=True)
    st.write("The following list won’t indent no matter what I try:")
    st.markdown("- Item 1")
    st.markdown("- Item 2")
    st.markdown("- Item 3")

    st.markdown('''
        <style>
        [data-testid="stMarkdownContainer"] ul{
            padding-left:40px;
        }
        </style>
        ''', unsafe_allow_html=True)