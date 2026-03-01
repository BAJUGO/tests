from pymongo import MongoClient

client = MongoClient(host='localhost',
                     port=27017,
                     username="user",
                     password="password"
                     )

# print(client.list_database_names())

# * Выбрали БД из клиента (в случае отсутствия создали)
db = client["test"]

# print(db.list_collection_names())

# * Выбрали коллекцию из БД (в случае отсутствия ... )
users = db['test_users']

# * Создать что-то в коллекцию
# result = users.insert_one({
#     "name": "Ivan",
#     "age": 20,
#     "skills": ["python", "django", "flask"]
# })

# * Создать много чего-то в коллекцию
# * Парамметр ordered=False позволит БДшке вставлять всевозможные документы,
# * даже если один из них упал с ошибкой

# users.insert_many([
#     {"name": "Anna", "age": 22},
#     {"name": "Max", "age": 30}
# ], ordered=True)


for doc in users.find():
    print(doc)

print()

#* lt, gt если мы пишем вот такое вот условие
for doc in users.find({"age": {"$lt": 23}}):
    print(doc)


print()

for doc in users.find({"name": "Anna"}):
    print(doc)

print()


#* Почему-то Id здесь обязательное, но так можно написать порядок и вообще
#* что ты хочешь выводить, а что нет
for doc in users.find({}, {"_id": 0, "age": 2, "name": 1}):
    print(doc)



users.update_one(
    {"name": "Anna"},
    {"$set": {"updated": True}}
)


users.update_many(
    {"age": {"$lt": 18}},
    {"$set": {"kid": True}}
)


#users.delete_one({"name": "Anna"})
#users.delete_many({"young": True})




