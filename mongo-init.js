db = db.getSiblingDB('mydatabase');  // создаёт и переключается на mydatabase

db.createUser({
  user: 'appuser',
  pwd: 'apppassword',
  roles: [
    {
      role: 'readWrite',
      db: 'mydatabase',
    },
  ],
});

db.createCollection("events")
