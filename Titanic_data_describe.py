import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

way_to_data = "/Users/alexandreev/Desktop/Python/Titanic.csv"

data_to_analysis = pd.read_csv(way_to_data)

print("1. ПРОВЕДЕМ ОБЩИЙ ОБЗОР ДАННЫХ\n")

print("Количество строк:" , data_to_analysis.shape[0])

print("Количество столбцов:" , data_to_analysis.shape[1])

print("Каждая строка обозначает отдельного пассажира на корабле, а каждый столбец - характеристика, "
      "соответствующая этому пассажиру.")

print("Выведем подробную информацию о каждом столбце:\n")

print(data_to_analysis.info())

print("\nCтановится видно, что пять столбцов имеют целочисленный тип, "
      "пять переменных имеет тип строки и два столбца - это числа с плавающей точкой.\n"
      "Кроме того, не все столбцы содержат в себе 891 значение, что указывает на наличие пропусков.")

print("\n 2. ПРОИЗВЕДЕМ ПОИСК ПРОПУЩЕННЫХ ЗНАЧЕНИЙ\n")

print(data_to_analysis.isnull().sum())

print("\nЕсть несколько столбцов, в которых отсутствуют значения:\n"
      "\n Age"
      "\n Cabin"
      "\n Embarked \n"
      "\n77% данных пропущены в столбце Cabin. Напротив, у Embarked только 2 пропущенных значения. "
                                "\nВ столбце Age 177 пропущенных значений.")

print("\nЛинейный график (fig.1) и тепловая карта (fig.2) показывают количество пропущенных значений во всех столбцах. ")

pd.DataFrame(data_to_analysis.isnull().sum()).plot.line().set_title("Number of missing values in the given features")

plt.figure()

sns.heatmap(data_to_analysis.isnull(), cbar = False).set_title("Missing values heatmap")


print("\n 3. ОСУЩЕСТВИМ ПОИСК КАТЕГОРИАЛЬНЫХ ПЕРЕМЕННЫХ\n")

print("Чтобы увидеть категориальные данные выведем все столбцы с количеством уникальных значений, которые они содержат:\n")

print(data_to_analysis.nunique())

print("\nСтановится видно, что переменные Survived и Sex имеют всего два разных состояния,"
      " Embarked и PClass имеют три возможных состояния."
      "\nТаким образом, можно сделать вывод, что четыре столбца представленны категореальными данными - Survived, Sex, "
      "Embarked и PClass.")

print("\n 4. РАССМОТРИМ ОТДЕЛЬНО КАЖДУЮ ПЕРЕМЕННУЮ\n")

print("\n  4.1. Survived\n")

print("Горизонтальный график (fig.3) показывает процент людей, которые выжили (1), и процент людей, которые, "
      "\nне смогли выбраться живыми (0) после катастрофы. Более 60% людей на корабле погибли.")

plt.figure()

(data_to_analysis.Survived.value_counts(normalize=True) * 100).plot.barh().set_title("Training Data - Percentage of"
                                                                                     " people survived and Deceased")
print("\n  4.2. Pclass\n")

plt.figure()

data_to_analysis.Pclass.value_counts().plot.pie().legend(
    labels=["Class 3","Class 1","Class 2"],
    loc='center right',
    bbox_to_anchor=(2.25, 0.5)).set_title("People travelling in different classes")

print("Pclass представляет собой классы купленных пассажирами корабля билетов. Было три класса. "
      "\nВ объединенном наборе данных (fig.4) явное большинство путешествовало в третьем классе,\n"
      "затем по численности следовали пассажиры второго класса. Самыми малочисленными были пассажиры первого класса.\n")

pclass_1_survivor_distribution = round(
    (data_to_analysis[data_to_analysis.Pclass == 1].Survived == 1).value_counts()[1]/len(data_to_analysis[data_to_analysis.Pclass == 1]) * 100, 2)

pclass_2_survivor_distribution = round(
    (data_to_analysis[data_to_analysis.Pclass == 2].Survived == 1).value_counts()[1]/len(data_to_analysis[data_to_analysis.Pclass == 2]) * 100, 2)

pclass_3_survivor_distribution = round(
    (data_to_analysis[data_to_analysis.Pclass == 3].Survived == 1).value_counts()[1]/len(data_to_analysis[data_to_analysis.Pclass == 3]) * 100, 2)

pclass_perc_df = pd.DataFrame(
    { "Percentage Survived":{"Class 1": pclass_1_survivor_distribution,
                             "Class 2": pclass_2_survivor_distribution, "Class 3": pclass_3_survivor_distribution},
     "Percentage Not Survived":
         {"Class 1": 100-pclass_1_survivor_distribution,
          "Class 2": 100-pclass_2_survivor_distribution,
          "Class 3": 100-pclass_3_survivor_distribution}})

pclass_perc_df.plot.bar().set_title("Percentage of people survived on the basis of class")

print("Из fig.5 видно, что было спасено более 60% пассажиров первого класса."
      "\nСовершенно иная картина была представленна для выживших пассажиров второго и третьего классов, поскольку только "
      "47% пассажиров второго класса смогли выжить. "
      "\nВ случае пассажиров третьего статистика была наиболее печальной - удалось выжить всего 30%.\n")

print(pclass_perc_df)

print("\n  4.3. Sex\n")

print("Примерно 65% пассажиров составляли мужчины, а остальные 35% - женщины (fig.6.). \n"
      "Однако, процент выживших женщин был на много выше, чем таковой у мужчин (fig.7.).")

plt.figure()

fig_sex = (data_to_analysis.Sex.value_counts(normalize = True) * 100).plot.bar()

male_pr = round((data_to_analysis[data_to_analysis.Sex == 'male'].Survived == 1).value_counts()[1]/len(data_to_analysis.Sex) * 100, 2)

