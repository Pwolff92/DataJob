import streamlit as st
import numpy as np
import pandas as pd

st.sidebar.title("DataJob :chart_with_downwards_trend:")
st.sidebar.header("Menu")
pages =["Exploration","Preprocessing","Visualisation","Modélisation", "Conclusion", "Ouvertures"]
page = st.sidebar.radio("",options = pages)
'\n\n'
st.sidebar.info(
    "Projet Datajob - Promotion Bootcamp mars 2023"
    "\n\n"
    "Participants:"
    "\n\n"
    "David DUBOIS"
    "\n\n"
    "Pauline WOLFF"
    "\n\n"
    "Sophie LAUSSEL\n "
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
    st.title(':orange[Preprocessing] :tornado:')    
    st.write('''
             - Suppression de la première ligne avec le nom des questions \n\n
             - Suppression de la colonne ***duration*** \n\n
             - Suppression des colonnes ***partie B*** qui correspondaient aux réponses des non-salariés \n\n
             - Regroupement des colonnes à réponses multiples afin d'éliminer un maximum de ***NaN*** et pour nous permettre d'utiliser ses données dans nos graphiques \n\n
             - Suppression des colonnes à réponses multiples \n\n
             - Renommer les colonnes \n\n
             - Suppression des doublons \n\n
             - Suppression des ***métiers*** qui ne font pas partie de la data \n\n
             - Remplacement des ***NaN*** par le mode \n\n
             ''')

if page == pages[2]: 
    st.title(':orange[Visualisation] :eyes:')
    #st.header("Titre")
    #st.write("write")
    #st.markdown("Markdown")
    tab1, tab2, tab3, tab4, tab5, tab6= st.tabs(["📈 Pie chart", "📈 Chart 2","📈 Chart3","📈 Chart4","📈 Chart5","📈 Heatmap"])
    tab1.subheader("Répartition des métiers de la Data")
    tab1.image("Piechart.png")
    tab1.info("Nous constatons une forte concentration des Data Scientist (47%).") 
    #tab2.subheader("A tab with the data")

    tab2.subheader("La Data dans le monde")
    tab2.image("pays1.png")
    tab2.image("pays.png")
    tab2.info("Forte concentration des profils en Inde et aux Etats-Unis")

    tab3.subheader("Age")
    tab3.image("Age.png")
    tab3.info("Concentration des 22-29 ans")

    tab4.subheader("Rémunération")
    tab4.image("Remuneration.png")
    tab4.info("Quelques valeurs extrèmes")

    tab5.subheader("Langage de programmation")
    tab5.image("language.png")
    tab5.image("langage par metier.png")
    tab5.info("Les deux langages les plus utilisés en programmation sont  Python et  SQL.")

    tab6.subheader("Heatmap")
    tab6.image("heatmap.png")
    tab6.image("zoom heatmap.png")
    tab6.info("La heatmap complète contenant un volume important de données, nous avons décidé de faire une analyse ciblée sur les questions sur le machine learning et le cloud.")

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
        code = st.checkbox('Voir code')
        if code :
            st.code(
                '''
                param_grid = {'criterion': ['gini', 'entropy'], 'max_depth': np.arange(3, 10)}
                clf_gs = GridSearchCV(model, param_grid) 
                clf_gs.fit(X_train, y_train)
                ''')
    elif selected == 'RandomForest' :
        st.image('RF.png')
        st.info(":red[Accuracy à **0,57** avant optimisation, et 0,55 après optimisation] \n\n L'amélioration du modèle n'a pas permis d'améliorer le score et détecte très mal la classe 3, le seul avantage est qu'il évite un overfitting. \n\n :point_right: **Modèle sélectionné !**")    
        code = st.checkbox('Voir code')
        if code :
            st.code(
                '''
                param_grid = {'criterion': ['gini', 'entropy'], 'max_depth': np.arange(3, 20)}
                clf_gs = GridSearchCV(rf, param_grid) 
                clf_gs.fit(X_train, y_train)
                ''')
    else :
        st.image('RL.png')
        st.info(":red[Accuracy à 0,56 avant optimisation, **0,57** après optimisation et mauvaise détection de la classe 3] \n\n Pas d'amélioration de modèle. \n\n :point_right: **Modèle non sélectionné**")    
        code = st.checkbox('Voir code')
        if code :
            st.code(
                '''
                parameters = {'penalty' : ['l1','l2'], 
                            'C': np.logspace(-3,3,7),
                            'solver'  : ['newton-cg', 'lbfgs', 'liblinear']}
                clf_gs = GridSearchCV(reglog,
                                    param_grid = parameters,
                                    scoring='accuracy',
                                    cv=10) 
                clf_gs.fit(X_train, y_train)
                ''')
    code = st.checkbox('Voir le comparatif')
    if code :
            st.subheader("Coefficient :red[avant] optimisation")
            df = pd.read_csv("RecapML_1.csv", sep=';')
            st.dataframe(df.style.highlight_max(axis=0))

            st.subheader("Coefficient :red[après] optimisation")
            df = pd.read_csv("RecapML_2.csv", sep=';')
            st.dataframe(df.style.highlight_max(axis=0))

if page == pages[4]: 

    st.title(':orange[Conclusion] :ballot_box_with_check:')
    #st.header("Titre")
    #st.write("write")
    #st.markdown("Markdown")
    st.write('''
            - il est primordial de **prendre le temps de bien comprendre** l’objectif du projet ; ici, un cas de classification, puisque cet objectif va sous-tendre l’ensemble de notre travail (par exemple, la réduction de dimension de données)\n
            - l’exploration, l’analyse et le pré-processing des données sont des tâches **complexes**, très **chronophages** mais **indispensables** avant de construire des modèles de Machine Learning (ML). 
            - l’utilisation des modèles de ML standards comme le SVM, le Random Forest… fut **simple** ; il nous a suffi d’appliquer les commandes des cours de Datascientest en considérant ces modèles comme des utilitaires ou des boites noires
            - les **taux de prédiction** obtenus par les multiples modèles de ML tournaient autour de seulement 50%. Ceux-ci ne sont **pas satisfaisants**, nous avons alors optimisé ces modèles avec des techniques genre Bagging, Boosting… mais aussi en faisant varier les valeurs de leurs hyperparamètres via la méthode GridSearchCV
            - ces deux voies ne nous ont pas permis de dépasser un taux de 56% ; le **frein** principal à nos tentatives d’optimisations fut notre **niveau technique sur le ML** et la difficulté à appréhender le rôle de chaque **hyperparamètre** de chaque modèle de ML
            - le ML n’est **pas une solution miracle** ; si le problème à traiter est trop complexe et les données pas assez nombreuses ou de qualité, notre modèle ne pourra pas atteindre un taux de précision de 70 ou 80%
            ''')
    
if page == pages[5]:
    st.title(':orange[Ouvertures] 	:globe_with_meridians:')
    st.subheader('Ouverture 1 : prise en compte de tous les métiers de la data')

    st.write('''
            Pour notre projet, nous avons filtré les données du sondage de Kaggle pour ne retenir que quatre métiers : 
            ***Data Analyst, Data Scientist, Data Engineer, Machine Learning Engineer***
            \n\n
            En réalité, le monde de la data est 
            bien plus complexe et ses métiers 
            plus nombreux. 
            \n\n
            En se basant sur ces sites web, nous
            avons identifié vingt métiers :
            - https://www.data-bird.co/metiers-data#data-steward 
            - https://www.kdnuggets.com/2021/10/guide-14-different-data-science-jobs.html

            Une fois notre modèle de ML optimisé sur les quatre métiers de base, nous pourrons tester celui-ci sur l’ensemble des vingt. L’objectif sera à nouveau de trouver le poste le plus précisément adapté à chaque informaticien en reconversion. 
            - Architecte Big Data
            - Business analyst
            - Business intelligence (BI) developer
            - Chief Data Officer
            - Computer & information research scientist Data analyst
            - Dataarchitect
            - Data engineer
            - Data manager
            - Data miner
            - Data modeler
            - Data Protection Officer Data scientist
            - Data steward
            - Database administrator 
            - Machine Learning Engineer 
            - Marketing scientist 
            - Quantitative analyst 
            - Software engineer 
            - Statistician
            ''')
    
    st.subheader('Ouverture 2 : élargissement du modèle aux non informaticiens')
    st.write('''
            Un autre axe d’évolution sera d’adapter notre modèle aux personnes n’ayant aucun background informatique et désireuses de travailler dans le monde de la data (par goût ou opportunité économique). 
            Dans ce cas, les données en entrée seront de nature totalement différente de celles du sondage de Kaggle. 
		
            Nous pourrons utiliser des attributs non liés à l’informatique pour construire ce nouveau modèle de ML :
            - langues parlées
            - type d’étude (scientifique, littéraire, économique…)
            - appétence pour les langages informatiques ou le management
            - salaire souhaité
            - autres
            À partir de ces attributs, notre modèle devra proposer un poste dans la data où la personne aura le plus de chance de réussir sa reconversion.
            ''')
