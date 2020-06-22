import conf_management as ConfMgt
import psycopg2
from random import randrange


class Recipe:
    def __init__(self, id, is_lunch, is_dinner, for_adult, for_kids, name):
        self.id = id
        self.is_lunch = is_lunch
        self.is_dinner = is_dinner
        self.for_adult = for_adult
        self.for_kids = for_kids
        self.name = name

    def get_recipes(where=''):
        recipe_list = []

        connection = None

        try:
            connection = ConfMgt.get_connection_by_config()

            cursor = connection.cursor()

            sql = (
                'SELECT '
                'id,'
                'is_lunch,'
                'is_dinner,'
                'for_adult,'
                'for_kids,'
                'name'
                ' FROM menu_recipe'
            )

            sql += where

            cursor.execute(sql)
            record = cursor.fetchall()

            for row in record:
                my_recipe = Recipe(
                    id=row[0],
                    is_lunch=row[1],
                    is_dinner=row[2],
                    for_adult=row[3],
                    for_kids=row[4],
                    name=row[5]
                )

                recipe_list.append(my_recipe)
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            # closing database connection.
            if(connection):
                cursor.close()
                connection.close()

        return recipe_list

    def get_text_recipes():
        recipe_names = ''

        recipes = Recipe.get_recipes()

        for recipe in recipes:
            recipe_names += '\n' + recipe.name

        return recipe_names

    def get_random_recipe():
        recipe_name = ''

        recipes = Recipe.get_recipes()

        if len(recipes) > 0:
            recipe = recipes[randrange(len(recipes))]
            recipe_name = recipe.name

        return recipe_name

    def get_random_recipe_filtered(is_lunch=False, is_dinner=False, for_adult=False, for_kids=False):
        recipe_name = ''
        where_statement = " WHERE name <> ''"

        if is_lunch:
            where_statement += ' AND is_lunch = true'

        if is_dinner:
            where_statement += ' AND is_dinner = true'

        if for_adult:
            where_statement += ' AND for_adult = true'

        if for_kids:
            where_statement += ' AND for_kids = true'

        recipes = Recipe.get_recipes(where=where_statement)

        if len(recipes) > 0:
            recipe = recipes[randrange(len(recipes))]
            recipe_name = recipe.name

        return recipe_name