female_pr = round((data_to_analysis[data_to_analysis.Sex == 'female'].Survived == 1).value_counts()[1]/len(data_to_analysis.Sex) * 100, 2)

sex_perc_df = pd.DataFrame(
    { "Percentage Survived":{"male": male_pr,"female": female_pr},  "Percentage Not Survived":{"male": 100-male_pr,"female": 100-female_pr}})

sex_perc_df.plot.barh().set_title("Percentage of male and female survived and Deceased")

print("\n  4.4. Age\n")

print(pd.DataFrame(data_to_analysis.Age.describe()))

data_to_analysis['Age_Range'] = pd.cut(data_to_analysis.Age, [0, 10, 20, 30, 40, 50, 60,70,80])

plt.figure()

sns.countplot(x = "Age_Range", hue = "Survived", data = data_to_analysis, palette=["C1", "C0"]).legend(labels = ["Deceased", "Survived"])

print("\nОписание столбца Age  указывает, что самому молодому пассажиру на борту было около 4 месяцев,"
      "а самому старому пассажиру было 80 лет (fig. 8).\n"
      "Средний возраст пассажиров на борту был чуть менее 30 лет. Однако следует помнить, "
      "что в этих наблюдениях имеются пропущенные значения.")

plt.figure()

sns.histplot(data_to_analysis['Age'].dropna(),color='darkgreen', bins=30)

print("Судя по всему, было спасено больше детей младше 10 лет, чем погибло. Для всех остальных возрастных "
      "групп количество погибших было больше, чем количество выживших (fig.9). ")

print("\n  4.5. SibSp\n")

print("\nSibSp - это количество родственников на борту.\n")

print(data_to_analysis.SibSp.describe())

print("\nМаксимум 8 родствеников путешествовало вместе друг с другом (fig. 10)."
      "\nБолее 90% людей путешествовали в одиночку или с одним из своих родствеников."
      "\nШансы на выживание резко падали, если кто-то путешествовал с более чем двумя родствениками (fig.10).")

ss = pd.DataFrame()

ss['survived'] = data_to_analysis.Survived

ss['sibling_spouse'] = pd.cut(data_to_analysis.SibSp, [0, 1, 2, 3, 4, 5, 6,7,8], include_lowest = True)

plt.figure()

x = sns.countplot(x = "sibling_spouse", hue = "survived", data = ss, palette=["C1", "C0"]).legend(labels = ["Deceased", "Survived"])

x.set_title("Survival based on number of siblings or spouses")

print("\n  4.6. Parch\n")

print("Подобно SibSp, эта переменная содержала количество родителей или детей, с которыми путешествовал каждый пассажир.\n")

print(pd.DataFrame(data_to_analysis.Parch.describe()))

pc = pd.DataFrame()

print("\nМаксимум 9 родителей / детей путешествовали вместе с одним из пассажиров.")

pc['survived'] = data_to_analysis.Survived

pc['parents_children'] = pd.cut(data_to_analysis.Parch, [0, 1, 2, 3, 4, 5, 6], include_lowest = True)

plt.figure()

x = sns.countplot(x = "parents_children", hue = "survived", data = pc, palette=["C1", "C0"]).legend(labels = ["Deceased", "Survived"])

x.set_title("Survival based on number of parents/children")

print("Как видно из графиков, у людей путешествующих в одиночку было больше шансов на выживание (fig.11).")

print("\n  4.7. Ticket\n")

print("Поскольку переменная Ticket не предоставляет никакой интересной информации, не будем ее рассматривать.")

print("\n  4.8. Fare\n")

print("Данная переменная показывает сколько денег платили пассажиры за билет.")

data_to_analysis.Fare.describe()

data_to_analysis['Fare_Category'] = pd.cut(data_to_analysis['Fare'], bins=[0,7.90,14.45,31.28,120], labels=['Low','Mid',
                                                                                      'High_Mid','High'])
plt.figure()
parch_graph = sns.countplot(x = "Fare_Category", hue = "Survived",
                            data = data_to_analysis, palette=["C1", "C0"]).legend(labels = ["Deceased", "Survived"])

parch_graph.set_title("Survival based on fare category")

print("По графику (fig.12) можно увидеть, что существует сильная корреляция между ценой за проезд и выживанием.")

print("\n  4.9. Cabin\n")

print("Слишком много пропущенных значений. Нельзя ничего сказать о данной переменной.")

print("\n  4.10. Embarked\n")

print("Переменная Embarked содержит информацию о месте посадки пассажира. Есть три возможных уровня для Embark "
      "- Саутгемптон, Шербур, Квинстаун.")

plt.figure()

embarked = sns.countplot(x = "Embarked", hue = "Survived", data = data_to_analysis, palette=["C1", "C0"])

embarked.set_xticklabels(["Southampton","Cherbourg","Queenstown"])

embarked.legend(labels = ["Deceased", "Survived"])

embarked.set_title("Survival based on embarking point.")

print("По совокупным данным, более 70% людей были из Саутгемптона. Чуть менее 20% - из Шербура, остальные - из Квинстауна."
      "\nСоответственно выжило больше всего людей из Саутгемптона (fig.13). ")

print("\n 5.ВЫВОД\n")

print("Таким образом было проведино описание данных о пассажирах корабля Титаник. Результаты анализа свидетельствуют\n"
      "о том, что в данных присутствует большое количество пропущенных значений, таким образом перед продолжением дальнейшей работы\n"
      "необходимо исключить из данных переменную Cabin и произвести импликацию данных в переменной Age. Также была найдена\n"
      "корреляция между переменными Fare_Category и Survived, что необходимо будет учесть в случае принятия решения о\n"
      "выполнении регриссионого анализа в дальнейшем.")

plt.show()
