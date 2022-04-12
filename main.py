from nutrition import *
import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    food = input("What food have you eaten?\n")
    nutrition = NutritionAPI()
    response = nutrition.getNutritionData(food)
    print(nutrition.getNutritionData(food))
    labels = ['Protein', 'Carbohydrates', 'Fat', 'Fiber']
    total = response["protein_g"] + response["carbohydrates_total_g"] + response["fat_total_g"] + response["fiber_g"]
    try:
        sizes = [100 * response["protein_g"]/total, 100 * response['carbohydrates_total_g']/total, 100 * response["fat_total_g"]/total, 100 * response["fiber_g"]/total]
    except:
        print("Are you fucking blind? You cant divide by 0!")

    fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

    macronutrients = [str(response["protein_g"]) + " g Protein",
              str(response["carbohydrates_total_g"]) + " g Carbohydrates",
              str(response["fat_total_g"]) + " g Fat",
              str(response["fiber_g"]) + " g Fiber"]

    data = [float(x.split()[0]) for x in macronutrients]
    ingredients = [x.split()[-1] for x in macronutrients]


    def func(pct, allvals):
        absolute = int(np.round(pct / 100. * np.sum(allvals)))
        return "{:.1f}%\n({:d} g)".format(pct, absolute)


    wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                      textprops=dict(color="w"))

    ax.legend(wedges, ingredients,
              title="Nutrition",
              loc="center left",
              bbox_to_anchor=(1, 0, 0.5, 1))

    plt.setp(autotexts, size=8, weight="bold")

    ax.set_title(str(response["serving_size_g"]) + "g " + str(response["name"]))

    plt.show()


