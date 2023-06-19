from Classes.Database import Database

db = Database("v04")

db.run_drop()

db.run_create()
db.run_seed()

