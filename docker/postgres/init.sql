create table if not exists menu_recipe
(
    id  serial not null constraint menu_recipe_pk primary key,
    is_lunch  boolean default false not null,
    is_dinner boolean default false not null,
    for_adult boolean default false not null,
    for_kids  boolean default false not null,
    name text
);